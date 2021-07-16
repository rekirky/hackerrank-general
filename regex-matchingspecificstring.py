# Matching Specific String
# Match string 'hackerrank' from the input string


Regex_Pattern = r'hackerrank'	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))