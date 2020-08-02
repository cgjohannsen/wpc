import re
import string

# Standardizes input. Parts are syntax agnostic i.e. setting to lowercase,
# stripping of whitespace and punctuation
#
# Currently also supports some syntax specific behavior for C, such as 
# removing comments and any main function signature
#
# TODO
# strip unique C variable names. replace all variables names of each type 
# with generic identifier
def standardize(s, ext):
	
	std = s.lower()
	
	if ext == 'c':
		std = re.sub(r'//.*\n', r'', std)
		std = re.sub(r'int.*main.*(.*int.*argc.*,.*char.*argv.*)', r'', std)
	
	std = re.sub(r'[' + string.whitespace + string.punctuation + r']', r'', std)
	
	return std
