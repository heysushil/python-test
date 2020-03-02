# regex using module re to match patterns

'''
MetaCharacters
Metacharacters are characters that are interpreted in a special way by a RegEx engine. Here's a list of metacharacters:

[] . ^ $ * + ? {} () \ |

Here, [abc] will match if the string you are trying to match contains any of the a, b or c.

You can also specify a range of characters using - inside square brackets.

[a-e] is the same as [abcde].
[1-4] is the same as [1234].
[0-39] is the same as [01239].

You can complement (invert) the character set by using caret ^ symbol at the start of a square-bracket.

[^abc] means any character except a or b or c.
[^0-9] means any non-digit character.
'''
import re
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern,test_string)
print(result)
if result:
    print('Pattern matched')
else:
    print('Pattern not matched')
