import re

pattern = re.compile('is')
my_str = 'this is regular expression'
a = pattern.search( my_str)
b = pattern.split(my_str)
c = pattern.findall(my_str)
print(b)


