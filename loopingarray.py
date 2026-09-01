gems = ["Diamond", "Ruby", "La peace", "Emerald", "Amethyst", "Topaz"]
elements = {
    "Pyro": "Fire",
    "Hydro": "Water",
    "Electro": "Lightning",
    "Anemo": "Wind",
    "Geo": "Earth",
    "Dendro": "Nature",
    "Cryo": "Ice",
}

print(gems)

print ("=====================")

print(elements)

print ("=====================")

for gem in gems:
    print(gem)

print ("=====================")

for element in elements:
    print(element)

print ("=====================")

for key, value in elements.items():
    print(key, value)

print ("=====================")

for key in elements.keys():
    print(key)

print ("=====================")

for value in elements.values():
    print(value)
