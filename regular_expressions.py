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

pattern3 = re.compile(r"^(([\d]+)[^/A-Za-z]([\d]+))")
my_str3 = "250x300"
regex2 = pattern3.search(my_str3)
print(regex2)

pattern4 = re.compile('(([c]ats|[d]ogs))')
my_str3 = "i love cats,  i love dogs, i love logs, i love cogs"
regex3 = pattern4.search(my_str3)
print(regex3)
#
pattern5 = re.compile(r"(^([A-Za-z0-9_@]+)(\d$)+)")
my_str4 = "kamalrathi@49"
regex4 = pattern5.match(my_str4)
print(regex4)

pattern6 = re.compile(r"(^([A-Za-z_]+[:])([\w@+/-_$]))")
my_str5 = "this is my email_id:kamalrathi@49"
regex5 = pattern6.match(my_str5)
print(regex5)
