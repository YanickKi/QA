import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(1e-3, 2, 500)

plt.figure()

plt.plot(x, 3/np.log(1+x), color = 'deeppink')
plt.plot(x, 3/np.sqrt(x), color = 'grey')
plt.plot(x, 3/x, color = 'grey')
plt.ylim(1, 30)
plt.xticks([],[])
plt.yticks([],[])
plt.savefig('ln.pdf', bbox_inches = 'tight')

plt.figure()

plt.plot(x, 3/np.log(1+x), color = 'grey')
plt.plot(x, 3/np.sqrt(x), color = 'deeppink')
plt.plot(x, 3/x, color = 'grey')
plt.ylim(1, 30)
plt.xticks([],[])
plt.yticks([],[])
plt.savefig('sqrt.pdf', bbox_inches = 'tight')

plt.figure()

plt.plot(x, 3/np.log(1+x), color = 'grey')
plt.plot(x, 3/np.sqrt(x), color = 'grey')
plt.plot(x, 3/x, color = 'deeppink')
plt.ylim(1, 30)
plt.xticks()
plt.xticks([],[])
plt.yticks([],[])
plt.savefig('t.pdf', bbox_inches = 'tight')