import time

print ""
time.sleep(0.8)
print ""
time.sleep(0.8)
print "Problem 3:"
time.sleep(0.8)
print ""
time.sleep(0.8)
print "Find all possible values of the perimeter of a Pythagorean triangle whose hypotenuse has length 2017"
time.sleep(0.8)
print ""
time.sleep(0.8)
print ""
time.sleep(0.8)
print "let's go"
time.sleep(0.8)
print ""
time.sleep(0.8)
print ""
time.sleep(0.8)

pythagorean_list = [[0,0]]
counter = 0

for x in range(1,2017) :
    for y in range(x,2017) :
        time.sleep(0.001)

        print "input:","(",x,",",y,")"

        output = (x**2 + y**2) ** 0.5

        print "                                output:",output

        if output == 2017 :
            print "                                                    noice", "(",x,",",y,")", "works"
            pythagorean_list[counter][0] = x
            pythagorean_list[counter][1] = y
            counter += 1
            time.sleep(5)

for counter in range(len(pythagorean_list)) :
    print "(",pythagorean_list[counter][0],",", pythagorean_list[counter][1],")"
    print
