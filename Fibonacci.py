#Code by:Gerasimos Pnevmatikakis (SoTilted).
import time#To compare which function is faster.
import numpy as np#To calculate a square root(we could just replace it with the result).
from functools import lru_cache#In order to use cache memory for one of the functions.

#<------------------------------------- FUNCTIONS ------------------------------------->
def Fibonacci_no1(n):#Classic Fibonacci function,recursive (Fn=Fn-1 + Fn-2).
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci_no1(n-1)+Fibonacci_no1(n-2)

def Fibonacci_no2(n,temp):#The same recursive method, but we use a list to save the already calculated Fibonacci numbers.
    if temp[n-1]!=0:#This checks if that number has been calculated.
        return temp[n-1]
    else:
        temp[n-1]=(Fibonacci_no2(n-1,temp)+Fibonacci_no2(n-2,temp)) 
    return temp[n-1]

def Fibonacci_no3(n):#This is a pure calculative function that uses the close type of Fibonacci.
    phi=(1+np.sqrt(5))/2
    psi=(1-np.sqrt(5))/2
    return (phi**n-psi**n)/np.sqrt(5)

@lru_cache
def Fibonacci_no4(n):#This function uses the cache memory to save previous results, same as Fibonacci_no2.
    
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci_no4(n-1)+Fibonacci_no4(n-2)
#<------------------------------------- MAIN CODE ------------------------------------->
#Input
n=int(input('Give me the Fibonacci number you want to calculate: \n'))
#<-------------------------------- Counting time for function no1 -------------------------------->
toc=time.perf_counter()#Saves time it took to reach this part of the code.
print(f'First Fibonacci function: {Fibonacci_no1(n)}')#function call and print.
tic=time.perf_counter()#same here
print(f'time it took:{tic-toc:0.05f} for n={n}')#Prints the difference of the counters which is the time
#spent to execute the function and the print.
#<-------------------------------- Counting time for function no2 -------------------------------->
L=[1]+[1]+[0]*(n-2)
toc=time.perf_counter()
print(f'Second Fibonacci function: {Fibonacci_no2(n,L)}')
tic=time.perf_counter()
print(f'time it took:{tic-toc:0.05f} for n={n}')
#<-------------------------------- Counting time for function no3 -------------------------------->
toc=time.perf_counter()
print(f'Third fibonacci function: {int(Fibonacci_no3(n))}')
tic=time.perf_counter()
print(f'time it took:{tic-toc:0.05f} for n={n}')
#<-------------------------------- Counting time for function no4 -------------------------------->

toc=time.perf_counter()
print(f'Fourth Fibonacci function: {Fibonacci_no4(n)}')
tic=time.perf_counter()
print(f'time it took:{tic-toc:0.05f} for n={n}')



"""
As we can see, The first Fibonacci function is a lot slower than the rest, the reason being that
in order to calculate a big number, it will calculate small,already calculated numbers, again and
again.
This problem is solved by the second function, that uses a database to save already calculated
Fibonacci numbers, so instead of calculating them again, it returns the result.
The third function uses the closed type Fibonacci function and that way it is just a numeric
calculation.(It could probably become faster if we calculate the power of phi and psi with a
faster method.)
The fourth and last function use the cache memory in order to save the previous results and 
it checks first if a number has already been calculated before recursing again.
<------------------------------ Pros and Cons ------------------------------>
First function is bad for numbers bigger than 30 but really simple to understand.
Second function is the idea in the right direction, very fast for both small and
big numbers.(Note that array usage instead of list may speed it up a bit.)
Third function is The fastest function, but it comes at a cost of accuracy at
bigger numbers.
Fourth function is the best, fast and accurate for big numbers, basically an
optimazed version of the second function.(Note that there is a built in maxsize 
for cache usage.)
<------------------------------ Conclusions ------------------------------>
The purpose of this code is to demonstrate how a simple function can become 
really bad really fast, and to show that we can keep optimizing it.
The question generated from this is, at what point is optimizing a waste of
time instead of a gain?
"""
