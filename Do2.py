import math

ab = int(input())
bc = int(input())
ac = ((ab*ab)+(bc*bc))**0.5
mc = ac/2

theta = math.asin(mc/bc)*(180/3.14)
print("%d°"%(theta))
