for i in range(0, 10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{:01d}{:01d}".format(i, j))
        else:
            print("{:01d}{:01d}, ".format(i, j), end="")