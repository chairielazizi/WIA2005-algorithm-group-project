"""
our full code implementation can be seen here 
https://nbviewer.jupyter.org/github/chairielazizi/WIA2005-algorithm-group-project/blob/main/Problem%204/dtw_final.ipynb
"""
import numpy as np
# DWT algorithm
def dtw1(fast, normal):
    fast_len = len(fast)
    normal_len = len(normal)
    dtw_matrix = np.zeros((fast_len+1,normal_len+1))
    
    for i in range(fast_len+1):
        for j in range(normal_len+1):
            dtw_matrix[i, j] = np.inf
    dtw_matrix[0,0] = 0
    
    for i in range(1, fast_len+1):
        for j in range(1, normal_len+1):
            cost = abs(fast[i-1] - normal[j-1])
            
            last_min = np.min([dtw_matrix[i-1,j], dtw_matrix[i,j-1],dtw_matrix[i-1, j-1]])
            dtw_matrix[i, j] = cost + last_min
    return dtw_matrix

#with windows
#untuk hadkan matching of the value
#for example when window=3,dia match tiga value je bila one to many tu
def dtw2(fast,normal,window):
        fast_len = len(fast)
        normal_len = len(normal)
        w = np.max([window, abs(fast_len - normal_len)])
        dtw_matrix = np.zeros((fast_len+1,normal_len+1))

        for i in range(fast_len+1):
            for j in range(normal_len+1):
                dtw_matrix[i,j] = np.inf
        dtw_matrix[0,0] = 0

        for i in range(1, fast_len+1):
            for j in range(np.max([1,i-w]),np.min([normal_len,i+w])+1):
                dtw_matrix[i,j] = 0

        for i in range(1,fast_len+1):
            for j in range(np.max([1,i-w]),np.min([normal_len,i+w])+1):
                cost = abs(fast[i-1] - normal[j-1])
                
                last_min = np.min([dtw_matrix[i-1,j], dtw_matrix[i,j-1],dtw_matrix[i-1, j-1]])
                dtw_matrix[i, j] = cost + last_min
        return dtw_matrix


# fast_audio = [1.3,2.4,3.6]
# normal_audio = [2.4,2.4,2.4,3.6,4.1]



import librosa
audio_data1 = 'jnt-memohonmaaf.wav'
x , sampling_rate = librosa.load(audio_data1)
print(type(x), type(sampling_rate))
print(x.shape, sampling_rate)

# import librosa
audio_data2 = 'jnt-memohonmaaf-1.5.wav'
y , sampling_rate = librosa.load(audio_data2)
print(type(y), type(sampling_rate))
print(y.shape, sampling_rate)

# to get convert from numpy array to list
fast_audio = y.tolist()
normal_audio = x.tolist()

#using dtw library
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

# distance, path = fastdtw(x, y, dist=euclidean)
distance, path = fastdtw(fast_audio, normal_audio, dist=euclidean)

print("The distance between them is: "+ str(distance) +"\n")
print("The matched path are:")
print(path)
