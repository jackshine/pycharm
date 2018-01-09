import random
import string
seed = "1234567890"
#seed = "1234567890"
sa = []
salt = ''
for j in range(16):
	sa.append(random.choice(seed))
	salt = ''.join(sa)
print(salt)
