#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 13:36:23 2018

@author: Felipe Rafael de Souza
"""

import matplotlib.pyplot as plt

def start_market(state_market, number_of_companies):
    states = {'high' : 1000, 'low' : 2000, 'stagnant': 1000}
    #states[state_market] = number_of_companies
    return states

def update_market(states):
    states['high'] = states['high']*0.9 + states['low']*0.15 + states['stagnant']*0.25
    states['low'] = states['low']*0.8 + states['high']*0.075 + states['stagnant']*0.25
    states['stagnant'] = states['stagnant']*0.5 + states['high']*0.025 + states['low']*0.05
    return states


times = 1000
companies = 4000
states = start_market('high', companies)

state_in_time = {'high' : [], 'low' : [], 'stagnant': []}

for time in range(times):
    state_in_time['high'].append(states['high'])
    state_in_time['low'].append(states['low'])
    state_in_time['stagnant'].append(states['stagnant'])
    states = update_market(states)

plt.plot(state_in_time['high'])
plt.plot(state_in_time['low'])
plt.plot(state_in_time['stagnant'])
plt.show()