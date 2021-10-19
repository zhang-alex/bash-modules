import time
import math
from decimal import Decimal

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

isPrime = 1

toBreak = 0

primes = [2]

print ""
time.sleep(0.6)
print ""
time.sleep(0.6)
print "PLEASE USE CAUTION WHEN EXECUTING THIS PROGRAM"
time.sleep(0.6)
print "THE VALUES USED ARE INCOMPREHENSIBLY LARGE AND WILL BLOW YOUR MIND"
print ""
time.sleep(0.6)
print ""
time.sleep(0.6)
print ""
time.sleep(0.6)
print "Problem 1:"
time.sleep(0.6)
print ""
time.sleep(0.6)
print "Find all primes p for which 2017^(p-1) + p^3 is a perfect square"
time.sleep(0.6)
print ""
time.sleep(0.6)
print ""
time.sleep(0.6)
print "finding primes..."
time.sleep(0.6)
print ""
time.sleep(0.6)
print ""
time.sleep(0.6)

for i in range(3,25000) :

    isPrime = 1
    toBreak = 0

    for j in range(2,int(math.ceil(i**0.5))+1) :

        time.sleep(30/i**1.6)

        if (i % j == 0) :
            print i, "is composite because",j,'divides',i
            isPrime = 0
            toBreak = 1

        if (toBreak==1) : break

    if isPrime == 1 :
        print "                                                                                      ", i, "is prime"
        primes.append(i)

print ""
time.sleep(0.6)
print ""
time.sleep(0.6)
print ""
time.sleep(0.6)
print ""
time.sleep(0.6)
print ""
time.sleep(0.6)

print "listing primes from 1 to 25000;"
time.sleep(2)

for i in range(len(primes)) :
    time.sleep(0.0015)
    print primes[i]

print ""
time.sleep(0.8)
print ""
time.sleep(0.8)
print ""
time.sleep(0.8)
print ""
time.sleep(0.8)
print ""
time.sleep(0.8)

num_of_primes = 0

working_primes = []

for i in range(len(primes)) :

    now = time.clock()

    current_prime = primes[len(primes)-i-1]
    print ""
    print ""
    print "testing prime", i+1, "out of", len(primes) + 1
    time.sleep(0.12)
    print "current prime:", current_prime
    time.sleep(0.12)

    output = 2017**(current_prime-1) + current_prime**3
    print "output:", output
    time.sleep(0.12)

    if isqrt(output)**2 == output :
        print "HOLY."
        time.sleep(4)
        print "IVE FOUND A PRIME."
        time.sleep(2)
        print "the prime is ", current_prime
        time.sleep(2)
        print "let me repeat, the prime is ", current_prime
        time.sleep(2)
        print "again, the prime is ", current_prime
        time.sleep(2)
        working_primes.append(current_prime)
    else :
        print "prime does not work..."
        print ""
        print "estimated time until completetion:", (time.clock() - now)*(len(primes) - i + 1)/15, "seconds"
        print "-------------------------------------------------------"
        time.sleep(0.01)
print ""
time.sleep(0.6)
print ""
time.sleep(0.6)
print ""
time.sleep(0.6)
print "primes that work:"
print ""
time.sleep(0.6)
print ""
time.sleep(0.6)

for i in working_primes :
    print i
