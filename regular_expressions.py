import re


pattern = re.compile('[h?is]')
my_str = 'this is regular 1 44 4 2123 444 78 expression'
a = pattern.findall(my_str)
b = pattern.search(my_str)
c = pattern.split(my_str)
print(a)

pattern2 = re.compile('^(([\w ]+) ([\d ]+))')
new_str = "may 25 2020"
regex = pattern2.findall(new_str)
print(regex)
