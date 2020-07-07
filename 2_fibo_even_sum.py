#!/usr/bin/env bash

def fibo_even_sum(n):
    sum = 0
    current_fib = 1
    prev_fib1 = 1
    prev_fib2 = 1
    while current_fib < n:
        prev_fib2 = prev_fib1    
        prev_fib1 = current_fib
        current_fib = prev_fib1 + prev_fib2
        if current_fib % 2 == 0:
            sum = sum + current_fib
    
    return sum

print(fibo_even_sum(4000000))
