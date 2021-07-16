# Regex - Matching digts / non-digits
# You have a test string . Your task is to match the pattern xxXxxXxxxx 
Here x denotes a digit character, and X denotes a non-digit character.

Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())