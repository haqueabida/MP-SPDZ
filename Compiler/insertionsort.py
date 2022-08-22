#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 09:01:44 2022

@author: nianer

(taken from the GitHub repo
 
 )

mistake: You cannot use and in connection with run-time variables. Use x.bit_and(y) instead.

"""

def insertsort(a, low, high):
    @for_range(low,high)
    def _(i):
        j = i
        @while_do(j > 0 and sint.less_than(a[j],a[j-1]).reveal())
        def _():
            sint(1).cond_swap(a[j],a[j-1])
            j = j-1

a = Array(10,sint)
a.assign([45,65,1,47,11,54,154,254,96,47])
insertsort(a,0,10)
print_ln("a = %s",a.reveal())