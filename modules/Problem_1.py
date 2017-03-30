import time
import math

isPrime = 1

toBreak = 0

primes = [2]

print "Problem 1:"
print ""
print ""

for i in range(3,10000) :

    isPrime = 1
    toBreak = 0

    for j in range(2,int(math.ceil(i**0.5))+1) :

        time.sleep(6/i**1.6)

        if (i % j == 0) :
            print i, "is composite because",j,'divides',i
            isPrime = 0
            toBreak = 1

        if (toBreak==1) : break

    if isPrime == 1 :
        print "                                                                                                                                                ", i, "is prime"
        primes.append(i)

print ""
time.sleep(0.5)
print ""
time.sleep(0.5)
print ""
time.sleep(0.5)
print ""
time.sleep(0.5)
print ""
time.sleep(0.5)

print "listing primes from 1 to 10000;"
time.sleep(2)

for i in range(len(primes)) :
    time.sleep(0.0025)
    print primes[i]

print ""
time.sleep(0.5)
print ""
time.sleep(0.5)
print ""
time.sleep(0.5)
print ""
time.sleep(0.5)
print ""
time.sleep(0.5)
