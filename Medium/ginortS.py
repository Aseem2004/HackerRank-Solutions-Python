s=input()
l_letters = []
u_letters = []
o_digits = []
e_digits = []

for i in s:
    if i.islower():
        l_letters.append(i)
    elif i.isupper():
        u_letters.append(i)
    elif int(i)%2!=0:
        o_digits.append(i)
    else:
        e_digits.append(i)

l_strings=''.join(sorted(l_letters))
u_strings=''.join(sorted(u_letters))
o_strings=''.join(sorted(o_digits))
e_strings=''.join(sorted(e_digits))

print(f'{l_strings}{u_strings}{o_strings}{e_strings}')