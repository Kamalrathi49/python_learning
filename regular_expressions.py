import re

pattern = re.compile('[h?is]')
my_str = 'this is regular 1 44 4 2123 444 78 expression'
a = pattern.findall(my_str)
b = pattern.search(my_str)
c = pattern.split(my_str)
print(a)

pattern2 = re.compile('^(([\w ]+) ([\d ]+))')
my_str2 = "may 25 2020"
regex = pattern2.findall(my_str2)
print(regex)

pattern3 = re.compile('^(([\d]+)[^/A-Za-z]([\d]+))')
my_str3 = "250x300"
regex2 = pattern3.search(my_str3)
print(regex2)


pattern4 = re.compile('(([c]ats|[d]ogs))')
my_str4 = "i love cats, i love dogs, i love logs, i love cogs"
regex3 = pattern4.search(my_str4)
print(regex3)

