# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:54:48 2020

@author: smika
@purpose:
    This file contrasts list and generator approaches with iterative and memoised-recursion, using fibonachi numbers, comparing memory and time to perform.
"""

#here is the terms to generate in the trials
terms = 10_000
print("Terms to generate: {}".format(terms))

from functools import lru_cache

@lru_cache()
def fibonachi_memoise_recursive(index):
    """Memoised Recursive Function for generating a specified Fibonachi Number, given by the parameter."""
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonachi_memoise_recursive(index-1) + fibonachi_memoise_recursive(index-2)


def fibonachi_recursive(index):
    """Recursive Function for generating a specified Fibonachi Number, given by the parameter."""
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonachi_memoise_recursive(index-1) + fibonachi_memoise_recursive(index-2)


def fibonachi_iterative(index):
    """Iterative Function for generating a specified Fibonachi Number, given by the parameter."""
    a, b = 0, 1
    for _ in range(0,index):
        a, b = b, a + b
    return a


def fibonachi_iterative_list(index):
    """Iterative Function for generating a list of Fibonachi Numbers of length given by the parameter."""
    fib = []
    a, b = 0, 1
    for _ in range(0,index):
        fib.append(a)
        a, b = b, a + b
    return fib


def analyse_time_memory_of_list_sumation(function):
    """This takes a function that returns a list of summable items, and analyizes the time and memory to get the list and sum them all."""
    import memory_profiler
    import time
    
    def analyse(*args, **kwargs):
        
        timeA = time.time()  
        
        mem = memory_profiler.memory_usage()
        
        #run the function
        lst = function(*args, **kwargs)
        
        mem2 = memory_profiler.memory_usage()
        
        timeB = time.time() 
    
        total = 0
        for t in lst:
            total += t
        
        timeC = time.time() 
        
        time_create = timeB-timeA 
        time_total = timeC-timeA
        print( 'Memory (Before): {} Mb'.format(mem) )
        print( 'Memory (After): {} Mb'.format(mem2) )
        print( 'Memory (Difference): {} Mb'.format(  str( abs( mem2[0] - mem[0] ) ) ) )
        print(   'Time to create {} fibonachi numbers: {} Seconds'.format( terms, time_create  )    )
        print(   'Time to add {} fibonachi numbers: {} Seconds'.format( terms, time_total - time_create  )    )
        print(   'Time to create and add {} fibonachi numbers: {} Seconds'.format( terms, time_total  )    )
        
        return lst
    return analyse
    


@analyse_time_memory_of_list_sumation
def test_recursive_generator(terms):
    
    print("\n\nRecursive & Generator")    
    
    fib = (fibonachi_recursive(x) for x in range(terms))
    
    return fib

@analyse_time_memory_of_list_sumation
def test_recursive_list(terms):
    
    print("\n\nRecursive & List")
    
    fib = [fibonachi_recursive(x) for x in range(terms)]
    
    return fib

@analyse_time_memory_of_list_sumation
def test_memoise_recursive_generator(terms):
    
    print("\n\nRecursive w/ Memoise & Generator")    
    
    fib = (fibonachi_memoise_recursive(x) for x in range(terms))
    
    return fib

@analyse_time_memory_of_list_sumation
def test_memoise_recursive_list(terms):
    
    print("\n\nRecursive w/ Memoise & List")
    
    fib = [fibonachi_memoise_recursive(x) for x in range(terms)] 
    
    return fib


@analyse_time_memory_of_list_sumation
def test_iterative_list(terms):
    
    print("\n\nIterative list w/ Generator")
    
    fib = fibonachi_iterative_list(terms)
    
    return fib


@analyse_time_memory_of_list_sumation
def test_iterative_each_generator(terms):
    
    print("\n\nIterative each value w/ Generator")
    
    fib = (fibonachi_iterative(x) for x in range(terms))
    
    return fib

@analyse_time_memory_of_list_sumation
def test_iterative_each_list(terms):
    print("\n\nIterative each value w/ List")    
    
    fib = [fibonachi_iterative(x) for x in range(terms)]
    
    return fib



#tests:
test_recursive_generator(terms)
test_recursive_list(terms)
test_memoise_recursive_generator(terms)
test_memoise_recursive_list(terms)
test_iterative_list(terms)
test_iterative_each_list(terms)
test_iterative_each_generator(terms)
