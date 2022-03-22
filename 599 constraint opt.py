#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy.optimize import minimize


# In[2]:


# Data Processing

US_CPI=pd.read_csv('/Users/erinliang/Desktop/599/US_CPI.csv')
#stack years and months
US_CPI = pd.melt(US_CPI,id_vars=['YEAR'], var_name=['Month'])
US_CPI['date'] = pd.to_datetime(US_CPI['YEAR'].astype(str) + '-' + US_CPI['Month'].astype(str))
US_CPI = US_CPI.sort_values(by=['date']).drop(columns=['Month', 'YEAR']).reset_index(drop=['index'])
US_CPI = US_CPI.rename(columns={'value': 'US_CPI'})
US_CPI = US_CPI[['date', 'US_CPI']]


# In[3]:


# Data Processing

returns=pd.read_csv('/Users/erinliang/Desktop/599/599_data.csv')
#merge US CPI data and Indices return data into one dataframe
returns = pd.concat([US_CPI,returns], axis = 1)
#isolate inflation periods 
returns = returns[returns.US_CPI > 0.035]
returns = returns.drop(['Date','US_CPI'],1)
returns.set_index('date', inplace=True)


# In[4]:


# Main Code - Constraint Optimization 

times = 5000
#objective function
def obj_fx(weights,sample_returns): 
    exp_returns = sample_returns.dot(weights) #times*1
    #checked:opt_weights@t * sample_returns@t
    port_return = np.mean(exp_returns) #1*1
    risk = sum(n < 0 for n in exp_returns)/len(exp_returns) 
    return port_return, risk, port_return/risk

sample_returns = pd.DataFrame([])
for k in range(times):
    y = returns.sample(n=12) #12*14
    avg = np.mean(y) 
    sample_returns=sample_returns.append(avg,ignore_index=True) #times*14

#set initial weights equal 
initial_weights = [1./returns.shape[1] for x in range(returns.shape[1])]

#weights are between 0 and 1
bounds = tuple((0,1) for x in range(returns.shape[1]))

#weights sum to one and portfolio risk < 
constraints=({"type":"eq", "fun": lambda x: np.sum(x)-1})
             #,{"type": "ineq", "fun": lambda x: 0.05-obj_fx(x,sample_returns)[1]})
      
#minimize -return/risk subject to the constraints 
optimized_results = minimize(lambda x: -obj_fx(x,sample_returns)[2], initial_weights
                             ,method='SLSQP', bounds=bounds, constraints=constraints)
optimized_results


# In[5]:


print("Return:",obj_fx(optimized_results.x,sample_returns)[0]) #checked
print("Risk:",obj_fx(optimized_results.x,sample_returns)[1])


# In[6]:


# To generate chart below
pd.DataFrame(list(zip(list(sample_returns.columns), optimized_results.x)), columns=['Index', 'Weight'])

