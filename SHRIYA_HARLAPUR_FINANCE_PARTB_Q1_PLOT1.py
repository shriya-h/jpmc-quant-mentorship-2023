import matplotlib.pyplot as plt
import numpy as np

def plot_payoffs(s, k, c, p):
    # Define the payoffs for each leg of the trade
    payoffs_long_call = np.maximum(s - k, 0) - c
    payoffs_long_put = np.maximum(k - s, 0) - p

    # Total payoff for the trade
    payoffs = payoffs_long_call + payoffs_long_put

    important_points_x = np.array([0,k-(c+p),k,k+c+p,2*k])
    important_points_y = np.array([k-(c+p),0,-(c+p),0,k-(c+p)])

    # Plot the payoffs
    plt.figure()
    plt.plot(s, payoffs)
    plt.scatter(important_points_x, important_points_y)
    plt.xlabel('Stock Price at Expiration')
    plt.ylabel('Payoff')
    plt.title('Payoff Diagram')
    plt.text(0,k-(c+p),'(0,S-2P)')
    plt.text(k-(c+p),0,'(S-2P,0)', horizontalalignment='right')
    plt.text(k,-(c+p),'(S,-2P)')
    plt.text(k+c+p,0,'(S+2P,0)')
    plt.text(2*k,k-(c+p),'(2S,S-2P)',horizontalalignment='right')  
    plt.grid()
    plt.show()
    
    
# Define the parameters for the trade
s = np.linspace(0, 200, num=1000)  # Stock price at expiration
k = 100  # Strike price of call and put options
c = 10  # Premium paid for the call option
p = 10  # Premium paid for the put option

# Plot the payoffs
plot_payoffs(s, k, c, p)