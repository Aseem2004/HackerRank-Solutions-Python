import re
import email.utils as emu

for _ in range(int(input())):
    mail = emu.parseaddr(input())
    if re.match(r"^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$", mail[1]):
        print(emu.formataddr(mail))