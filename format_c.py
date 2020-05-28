import string
import re

with open('quad.c', 'r') as f:
	str0 = f.read()

# Remove:
# - include directives
# - whitespace
# - punctuation
# - int main(int...

str1 = re.sub(r'#include.*[<"][a-z.]+[>"]' +  
			'|[' + string.whitespace + string.punctuation + ']'+  
			'|int.*main.*(.*int.*argc.*,.*char.*argv.*)', r'', str0).lower()

with open('std', 'w') as f:
	f.write(str1)

print(str1)
