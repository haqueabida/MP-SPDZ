#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 16:20:54 2022

@author: abidahaque

Saves the permutation from an odd-even merge (functions copied from library)
Can apply the permutation and create the inverse permutation.

This is a scratch file practicing how permutations work in Python; not yet
ready for MP-SPDZ.

"""

def oempartner(n,l,p):
		if (p == 1):
				return n ^ (1 << (l - 1))
		else:
				(scale, box) = (1 << (l - p), 1 << p)
				sn = n // scale - (((n // scale) // box) * box)
				if (sn == 0 or (sn == box - 1)):
						return n
				else:
						if (sn % 2 == 0):
								return n - scale
						else:
								return n + scale
						
def oemcomps_iter(n):
		'''
		Parameters
		----------
		n : length of array (must be power of 2)

		Returns
		-------
		sp: a list of pairs of what needs to get compared.

		'''

		l = n.bit_length()-1

		 
		sp = []

		for p in range(1, l+1):
				for node in range(0,n):		
						s = oempartner(node,l,p)
						if node<s:
								sp.append((node, s))
		return sp


def apply_perm_simple(arr, perm):
    '''

    Parameters
    ----------
    arr : a list
    perm : a list (assume Cauchy notation)
    
    Applies the permutation perm to arr

    Returns
    -------
    result : permuted list of perm(arr).

    '''
    n = len(arr)
    result = np.empty(n, dtype=object)
    for i in range(n):
        result[i] = arr[perm[i]]
    return result


def inversePermutation(arr) :
 
		# To store element to index mappings
		size = len(arr)
		arr2 = [0] *(size)
		 
		# Inserting position at their
		# respective element in second array
		for i in range(0, size) :
				arr2[arr[i]] = i 

		return arr2
				
				

import numpy as np

### saving the permutation
n=16


pset0 = np.random.permutation(n)[0:n//2]+1
pset1 = np.random.permutation(n)[0:n//2]+1

pset0.sort()
pset1.sort()

pset = np.concatenate((pset0, pset1))

tups = np.array(oemcomps_iter(n))


didswap = []
for i,j in tups:
		if (pset[i]>pset[j]):
				pset[i], pset[j] = pset[j], pset[i]
				didswap.append(1)
		else:
				didswap.append(0)

didswap = np.array(didswap)

swaptuples = tups[didswap==1]

myperm = [i for i in range(n)]

for k,l in swaptuples:
		temp1 = myperm[k]
		myperm[k] = myperm[l]
		myperm[l] = temp1
		
		


#get back the original pset
pset = np.concatenate((pset0, pset1))
result = apply_perm_simple(pset, myperm)