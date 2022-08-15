from random import Random
import math

#import sys
#from Test.core import *
if '_Array' not in dir():
    from Compiler.types import *
    from Compiler.types import _secret
    from Compiler.library import *
    from Compiler.program import Program
    _Array = Array


def normal_comparator(x, y):
    return x < y

def cond_swap_bit(x,y, b):
    """ swap if b == 1 """
    if isinstance(x, list):
        t = [(xi - yi) * b for xi,yi in zip(x, y)]
        return [xi - ti for xi,ti in zip(x, t)], \
            [yi + ti for yi,ti in zip(y, t)]
    else:
        t = (x - y) * b
        return x - t, y + t


def bitoniciter(arr, n_threads=None): 
    '''
    Parameters
    ----------
    arr : an array
    
    Does a non-recursive bitonic sort
    Returns
    -------
    arr: sorted list
    '''
    n = len(arr)
    numofbits= n.bit_length()
    
    @for_range(1, numofbits)
    def _(x):
        k = 2**x
        @for_range(x)
        def _(r): 
            j = 2**r
            @for_range(n)
            def _(i):
                l = i^j #bitwise XOR
                if (l>i):
                    if ((i&k) ==0) and (arr[i] > arr[l]) or ((i&k)!=0 and (arr[i] < arr[l])):
                        arr[i], arr[l] = arr[l], arr[i]


def bitoniccomps(n):
    '''
    

    Parameters
    ----------
    n : length (a power of 2)
    
    Checks the indices to see if the XOR is off by the right amount
    This yields the pairs we will eventually want to compare for bitonic merge
    (in order)

    Returns
    -------
    comp_tuples : a list of tuples

    '''
    numofbits = n.bit_length()-1
    comp_tuples = []

    powof2 = list(map(lambda x: 2**x, range(numofbits)))
    
    for k in powof2[::-1]:
        for i in range(n-1):
            for j in range(i+1, n):
                if i^j == k:
                    comp_tuples.append((i,j))

    return comp_tuples

            
def bitoniccomps_uneven(n,m):
    '''
    

    Parameters
    ----------
    n : length of first array (n<m)
    m : length of the second array
    rule that n+m is a power of 2
    
    THIS DOESN'T WORK YET!
    Returns
    -------
    comp_tuples : a list of tuples

    '''
    #kind of like picking medians
    my_diff = m//n
    
    comp_tuples = []
    
    for  s in range(my_diff):
        comp_tuples +=bitoniccomps(n+s*my_diff)

    return comp_tuples



def bitsortcomps(n):
    p = (n).bit_length()-1
    return (n/2)*(p *(p+1)/2)

# Python program for Bitonic Sort.
# works only when size of input is a power of 2.
 
# The parameter dir indicates the sorting direction, ASCENDING
# or DESCENDING; if (a[i] > a[j]) agrees with the direction,
# then a[i] and a[j] are interchanged.*/
def compAndSwap(a, i, j, dire):
    if (dire==1 and normal_comparator(a[j], a[i])) or (dire==0 and
            normal_comparator(a[i],  a[j])):
        a[i],a[j] = a[j],a[i]
 
# It recursively sorts a bitonic sequence in ascending order,
# if dir = 1, and in descending order otherwise (means dir=0).
# The sequence to be sorted starts at index position low,
# the parameter cnt is the number of elements to be sorted.
def bitonicMerge(a, low, cnt, dire):
    if cnt > 1:
        k = cnt//2
        for i in range(low , low+k):
            compAndSwap(a, i, i+k, dire)
        bitonicMerge(a, low, k, dire)
        bitonicMerge(a, low+k, k, dire)
 
# This function first produces a bitonic sequence by recursively
# sorting its two halves in opposite sorting orders, and then
# calls bitonicMerge to make them in the same order
def bitonicSort(a, low, cnt,dire):
    if cnt > 1:
          k = cnt//2
          bitonicSort(a, low, k, 1)
          bitonicSort(a, low+k, k, 0)
          bitonicMerge(a, low, cnt, dire)
