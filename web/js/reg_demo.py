import re
pattern = re.compile(r'^index*')
match = pattern.match('index.html')
if match:
    print(match.group())
else:
    print('false')