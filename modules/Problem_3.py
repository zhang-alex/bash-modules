x = 86
y = x - 87

solved = 0

while (solved == 0) :
    x += 1
    y += 1
    
    print "input:","(",x,",",y,")"
    
    output = (2017-x)**0.5 + (2018-y)**0.5
    print "output:",output
    
    if (output == 22) :
        solved = 1
        
    print ""

print ""
print ""
print ""
print ""
print "Solved."
print "x =",x
print "y =",y
