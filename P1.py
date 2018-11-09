def star(words):
    size = max(len(word) for word in words)
    print('*' * (size + 4))
    for word in words:
        print('* {:<{}} *'.format(word, size))
    print('*' * (size + 4))
f = open(r"E:\file1.txt")
for line in f:
    s=line.split()
    star(s)

