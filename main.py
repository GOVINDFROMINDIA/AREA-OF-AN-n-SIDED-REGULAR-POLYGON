#0. Import header files/ modules.
  import math

#1. Get number of sides.
  number = int(input("HOW MANY SIDES DOES POLYGON HAVE? "))
 
#2. Get side length.
  length = float(input("length of a side: "))

#3. Area = number * (length * length) / (4 * tan(pi / number))
  number*(length*length)/(4*math.tan(math.pi/number))
  
#4. Display Area.
  print ("THE AREA OF YOUR",number,"SIDED POLYGON IS ",area)