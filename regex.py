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

. - Period

A period matches any single character (except newline '\n').

^ - Caret

The caret symbol ^ is used to check if a string starts with a certain character.

$ - Dollar

The dollar symbol $ is used to check if a string ends with a certain character.

* - Star

The star symbol * matches zero or more occurrences of the pattern left to it.

+ - Plus

The plus symbol + matches one or more occurrences of the pattern left to it.

? - Question Mark

The question mark symbol ? matches zero or one occurrence of the pattern left to it.

{} - Braces

Consider this code: {n,m}. This means at least n, and at most m repetitions of the pattern left to it.

| - Alternation

Vertical bar | is used for alternation (or operator).

() - Group

Parentheses () is used to group sub-patterns. For example, (a|b|c)xz match any string that matches either a or b or c followed by xz

\ - Backslash

Backlash \ is used to escape various characters including all metacharacters. For example,

\$a match if a string contains $ followed by a. Here, $ is not interpreted by a RegEx engine in a special way.

If you are unsure if a character has special meaning or not, you can put \ in front of it. This makes sure the character is not treated in a special way.

'''

'''
----------------Special Sequences--------------------------
Special sequences make commonly used patterns easier to write. Here's a list of special sequences:

\A - Matches if the specified characters are at the start of a string.

\b - Matches if the specified characters are at the beginning or end of a word.

\B - Opposite of \b. Matches if the specified characters are not at the beginning or end of a word.

\d - Matches any decimal digit. Equivalent to [0-9]

\D - Matches any non-decimal digit. Equivalent to [^0-9]

\s - Matches where a string contains any whitespace character. Equivalent to [ \t\n\r\f\v].

\S - Matches where a string contains any non-whitespace character. Equivalent to [^ \t\n\r\f\v].

\w - Matches any alphanumeric character (digits and alphabets). Equivalent to [a-zA-Z0-9_]. By the way, underscore _ is also considered an alphanumeric character.

\W - Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_]

\Z - Matches if the specified characters are at the end of a string.

Tip: To build and test regular expressions, you can use RegEx tester tools such as regex101. This tool not only helps you in creating regular expressions, but it also helps you learn it.

Now you understand the basics of RegEx, let's discuss how to use RegEx in your Python code.
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

# use findall
p = '\d+'
s = 'hello 34 sushil 45 how 55'
result = re.findall(p,s)
print(result)




