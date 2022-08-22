#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 17:38:15 2022

@author: abidahaque
"""


# is_match_B = combo.get_column(0).get_vector(base=1)
# is_match_A = combo.get_column(0).get_vector()

#    all_match = Matrix(N, 3, sint)
#    all_match.set_column(0, combo.get_column(0))
#    all_match.set_column(1, combo.get_column(1))
    
    
#    all_match.set_column(2,combo.get_column(2).get_vector(base=1) )

    

ind_match = dict()
a_dict = {vals0[a]:(a+1) for a in range(len(vals0))}

combo = np.concatenate((vals0,vals1))

combo.sort()

for i in range(15):
    if combo[i]==combo[i+1]:
        ind_match[combo[i]] = (a_dict[combo[i]])
        



# these should be the values of B
yy = np.array([0, 0, 0, 0, 0, 0, 17, 5, 26, 21, 0, 4, 20, 0, 30, 0, 28, 0, 29,
               0, 23, 0, 31, 19, 0, 32, 15, 0, 8, 3, 0, 0])


yy=yy[yy!=0]
yy.sort()

# these should be the matches, the dictionary elements
#although can 
zz = np.array([0, 0, 0, 0, 0, 0, 0, 5, 14, 0, 0, 4, 0, 0, 0, 0, 0, 0,
    16, 0, 12, 0, 0, 10, 0, 0, 0, 0, 0, 3, 0, 0])

zz = zz[zz!=0]
zz.sort()


all_vals = np.concatenate((vals0, vals1))
all_vals.sort()