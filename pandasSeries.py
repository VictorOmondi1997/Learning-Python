# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 09:53:35 2019

@author: Victor Omondi
"""
import pandas as pd
s2 = pd.Series([10,29,34,843])
print(s2)


#Pd String
names = pd.Series(['Victor', 'Leucrecia', 'Shirley', 'James'], index=['V', 'L', 'S', 'J'])
print(names)

#Passing A Dictonary
names2 = pd.Series({'V':'Victor', 'L':'Leucrecia', 'S':'Shirley'})
print(names2)
