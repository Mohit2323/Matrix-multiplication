import numpy as np
import random
import timeit

start = timeit.default_timer()

def generate_matrix(m, n):
    A = np.random.randint(1000, size=(1000, 1000))
    return(A)

def user_define(m, n):
    A = generate_matrix(m, n)    
    B = generate_matrix(m, n)
    print("Random Matrix 1 is:")
    print(A)
    print("Random Matrix 2 is:")
    print(B)
    print("Sum of two random matrices is:")
    print(A + B)
    return(A + B)
x = user_define(3, 4)
stop = timeit.default_timer()
execution_time = stop - start

print("Seconds to execute the program is := "+str(execution_time))