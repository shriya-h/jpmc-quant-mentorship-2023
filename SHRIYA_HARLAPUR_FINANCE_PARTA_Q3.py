import matplotlib.pyplot as plt
import numpy as np

# Define the parameters for the trade
s = np.linspace(0, 2000, num=1000)  # Stock price at expiration
k = 1000  # Strike price of put option
c = 100  # Premium paid for the put option
f = 1000  # Futures price

# Define the payoffs for the put option and the short futures contract
payoffs_put_option = np.maximum(k - s, 0) - c
payoffs_short_futures = f - s

# Plot the payoffs
plt.figure()
plt.plot(s, payoffs_put_option, label='Put Option', color='orange')
plt.plot(s, payoffs_short_futures, label='Short Futures', color='blue')
plt.xlabel('Stock Price at Expiration')
plt.ylabel('Payoff')
plt.title('Payoff Diagram')
plt.grid()
plt.legend()

# Mark the strike, premium, and futures price on the graph
plt.axvline(x=k, linestyle='--', color='black', label='Strike')
plt.axvline(x=f, linestyle=':', color='black', label='Futures Price')
plt.axhline(y=-c, linestyle='-.', color='black', label='Premium')
plt.axvspan(0,1100, alpha=0.5, color='lightblue')
plt.axvspan(1100,2000, alpha=0.5, color='orange')
plt.legend()
plt.show()