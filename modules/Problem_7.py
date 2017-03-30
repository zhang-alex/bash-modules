import time

x = 86
y = x - 87

solved = 0

while (solved == 0) :
    x += 1
    y += 1

    print "input:","(",x,",",y,")"
    time.sleep(0.0008)

    output = (2017-x)**0.5 + (2018-y)**0.5
    print "                                output:",output
    time.sleep(0.0008)

    if (output == 22) :
        solved = 1

    print ""
    time.sleep(0.0008)

print ""
time.sleep(0.1)
print ""
time.sleep(0.1)
print ""
time.sleep(0.1)
print ""
time.sleep(0.1)
print "Solved."
time.sleep(0.1)
print "x =",x
time.sleep(0.1)
print "y =",y
