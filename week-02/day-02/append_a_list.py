# - Create a variable named `nimals`
#   with the following content: `["kuty", "macs", "cic"]`
# - Add all elements an `"a"` at the end

nimals = ["kuty", "macs", "cic"]

animals = []

for i in range(len(nimals)):
    animals.append(nimals[i] + "a")

print(animals)