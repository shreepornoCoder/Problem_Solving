def swap_case(s):
    res = []
    for char in s:
        char = str(char)
        if char.isalpha():
            if char.isupper():
                char = char.lower()

            else:
                char = char.upper()
        
        res.append(char)

    res = ''.join(res)
    
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)