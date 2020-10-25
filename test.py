#!/usr/bin/python3
def sieve(n):
    primes=[]
    temp_list = [0 for x in range(0,n)]
    i,j=2,2
    while(i*j<n):
         temp_list[i*j] = 1
         j=j+1
         if i*j >= n:
             i,j = i+1,2
    for i in range(2,n):
         if temp_list[i] == 0:
             primes.append(i)
    return primes

if __name__ == '__main__':
    n = int(input())
    print sieve(n)