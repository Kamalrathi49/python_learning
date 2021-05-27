import utility
import shoping.shoping_cart as shop

import random

print(random.random())
print(random.randint(1, 10))

if __name__ == '__main__':
    fruits = shop.my_func('apple', 'banana', 'pineapple', 'mango')
    num = utility.my_func(100)
    print(random.choice(fruits))



