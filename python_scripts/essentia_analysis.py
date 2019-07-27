import essentia
from essentia.standard import *
import os
from db_vars import root, unique_audio_folder, unique_audio_files
import sys
import multiprocessing as mp

def descriptor_analyse(idx):
    for i in range(len(to_analyse)):
        audio_file = os.path.join(unique_audio_folder, to_analyse[idx])
        input_name = to_analyse[idx]
        loader = MonoLoader(filename=audio_file)
        audio = loader()
        # Whole Buffer
        pool = essentia.Pool()
        dynamic_complexity, loudness = f_dynamic_complexity(audio)
        pool.add(f'dynamic_complexity', dynamic_complexity)
        for frame in FrameGenerator(audio, frameSize = frame_size, hopSize = hop_size, startFromZero = True):
            f = frame
            wf = w(f) # windowed frame
            swf = f_spec(wf) # Simplification for a windowed spectral frame - returns the maginutde of the FFT
            
            spec_peaks_freq, spec_peaks_magn = f_spec_peaks(swf)
            mfcc_bands, mfcc_coeffs = f_mfcc(swf)
            rms = f_rms(f)
            spec_contrast, spec_valley = f_spec_contrast(swf)
            spec_energy = f_energy(swf)
            spec_crest = f_crest(swf)
            spec_complexity = f_spec_complexity(swf)
            strong_peak = f_strong_peak(swf)
            flux = f_flux(swf)
            pitch, pitch_confidence = f_yin(f)
            pitch_salience = f_pitch_salience(swf)
            dissonance = f_dissonance(spec_peaks_freq, spec_peaks_magn)
            hpcp = f_hpcp(spec_peaks_freq, spec_peaks_magn)
            hpcp_entropy = f_entropy(hpcp)
            hpcp_crest = f_crest(hpcp)
            harmonic_freq, harmonic_mag = f_harm_peaks(spec_peaks_freq, spec_peaks_magn, pitch)
            tristimulus = f_tristiumulus(harmonic_freq, harmonic_mag)
            inharmonicity = f_inharmonicity(harmonic_freq, harmonic_mag)
            odd_to_even = f_odd_to_even_ratio(harmonic_freq, harmonic_mag)
            moments = f_moments(swf)
            rolloff = f_rolloff(swf)
            decrease = f_decrease(swf)
            hfc = f_hfc(swf)
            flatness = f_flatness(swf)
            zero_crossing = f_zc(f)
            entropy = f_entropy(swf)

            pool.add(f'{input_name}.mfcc_coeffs', mfcc_coeffs)
            pool.add(f'{input_name}.mfcc_bands', mfcc_bands)
            pool.add(f'{input_name}.rms', rms)
            pool.add(f'{input_name}.spec_contrast', spec_contrast)
            pool.add(f'{input_name}.spec_valley', spec_valley)
            pool.add(f'{input_name}.spec_energy', spec_energy)
            pool.add(f'{input_name}.spec_crest', spec_crest)
            pool.add(f'{input_name}.spec_complexity', spec_complexity)
            pool.add(f'{input_name}.strong_peak', strong_peak)
            pool.add(f'{input_name}.flux', flux)
            pool.add(f'{input_name}.pitch', pitch)
            pool.add(f'{input_name}.pitch_confidence', pitch_confidence)
            pool.add(f'{input_name}.pitch_salience', pitch_salience)
            pool.add(f'{input_name}.dissonance', dissonance)
            pool.add(f'{input_name}.hpcp', hpcp)
            pool.add(f'{input_name}.hpcp_entropy', hpcp_entropy)
            pool.add(f'{input_name}.hpcp_crest', hpcp_crest)
            pool.add(f'{input_name}.tristumulus', tristimulus)
            pool.add(f'{input_name}.inharmonicity', inharmonicity)
            pool.add(f'{input_name}.odd_to_even', odd_to_even)
            pool.add(f'{input_name}.moments', moments)
            pool.add(f'{input_name}.rolloff', rolloff)
            pool.add(f'{input_name}.decrease', decrease)
            pool.add(f'{input_name}.hfc', hfc)
            pool.add(f'{input_name}.flatness', flatness)
            pool.add(f'{input_name}.zero_crossing', zero_crossing)
            pool.add(f'{input_name}.entropy', entropy)

        aggr_pool = PoolAggregator(defaultStats=stats)(pool)
        YamlOutput(filename=os.path.join(root, 'python_essentia_analysis', f'{input_name}.json'), format='json')(aggr_pool)

if __name__ == '__main__':
    # FrameCutter parameters
    frame_size = 4096
    hop_size = 1024
    frame_cutter = FrameCutter(frameSize=frame_size, hopSize=hop_size)
    w = Windowing(type='hann')
    stats = ['mean', 'stdev', 'median', 'mean', 'var', 'min',
            'max', 'skew', 'kurt', 'dmean', 'dvar', 'dmean2', 'dvar2']

    # Analysis functions
    f_spec = Spectrum()
    f_mfcc = MFCC(inputSize=frame_size)
    f_spec_contrast = SpectralContrast(frameSize=frame_size)
    f_spec_complexity = SpectralComplexity()
    f_yin = PitchYinFFT()
    f_pitch_salience = PitchSalience()
    f_norm_temporal_centroid = TCToTotal()
    f_strong_peak = StrongPeak()
    f_flux = Flux()
    f_flatness = FlatnessDB()
    f_rms = RMS()
    f_moments = CentralMoments()
    f_rolloff = RollOff()
    f_decrease = Decrease()
    f_hfc = HFC()
    f_zc = ZeroCrossingRate()
    f_energy = Energy()
    f_spec_peaks = SpectralPeaks(minFrequency=1)
    f_dissonance = Dissonance()
    f_entropy = Entropy()
    f_dance = Danceability()
    f_hpcp = HPCP()
    f_crest = Crest()
    f_amtbmer = AfterMaxToBeforeMaxEnergyRatio()
    f_envelope = Envelope()
    f_flatnessSFX = FlatnessSFX()
    f_log_attacktime = LogAttackTime()
    f_tristiumulus = Tristimulus()
    f_harm_peaks = HarmonicPeaks()
    f_inharmonicity = Inharmonicity()
    f_odd_to_even_ratio = OddToEvenHarmonicEnergyRatio()
    f_duration = Duration()
    f_effective_duration = EffectiveDuration()
    f_dynamic_complexity = DynamicComplexity()
    f_loudness = Loudness()

    to_analyse = os.listdir(unique_audio_folder)
    num_jobs = len(to_analyse)
    with mp.Pool() as workers:
        for i, _ in enumerate(
            workers.imap_unordered(descriptor_analyse, range(num_jobs))
            , 1):
            sys.stderr.write('\rdone {0:%}'.format(i/num_jobs))

