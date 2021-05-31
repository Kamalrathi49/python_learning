from collections import Counter, defaultdict, OrderedDict
import emoji


li = [1, 2, 3, 3, 4, 5, 6, 6, 7, 5]
string = emoji.emojize('python is :red_heart: with pycharm :red_heart:')
print(Counter(li))
print(Counter(string))

my_dict = defaultdict(lambda: 0, {
    'a': 1,
    'b': 2,
    'c': 3
})

print(my_dict['d'])
