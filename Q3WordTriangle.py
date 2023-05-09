x = input("Enter a word: ")
length = len(x)

for i in range(length):
    print(x[:i+1])