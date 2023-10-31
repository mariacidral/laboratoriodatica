for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print('πtu')
    if i % 3 == 0 and i % 3 == 0 and i % 7 == 0:
        print('πtuco')
    else:
        if i % 3 == 0:
            print('π')
        if i % 5 == 0:
            print('tu')
        if i % 7 == 0:
            print('co')
        if i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            print(i)