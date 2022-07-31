import json

world_dictionary = {
    "names": {
        "person": "Jesus",
        "age": 34,
        "height": "175cm",
        "weight": "60kg"
    },
    "fruits": {
        "colour": "red",
        "type": "devil",
        "name": "apple"
    }
}

the_string = json.dumps(world_dictionary, indent=4)
with open("data.json", "w") as f:
    f.write(the_string)