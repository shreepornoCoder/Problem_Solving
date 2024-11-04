import sys
import math
def get_ints(): return map(int, sys.stdin.readline().strip().split())
 
a,b = get_ints()
res = a/b

print(10/4)
print(f"floor {a} / {b} =", math.floor(res))
print(f"ceil {a} / {b} =", math.ceil(res))
print(f"round {a} / {b} =", round(res))