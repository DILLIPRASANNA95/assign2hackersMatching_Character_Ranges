Regex_Pattern = r'__________'	# Do not delete 'r'.
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'    # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, "raw_input"()))).lower())