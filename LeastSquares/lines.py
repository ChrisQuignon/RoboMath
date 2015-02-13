import IPython.core.display
import sys

s1 = load('shape001.npy')
#print s1.shape

s2 = load('shape0001.npy')
#print s2.shape

s3 = load('shape002.npy')
#print s3.shape

s4 = load('shape003.npy')
#print s4.shape

plot(s1[:,0], s1[:, 1], 'o')
#show()

a, b, c, d = s2
plot(a[:,0], a[:, 1], 'o')
plot(b[:,0], b[:, 1], 'o')
plot(c[:,0], c[:, 1], 'o')
plot(d[:,0], d[:, 1], 'o')
#show()

a, b = s3
plot(a[:,0], a[:, 1], 'o')
plot(b[:,0], b[:, 1], 'o')
#show()

a, b = s4
plot(a[:,0], a[:, 1], 'o')
plot(b[:,0], b[:, 1], 'o')
#show()
