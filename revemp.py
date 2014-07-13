import numpy as np
import matplotlib.pyplot as plt

N = 17
data = np.random.random((N, 4))
#labels = ["ZNGA","GLUU","EA","ATVI","TTWO","COOL","FB","GOOG","YHOO","IGT","KNM","GA","ROVI","GAME","CYOU","PWRD","KONG"]
#NEmp = np.array([2034.,547.,9000.,6790.,2530.,62.,6820.,49830.,12200.,5000.,5540.,1500.,1220.,3130.,6110.,4800.,1120.])/1000.
#Earn = np.array([168.02,44.58,1123.00,1110,195.21,3.24,2502.00,15420.,1132.73,512.8,604.16,92.02,142.45,158.736,180.75,142.5712,48.95])
labels = ["KING","ZNGA","GLUU","EA","ATVI","TTWO","COOL","IGT","KNM","GA","ROVI","GAME","CYOU","PWRD"]
NEmp = np.array([665,2034.,547.,9000.,6790.,2530.,62.,5000.,5540.,1500.,1220.,3130.,6110.,4800.])
Earn = np.array([592.05, 168.02,44.58,1123.00,1110,195.21,3.24,512.8,604.16,92.02,142.45,158.736,180.75,142.5712])
ratio = Earn/NEmp
ratioS = (Earn/NEmp)*500
#plt.subplots_adjust(bottom = 0.1)
plt.plot([0,10000],[0,800],"--")
plt.scatter(
#    NEmp, Earn, marker = 'o', c = data[:, 2], s = ratio*10000,
    NEmp, Earn,  marker = 'o', c = Earn,s = ratioS,
    cmap = plt.get_cmap('Spectral'))
for label, x, y in zip(labels, NEmp, Earn):
    plt.annotate(
        label, 
        xy = (x, y), xytext = (10,4),
        textcoords = 'offset points', ha = 'right', va = 'bottom')
        #bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        #arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

#plt.scatter(NEmp,Earn)
plt.xlim(xmax=10000)
plt.xlim(xmin=-500)
plt.ylim(ymin=0)
plt.xlabel('Number of Employees')
plt.ylabel('Q1 2014 Revenue (Million Dollar)')
plt.show()
