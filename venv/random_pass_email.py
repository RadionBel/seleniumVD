import random
psw = ''
for x in range(12):
    psw = psw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    email = psw + "@gmail.com"
print(psw, email)
