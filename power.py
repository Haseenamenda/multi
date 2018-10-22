import math
n,m=map(int,input().split())
m*=n	
s=math.sqrt(m)
if s==int(s):
	print("yes")
else :
	print("no")
