import matplotlib.pyplot as plt
import numpy as np

# Define the parameters for the trade
s = np.linspace(0, 200, num=1000)  # Stock price at expiration
k_itm = 100  # Strike price of the ITM call option
k_otm = 130  # Strike price of the OTM call option
k_atm1 = 110  # Strike price of the ATM call option 1
k_atm2 = 120  # Strike price of the ATM call option

# Define the payoffs for the options
payoff_itm_call = np.maximum(s - k_itm, 0)
payoff_otm_call = np.maximum(s - k_otm, 0)
payoff_atm1_call = -np.maximum(s - k_atm1, 0)
payoff_atm2_call = -np.maximum(s - k_atm2, 0)

x_itm = np.array([0,k_itm,200])
y_itm = np.array([0,0,200-k_itm])
x_otm = np.array([0,k_otm,200])
y_otm = np.array([0,0,200-k_otm])
x_atm1 = np.array([0,k_atm1,200])
y_atm1 = np.array([0,0,k_atm1-200])
x_atm2 = np.array([0,k_atm2,200])
y_atm2 = np.array([0,0,k_atm2-200])

# Plot the payoffs
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0, 0].plot(s, payoff_itm_call, label='ITM Call Option')
axs[0, 0].set_xlabel('Stock Price at Expiration')
axs[0, 0].set_ylabel('Payoff')
axs[0, 0].set_title('ITM Call Option')
axs[0, 0].scatter(x_itm,y_itm)
axs[0, 0].text(0,0,'(0,0)')
axs[0, 0].text(k_itm,0,'(S_ITM,0)')
axs[0, 0].text(200,200-k_itm,'(200,200-S_ITM)', horizontalalignment='right')
axs[0, 0].grid()
axs[0, 0].legend()

axs[0, 1].plot(s, payoff_otm_call, label='OTM Call Option')
axs[0, 1].set_xlabel('Stock Price at Expiration')
axs[0, 1].set_ylabel('Payoff')
axs[0, 1].set_title('OTM Call Option')
axs[0, 1].scatter(x_otm,y_otm)
axs[0, 1].text(0,0,'(0,0)')
axs[0, 1].text(k_otm,0,'(S_OTM,0)')
axs[0, 1].text(200,200-k_otm,'(200,200-S_OTM)', horizontalalignment='right')
axs[0, 1].grid()
axs[0, 1].legend()

axs[1, 0].plot(s, payoff_atm1_call, label='Short ATM Call Option 1')
axs[1, 0].set_xlabel('Stock Price at Expiration')
axs[1, 0].set_ylabel('Payoff')
axs[1, 0].set_title('Short ATM Call Option 1')
axs[1, 0].scatter(x_atm1,y_atm1)
axs[1, 0].text(0,0,'(0,0)')
axs[1, 0].text(k_atm1,0,'(S_ATM1,0)')
axs[1, 0].text(200,k_atm1-200,'(200,S_ATM1-200)', horizontalalignment='right')
axs[1, 0].grid()
axs[1, 0].legend()

axs[1, 1].plot(s, payoff_atm2_call, label='Short ATM Call Option 2')
axs[1, 1].set_xlabel('Stock Price at Expiration')
axs[1, 1].set_ylabel('Payoff')
axs[1, 1].set_title('Short ATM Call Option 2')
axs[1, 1].scatter(x_atm2,y_atm2)
axs[1, 1].text(0,0,'(0,0)')
axs[1, 1].text(k_atm2,0,'(S_ATM2,0)')
axs[1, 1].text(200,k_atm2-200,'(200,S_ATM2-200)', horizontalalignment='right')
axs[1, 1].grid()
axs[1, 1].legend()

plt.show()

x_strat = np.array([k_itm,k_atm1,k_atm2,k_otm])
y_strat = np.array([0,k_atm1-k_itm,k_otm-k_atm2,0])

plt.plot(s, payoff_itm_call + payoff_otm_call + payoff_atm1_call + payoff_atm2_call, label='Strategy')
plt.xlabel('Stock Price at Expiration')
plt.ylabel('Payoff')
plt.title('Strategy')
plt.scatter(x_strat,y_strat)
plt.text(k_itm,0,'(S_ITM,0)', horizontalalignment='right')
plt.text(k_atm1,k_atm1-k_itm,'(S_ATM1,S_ATM1-S_ITM)', horizontalalignment='right')
plt.text(k_atm2,k_otm-k_atm2,'(S_ATM2,S_OTM-S_ATM2)')
plt.text(k_otm,0,'(S_OTM,0)')
plt.grid()
plt.legend()
plt.show()
