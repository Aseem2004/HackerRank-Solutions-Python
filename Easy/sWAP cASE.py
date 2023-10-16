def swap_case(s):
    s_new = []
    for i in list(s):
        if i.islower():
            s_new.append(i.upper()) 
        elif i.isupper():
            s_new.append(i.lower())
        else:
            s_new.append(i)
    return "".join(s_new)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)