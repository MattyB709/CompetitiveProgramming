import math
a = 18**6-5*36*18**4-5*36**2*18**2+36**3
b = 8 * 72**3
g = math.gcd(a,b)
print(a/g, b/g)

a2 = 18**4+2*36*18**2+36**2
b2 = 4*72**2
g = math.gcd(a2,b2)
print(a2/g, b2/g)
