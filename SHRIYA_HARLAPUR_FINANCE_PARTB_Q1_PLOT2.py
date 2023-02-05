import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array([0,6,7,8,14])
putoption = np.array([6,0,-1,-1,-1])
calloption = np.array([-1,-1,-1,0,6])

plt.subplot(1,2,1)
plt.plot(xpoints,putoption)
plt.title("Put Option Payoff Payoff vs Stock Price")
plt.xlabel("Stock Price")
plt.ylabel("Put Option Payoff")
plt.text(0,6,'(0,S-P)')
plt.text(6,0,'(S-P,0)', horizontalalignment='right')
plt.text(7,-1,'(S,-P)', horizontalalignment='right')
plt.grid()

plt.subplot(1,2,2)
plt.plot(xpoints,calloption)
plt.title("Call Option Payoff Payoff vs Stock Price")
plt.xlabel("Stock Price")
plt.ylabel("Call Option Payoff")
plt.text(0,-1,'(0,-P)')
plt.text(7,-1,'(S,-P)', horizontalalignment='right')
plt.text(8,0,'(P+S,0)', horizontalalignment='right')
plt.text(14,6,'(2S,S-P)', horizontalalignment='right')
plt.grid()

plt.suptitle("Put Option vs Call Option")
plt.show()
