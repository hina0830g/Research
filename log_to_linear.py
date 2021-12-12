# -*- coding: utf-8 -*-
"""
Created on Wed May 26 16:23:55 2021

@author: Hina Goto
"""
# Taking out the log10 and converts them into 
# linear scale including the upper and lower limits of 
# uncertainty 
import numpy as np
#=====input value and uncertainty====#
a = -0.08 # lower uncertainty 
b = 0.07 # upper uncertainty
c = -0.5 # Value
#====================================#
Bot = 10**(a+c)# Evaluates lower error in linear scale
Up = 10**(b+c) # Evaluates upper error in linear scale
val = 10**(c) # Evaluates values in linear scale
error1 = Up-val
error2 = Bot-val

print('upper',  '{:.3f}'.format(Up))
print('actual value: ',  '{:.3f}'.format(val))
print('lower:',  '{:.3f}'.format(Bot))
print('value is: ',  '{:.3f}'.format(val), '+' + '{:.3f}'.format(error1), 'or', '{:.3f}'.format(error2))
