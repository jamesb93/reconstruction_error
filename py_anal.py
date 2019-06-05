from databending_utilities import *
import librosa
import librosa.display
import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy
import sklearn

from sklearn import decomposition
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

### Folder Setup ###
root = get_path()
audio_folder = f'{root}/DataAudio'
audio_files = os.listdir(audio_folder)
random_file = random.choice(audio_files)
full_path = os.path.join(audio_folder, random_file)


########## Segmentation ##########
y, sr = librosa.load('/Users/jamesbradbury/dev/data_bending/DataAudio/libLLVMAMDGPUDesc.a.wav', sr=None)

### Decomposition ###
# S_full, phase = librosa.magphase(librosa.stft(y))

# # We'll compare frames using cosine similarity, and aggregate similar frames
# # by taking their (per-frequency) median value.
# #
# # To avoid being biased by local continuity, we constrain similar frames to be
# # separated by at least 2 seconds.
# #
# # This suppresses sparse/non-repetetitive deviations from the average spectrum,
# # and works well to discard vocal elements.

# S_filter = librosa.decompose.nn_filter(S_full,
#                                        aggregate=np.median,
#                                        metric='cosine',
#                                        width=int(librosa.time_to_frames(2, sr=sr)))

# # The output of the filter shouldn't be greater than the input
# # if we assume signals are additive.  Taking the pointwise minimium
# # with the input spectrum forces this.
# S_filter = np.minimum(S_full, S_filter)

# # We can also use a margin to reduce bleed between the vocals and instrumentation masks.
# # Note: the margins need not be equal for foreground and background separation
# margin_i, margin_v = 2, 10
# power = 2

# mask_i = librosa.util.softmask(S_filter,
#                                margin_i * (S_full - S_filter),
#                                power=power)

# mask_v = librosa.util.softmask(S_full - S_filter,
#                                margin_v * S_filter,
#                                power=power)

# # Once we have the masks, simply multiply them with the input spectrum
# # to separate the components

# S_foreground = mask_v * S_full
# S_background = mask_i * S_full

# plt.figure(figsize=(12, 8))
# plt.subplot(3, 1, 1)
# librosa.display.specshow(librosa.amplitude_to_db(S_full, ref=np.max),
#                          y_axis='log', sr=sr)
# plt.title('Full spectrum')
# plt.colorbar()

# plt.subplot(3, 1, 2)
# librosa.display.specshow(librosa.amplitude_to_db(S_background, ref=np.max),
#                          y_axis='log', sr=sr)
# plt.title('Background')
# plt.colorbar()
# plt.subplot(3, 1, 3)
# librosa.display.specshow(librosa.amplitude_to_db(S_foreground, ref=np.max),
#                          y_axis='log', x_axis='time', sr=sr)
# plt.title('Foreground')
# plt.colorbar()
# plt.tight_layout()
# plt.show()

# librosa.output.write_wav('/Users/jamesbradbury/desktop/foreground.wav', S_foreground, sr)
# librosa.output.write_wav('/Users/jamesbradbury/desktop/background.wav', S_background, sr)

### Spectrogram ###
S_full, phase = librosa.magphase(librosa.stft(y))

plt.figure(figsize=(12, 4))
librosa.display.specshow(librosa.amplitude_to_db(S_full, ref=np.max),
                         y_axis='log', x_axis='time', sr=sr)
plt.colorbar()
plt.tight_layout()
plt.show()

### Create and plot recurrence Matrix ###
mfcc = librosa.feature.mfcc(y, sr)
recur = librosa.segment.recurrence_matrix(mfcc)

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
librosa.display.specshow(recur, x_axis='time', y_axis='time')
plt.title('Recurrence')
plt.tight_layout()
plt.show()

### Timelag Filter ###
# mfcc = librosa.feature.mfcc(y, sr)
# rec = librosa.segment.recurrence_matrix(mfcc)
# from scipy.ndimage import median_filter
# diagonal_median = librosa.segment.timelag_filter(median_filter)
# rec_filtered = diagonal_median(rec, size=(1, 3), mode='mirror')
# rec_aff = librosa.segment.recurrence_matrix(mfcc, mode='affinity')
# rec_aff_fil = diagonal_median(rec_aff, size=(1, 3), mode='mirror')
# plt.figure(figsize=(8,8))
# plt.subplot(2, 2, 1)
# librosa.display.specshow(rec, y_axis='time')
# plt.title('Raw recurrence matrix')
# plt.subplot(2, 2, 2)
# librosa.display.specshow(rec_filtered)
# plt.title('Filtered recurrence matrix')
# plt.subplot(2, 2, 3)
# librosa.display.specshow(rec_aff, x_axis='time', y_axis='time',
#                           cmap='magma_r')
# plt.title('Raw affinity matrix')
# plt.subplot(2, 2, 4)
# librosa.display.specshow(rec_aff_fil, x_axis='time',
#                           cmap='magma_r')
# plt.title('Filtered affinity matrix')
# plt.tight_layout()
# plt.show()

### Agglomerative Clustering ###
# chroma = librosa.feature.chroma_stft(y, sr)
# bounds = librosa.segment.agglomerative(chroma, 5)
# bound_times = librosa.frames_to_time(bounds, sr=sr)

# plt.figure()
# librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
# plt.vlines(bound_times, 0, chroma.shape[0], color='linen', linestyle='--',
#             linewidth=2, alpha=0.9, label='Segment boundaries')
# plt.axis('tight')
# plt.legend(frameon=True, shadow=True)
# plt.title('Power spectrogram')
# plt.tight_layout()
# plt.show()

### Onset Detection ###
# onset_envelope = librosa.onset.onset_strength(y, sr)
# onsets = librosa.onset.onset_detect(onset_envelope)
# plt.subplot(2, 1, 1)
# plt.plot(onset_envelope, label='Onset Stregnth')
# plt.vlines(onsets, 0, onset_envelope.max(), color='r', alpha=0.25)
# plt.xticks([]), plt.yticks([])
# plt.legend(frameon=True)
# plt.axis('tight')
# plt.subplot(2, 1, 2)
# librosa.display.waveplot(y, sr)
# plt.show()

### Laplacian Segmentation ###
# BINS_PER_OCTAVE = 12 * 3
# N_OCTAVES = 8
# C = librosa.amplitude_to_db(np.abs(librosa.cqt(y=y, sr=sr,
#                                         bins_per_octave=BINS_PER_OCTAVE,
#                                         n_bins=N_OCTAVES * BINS_PER_OCTAVE)),
#                             ref=np.max)

# tempo, beats = librosa.beat.beat_track(y=y, sr=sr, trim=False)
# Csync = librosa.util.sync(C, beats, aggregate=np.median)

# # For plotting purposes, we'll need the timing of the beats
# # we fix_frames to include non-beat frames 0 and C.shape[1] (final frame)
# beat_times = librosa.frames_to_time(librosa.util.fix_frames(beats,
#                                                             x_min=0,
#                                                             x_max=C.shape[1]),
#                                     sr=sr)

# R = librosa.segment.recurrence_matrix(Csync, width=3, mode='affinity',
#                                       sym=True)

# # Enhance diagonals with a median filter (Equation 2)
# df = librosa.segment.timelag_filter(scipy.ndimage.median_filter)
# Rf = df(R, size=(1, 7))

# mfcc = librosa.feature.mfcc(y=y, sr=sr)
# Msync = librosa.util.sync(mfcc, beats)

# path_distance = np.sum(np.diff(Msync, axis=1)**2, axis=0)
# sigma = np.median(path_distance)
# path_sim = np.exp(-path_distance / sigma)

# R_path = np.diag(path_sim, k=1) + np.diag(path_sim, k=-1)

# deg_path = np.sum(R_path, axis=1)
# deg_rec = np.sum(Rf, axis=1)

# mu = deg_path.dot(deg_path + deg_rec) / np.sum((deg_path + deg_rec)**2)

# A = mu * Rf + (1 - mu) * R_path

# plt.figure(figsize=(8, 4))
# plt.subplot(1, 3, 1)
# librosa.display.specshow(Rf, cmap='inferno_r', y_axis='time',
#                          y_coords=beat_times)
# plt.title('Recurrence similarity')
# plt.subplot(1, 3, 2)
# librosa.display.specshow(R_path, cmap='inferno_r')
# plt.title('Path similarity')
# plt.subplot(1, 3, 3)
# librosa.display.specshow(A, cmap='inferno_r')
# plt.title('Combined graph')
# plt.tight_layout()

# L = scipy.sparse.csgraph.laplacian(A, normed=True)


# # and its spectral decomposition
# evals, evecs = scipy.linalg.eigh(L)


# # We can clean this up further with a median filter.
# # This can help smooth over small discontinuities
# evecs = scipy.ndimage.median_filter(evecs, size=(9, 1))


# # cumulative normalization is needed for symmetric normalize laplacian eigenvectors
# Cnorm = np.cumsum(evecs**2, axis=1)**0.5

# # If we want k clusters, use the first k normalized eigenvectors.
# # Fun exercise: see how the segmentation changes as you vary k

# k = 5

# X = evecs[:, :k] / Cnorm[:, k-1:k]

# # Plot the resulting representation (Figure 1, center and right)

# plt.figure(figsize=(8, 4))
# plt.subplot(1, 2, 2)
# librosa.display.specshow(Rf, cmap='inferno_r')
# plt.title('Recurrence matrix')

# plt.subplot(1, 2, 1)
# librosa.display.specshow(X,
#                          y_axis='time',
#                          y_coords=beat_times)
# plt.title('Structure components')
# plt.tight_layout()

# KM = sklearn.cluster.KMeans(n_clusters=k)

# seg_ids = KM.fit_predict(X)


# # and plot the results
# plt.figure(figsize=(12, 4))
# colors = plt.get_cmap('Paired', k)

# plt.subplot(1, 3, 2)
# librosa.display.specshow(Rf, cmap='inferno_r')
# plt.title('Recurrence matrix')
# plt.subplot(1, 3, 1)
# librosa.display.specshow(X,
#                          y_axis='time',
#                          y_coords=beat_times)
# plt.title('Structure components')
# plt.subplot(1, 3, 3)
# librosa.display.specshow(np.atleast_2d(seg_ids).T, cmap=colors)
# plt.title('Estimated segments')
# plt.colorbar(ticks=range(k))
# plt.tight_layout()

# bound_beats = 1 + np.flatnonzero(seg_ids[:-1] != seg_ids[1:])

# # Count beat 0 as a boundary
# bound_beats = librosa.util.fix_frames(bound_beats, x_min=0)

# # Compute the segment label for each boundary
# bound_segs = list(seg_ids[bound_beats])

# # Convert beat indices to frames
# bound_frames = beats[bound_beats]

# # Make sure we cover to the end of the track
# bound_frames = librosa.util.fix_frames(bound_frames,
#                                        x_min=None,
#                                        x_max=C.shape[1]-1)

# import matplotlib.patches as patches
# plt.figure(figsize=(12, 4))

# bound_times = librosa.frames_to_time(bound_frames)
# freqs = librosa.cqt_frequencies(n_bins=C.shape[0],
#                                 fmin=librosa.note_to_hz('C1'),
#                                 bins_per_octave=BINS_PER_OCTAVE)

# librosa.display.specshow(C, y_axis='cqt_hz', sr=sr,
#                          bins_per_octave=BINS_PER_OCTAVE,
#                          x_axis='time')
# ax = plt.gca()

# for interval, label in zip(zip(bound_times, bound_times[1:]), bound_segs):
#     ax.add_patch(patches.Rectangle((interval[0], freqs[0]),
#                                    interval[1] - interval[0],
#                                    freqs[-1],
#                                    facecolor=colors(label),
#                                    alpha=0.50))

# plt.tight_layout()
# plt.show()


########## Dimensionality Reduction ##########
# X = StandardScaler().fit_transform(X) # Standardise Data

# print(X)
# pca = decomposition.PCA(n_components=2)
# pca.fit(X)
# X = pca.transform(X)
# plt.scatter(X[:, 0], X[:, 1]) #scatterplot the first value against the second
# plt.show() #show plot


########## How to extract features ##########
# y, sr = librosa.load('/Users/jamesbradbury/dev/data_bending/DataAudio/fl.and~_lto.o.wav', sr=None)
# centroid = librosa.feature.spectral_centroid(y=y, sr=sr, n_fft=8192, hop_length=128)
# print(centroid)
# print(np.median(centroid))
# print(np.amax(centroid))
# X = librosa.feature.(y=y, sr=sr, hop_length=128, n_mfcc=13)