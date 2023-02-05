import matplotlib.pyplot as plt
import numpy as np

# Assume the following:
# Strike price of ITM put: 90
# Strike price of OTM put: 110
# Stock price at expiration: 100

s_itm = 90
s_otm = 110

# Create the x-axis (stock prices)
x = np.linspace(0, 200, 100)

# Create the y-axis (payoffs) for ITM put
y1 = np.maximum(s_itm - x, 0)

# Create the y-axis (payoffs) for OTM put
y2 = np.maximum(x - s_otm, 0)

# Create the figure and subplots
fig, axs = plt.subplots(1, 2)

x_itm = np.array([0,s_itm,200])
y_itm = np.array([s_itm,0,0])
x_otm = np.array([0,s_otm,200])
y_otm = np.array([0,0,200-s_otm])

# Plot the ITM put payoff in the first subplot
axs[0].plot(x, y1)
axs[0].set_title("ITM Put")
axs[0].set_xlabel("Stock Price at Expiration")
axs[0].set_ylabel("Payoff")
axs[0].scatter(x_itm,y_itm)
axs[0].text(0,s_itm,'(0,S_ITM)')
axs[0].text(s_itm,0,'(S_ITM,0)')
axs[0].text(200,0,'(200,0)', horizontalalignment='right')
axs[0].grid()

# Plot the OTM put payoff in the second subplot
axs[1].plot(x, y2)
axs[1].set_title("OTM Put")
axs[1].set_xlabel("Stock Price at Expiration")
axs[1].set_ylabel("Payoff")
axs[1].scatter(x_otm,y_otm)
axs[1].text(0,0,'(0,0)')
axs[1].text(s_otm,0,'(S_OTM,0)')
axs[1].text(200,200-s_otm,'(200,200-S_OTM)', horizontalalignment='right')
axs[1].grid()


# Show the plot
plt.show()