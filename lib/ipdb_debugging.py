#!/usr/bin/env python3

import pdb  # Built-in debugger

def plus_two(num):
    return num + 2

def tracing_the_function():
    pdb.set_trace()  # Debugging breakpoint

    inside_the_function = "We're inside the function"
    print(inside_the_function)

    print("We're about to stop because of pdb!")
    pdb.set_trace()  # Second debugging breakpoint
    
    this_variable_hasnt_been_interpreted_yet = "The program froze before it could read me!"
    print(this_variable_hasnt_been_interpreted_yet)

if __name__ == "__main__":
    tracing_the_function()
