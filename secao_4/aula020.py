# secrets gera números aleatórios seguros
import secrets
import string as s
from secrets import SystemRandom as Sr

print("".join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=8)))

random = secrets.SystemRandom()

print(secrets.randbelow(50))

print(random.randrange(10,20, 2))

print(random.randint(1,100))
