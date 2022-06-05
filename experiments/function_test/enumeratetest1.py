characters = ["Krillin", "Goku", "Goku", "Gohan", "Piccolo",
              "Krillin", "Goku", "Vegeta", "Gohan", "Piccolo",
              "Piccolo", "Goku", "Vegeta", "Goku", "Piccolo",
              "Apple", "Pinapple"]

character_map = {character: [] for character in characters}

for index, character in enumerate(characters):
    character_map[character].append(index)

print(character_map)

print("\n-----------------------------")

dic = {"apple": ["pie", "juice", "candy", "watch", "pie", "juice", "juice", "candy", "pie", "juice"]}
print(len(dic["apple"]))

for x, y in enumerate(dic["apple"]):
    print("Apple {:5s} {}".format(y.title(), x))

print("\n-----------------------------")

extra_dict = {i: [] for i in dic["apple"]}

print(extra_dict)

for x, y in enumerate(dic["apple"]):
    extra_dict[y].append(x)
    print(extra_dict)
