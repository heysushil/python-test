# regex using module re to match patterns
import re
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern,test_string)
print(result)
if result:
    print('Pattern matched')
else:
    print('Pattern not matched')