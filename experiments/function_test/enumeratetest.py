number = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [3, 5, 7], [1, 5, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9])

for count, i in enumerate(number):
    print(count, i)


charac = ["Tokyo", "Osaka", "Shiro", "Goku"]
y = ["Apple", "Orange", "White", "Black"]

x = list(enumerate(y + charac))

print(x)


