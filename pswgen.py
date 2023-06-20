import string
import secrets

count = 0
pswds = int(input("How many passwords: "))

alphabet = string.ascii_letters + string.digits + string.punctuation
while count < pswds:
    password = ''.join(secrets.choice(alphabet) for i in range(12))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        print (password)
        count = count + 1