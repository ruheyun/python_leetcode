def my_write():
    f = open('../a.txt', 'w', encoding='utf-8')
    f.write('hello, 世界')
    f.close()


def my_read():
    f = open('../a.txt', 'r', encoding='utf-8')
    s = f.read()
    print(type(s), s)


if __name__ == '__main__':
    # my_write()
    my_read()
