with open('text_file.txt', mode='a') as my_file:
    text = my_file.write('python is easy to learn :)')
    print(my_file.readlines())
try:
    with open('text.tx', mode='r') as file:
        print(file.readline())
except FileNotFoundError:
    print("file does not found")
