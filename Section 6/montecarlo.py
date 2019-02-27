# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as npr
import pandas as pd
from scipy.stats import norm

class MonteCarlo:
    '''

Will calculate:
-------------------    
Parametric VaR deterministically given current value, volatility, 
time horizon (1 = one year) & confidence level - value between 0 and 1, 
typically .95 or higher
 
expected return effect will be negligible for short time horizons

-------------------
Parametric VaR Monte Carlo estimation given current value, 
expected return, volatility, time horizon (1 = one year), confidence level

-------------------
Expected portfolio ending value given present value, expected return, volatility,
time horizon and number of iterations.

It is recommended that the result be stored in a variable for analysis

'''    
    
    
    def quick_var(value, vol, T, CL):
        cutoff = norm.ppf(CL)
        return value * vol * np.sqrt(T) * cutoff
    
    def mc_VaR(pv, er, vol, T, iterations):
        end = pv * np.exp((er - .5 * vol ** 2) * T + 
                     vol * np.sqrt(T) * np.random.standard_normal(iterations))
        ending_values = end - pv
        return ending_values
    
    
    def monte_carlo_sim(pv, er, volatility, horizon, iterations):
        returns = np.zeros((iterations, horizon))
        for t in range(iterations):
            for year in range(horizon):
                returns[t][year] = npr.normal(er, volatility)
        
        portfolio = np.zeros((iterations,horizon))
        for iteration in range(iterations):
            starting = pv
            for year in range(horizon):
                ending = starting * (1 + returns[iteration,year])
                portfolio[iteration,year] = ending
                starting = ending
        return pd.DataFrame(portfolio).T