import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
 
a,b = get_ints()
print((a%10)+(b%10))