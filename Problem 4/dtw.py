"""
our full code implementation can be seen here 
https://nbviewer.jupyter.org/github/chairielazizi/WIA2005-algorithm-group-project/blob/main/Problem%204/dtw_final.ipynb
"""
import wave
import numpy as np

#this audio says "memohon maaf"
jnt = wave.open("jnt-memohonmaaf.wav", "r")
jnt_soundwave = jnt.readframes(-1)

jnt_slow = wave.open("jnt-memohonmaaf-slowed.wav", "r")
jnt_soundwave_slow = jnt_slow.readframes(-1)

jnt_fast = wave.open("jnt-memohonmaaf-1.5.wav", "r")
jnt_soundwave_fast = jnt_fast.readframes(-1)

#---------------------------------------------------------------
#this audio says "citylink express"
citylink = wave.open("citylink.wav", "r")
citylink_soundwave = citylink.readframes(-1)

citylink_slow = wave.open("citylink-slowed.wav", "r")
citylink_soundwave_slow = citylink_slow.readframes(-1)

# this is to show just how big the array is 
jnt_signal_maaf = np.frombuffer(jnt_soundwave, dtype='int16')
# print(jnt_signal[:10])
jnt_signal_maaf_slow = np.frombuffer(jnt_soundwave_slow, dtype='int16')


# jnt_framerate = jnt.getframerate() #frame rate
# print(jnt_framerate)

def dtw(s, t):
    n, m = len(s), len(t)
    dtw_matrix = np.zeros((n+1, m+1))
    for i in range(n+1):
        for j in range(m+1):
            dtw_matrix[i, j] = np.inf
    dtw_matrix[0, 0] = 0
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = abs(s[i-1] - t[j-1])
            # take last min from a square box
            last_min = np.min([dtw_matrix[i-1, j], dtw_matrix[i, j-1], dtw_matrix[i-1, j-1]])
            dtw_matrix[i, j] = cost + last_min
    return dtw_matrix

print("\nmemohon maaf vs memohon maaf (slowed):")
print(dtw(jnt_soundwave[:10], jnt_soundwave_slow[:10]))

print("\n\ncitylink express vs citylink express (slowed):")
print(dtw(citylink_soundwave[:10], citylink_soundwave_slow[:10]))

print("\n\nmemohon maaf vs citylink express:")
print(dtw(jnt_soundwave[:10], citylink_soundwave[:10]))

from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

# distance1, path1 = fastdtw(jnt2_soundwave, jnt2_soundwave_slow, dist=euclidean)
distance1, path1 = fastdtw(jnt_signal_maaf, jnt_signal_maaf_slow, dist=euclidean)
print(distance1)
print(path1)

# print(jnt2_soundwave[:10])