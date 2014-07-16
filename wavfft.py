import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from numpy import fft
fs, data = wavfile.read('Downloads/animals013.wav') # load the data
print fs, min(data),max(data)
print data.dtype
#a = data.T[0] # this is a two channel soundtrack, I get the first track
b=[(ele/2**8.)*2-1 for ele in data] # this is 8-bit track, b is now normalized on [-1,1)
b = data / (2.**7) -1
print b

c = fft.fft(b) # create a list of complex number
d = len(c)/2  # you only need half of the fft list
plt.plot(abs(c),'r') 
#plt.plot(abs(c[:(d-1)]),'r') 
plt.show()
