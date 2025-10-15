import numpy as np
import matplotlib.pyplot as plt 


h = 10.0 ** (-np.arange(1, 17))
dfdx = np.zeros(len(h))
error = np.zeros(len(h))
for i in range(len(h)):
    dfdx[i] = (np.sin(1+h[i]) - np.sin(1))/h[i]
    error[i] = np.abs(dfdx[i] - np.cos(1))

plt.loglog(h, error, 'o-', label='Błąd numeryczny')
plt.xlabel('h')
plt.ylabel('Błąd bezwzględny')
plt.title('Błąd różniczkowania w zależności od h')
plt.grid(True, which='both', ls='--', alpha=0.5)
plt.legend()
#plt.gca().invert_xaxis()
plt.tight_layout()
plt.show()