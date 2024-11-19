def checking(string1:str, string2:str):
    if string1 == string2:
        print("YES")

    else:
        print("NO")

s = input()
t = input()

s = s.replace(" ", "")
t = t.replace(" ", "")

if len(s) == 0 and len(t) == 0:
    checking(s, t)

else:
    u = s[::-1]
    checking(u, t)
