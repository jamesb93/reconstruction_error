sfm      = __import__('3_sfm')
loudness = __import__('4_loudness')
mfcc     = __import__('6_mfccs')
import time

start = time.time()
print('Starting Spectral Flatness Measure analysis.')
sfm.main()

print('Starting Loudness analysis.')
loudness.main()

print('Starting MFCC analysis.')
mfcc.main()

end = time.time()
time_taken = round(((start-end) / 60.), 2)
print(f'All analysis took: {time_taken} minutes.')

