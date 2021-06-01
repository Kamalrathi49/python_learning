# with open('text_file.txt', mode='a') as my_file:
#     text = my_file.write('python is easy to learn :)')
#     print(my_file.readlines())

with open('text.txt', mode='w') as file:
    texts = file.write('python is pretty complicated :(')
    print(texts)
