x = ((1, 2, 3), (4, 5, 6), (4, 5, 1))

y = [4, 1, 6, 5]
for index, tile in enumerate(x):
    print(tile)
    z = all(item in y for item in tile)
    if z is True:
        break