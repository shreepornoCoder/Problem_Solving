# word = input()
word = 'hellohello'

for i in range(len(word), -2, -1):
    if i != len(word):
        for j in range(0, len(word)):
            if j <= i:
                print(word[j], end="")
            else:
                print("*", end="")
        print("")