import random
import string

def randomStringDigits(stringLength=13) :
    # Generate a random string of letters and digits
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

providers = ["@gmail.com", "@googlemail.com", "@gmx.de","@outlook.com","@outlook.fr","@yandex.ru","@mail.com","@yahoo.co.uk","@protonmail.ch"]


rngemail = randomStringDigits(10)

print((rngemail) + random.choice(providers))
