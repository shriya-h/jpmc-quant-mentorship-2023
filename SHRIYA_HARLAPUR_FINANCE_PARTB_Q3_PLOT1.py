import matplotlib.pyplot as plt
import numpy as np

def plot_payoffs(s, k1, k2):
    # Define the payoffs for each leg of the trade
    payoffs_long_itm_put = np.maximum(k1 - s, 0)
    payoffs_short_otm_put = -np.maximum(k2 - s, 0)

    # Total payoff for the trade
    payoff = payoffs_long_itm_put + payoffs_short_otm_put

    x = np.array([0,k2,k1,200])
    y = np.array([k1-k2,k1-k2,0,0])

    # Plot the payoffs
    plt.figure()
    plt.plot(s, payoff)
    plt.xlabel('Stock Price at Expiration')
    plt.ylabel('Payoff')
    plt.title('Payoff Diagram')
    plt.scatter(x,y)
    plt.text(0,k1-k2,'(0,S_ITM-S_OTM)')
    plt.text(k2,k1-k2,'(S_OTM,S_ITM-S_OTM)')
    plt.text(k1,0,'(S_ITM,0)', horizontalalignment='right')
    plt.text(200,0,'(200,0)', horizontalalignment='right')
    plt.grid()
    plt.show()
    
    
# Define the parameters for the trade
s = np.linspace(0, 200, num=1000)  # Stock price at expiration
k1 = 110  # Strike price of ITM put option
k2 = 90  # Strike price of OTM put option

# Plot the payoffs
plot_payoffs(s, k1, k2)