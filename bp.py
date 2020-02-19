from scipy import signal
import matplotlib.pyplot as plt
#defining the transfer function which is 1/((s+1)**2)*(s+2)
sys = signal.TransferFunction([1], [1, 5, 6])
w, mag, phase = signal.bode(sys)

plt.figure()
plt.title('Bode magnitude plot')
plt.semilogx(w, mag)    # Bode magnitude plot
plt.figure()
plt.title('Bode phase plot')
plt.semilogx(w, phase)  # Bode phase plot
plt.show()