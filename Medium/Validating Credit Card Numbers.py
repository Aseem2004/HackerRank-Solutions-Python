import re

x=r'^(?!.*(\d)(-*\1){3,})([456][0-9]{3}-?([0-9]{4}-?){3})$'

for i in range(int(input())):
    if(re.match(x,input())):
        print('Valid')
    else:
        print('Invalid')