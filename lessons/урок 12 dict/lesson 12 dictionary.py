#dictionary
#key -> value
list1 = list("abcdefg")
print(list1[4])

dict1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
print(dict1[2])

dict2 = {0: 'a', 1.5: 'b', True: 'c', "string": 'd' , (1, 2, 3): 'e'}
dict2["string"] = [1, 2, 3, 4]
print(dict2["string"])
print(dict2)
# ключи должны быть неизменяемый тип данных

dict3 = {}
dict4 = dict()
# пустой словарь

dict4["Key"] = "Value"
dict4["key1"] = "Value1"
print(dict4)

dict5 = dict([("Belarus", "Minsk"), ("Germany", "Berlin")])
print(dict5)

dict6 = dict(Ukraine = "Kiev", Poland = "Warsaw")
print(dict6)

countries = ["USA", "CANADA", "SPAIN"]
capitals = ["WASHINGTON", "OTTAWA", "MADRID"]

dict7 = dict(zip(countries, capitals))
print(dict7)
dict7 = dict(zip(countries, capitals))
print(list(zip(countries, capitals)))

#print(dir(dict))

del dict7["USA"]
print(dict7)

# удаление пересмотреть надо будет





dict6.update(dict5)
print(dict6)

dict8 = {"Germany": "Minks"}
dict6.update(dict8)
print(dict6)

dict9 = dict7 | dict8
print(dict9)

for key in dict9:
    print(key, dict9[key])

for value in dict9.values():
    print(value)

for key, value in dict9.items():
    print(key, " -> ", value)

print(dict9.items())
print(dict9.keys())
print(dict9.values())

print(dict9.get("Canada", " usa not exists"))

string1 = "asdsadsafasjfjkljklkfghs"
dict10 = {}

for letter in string1:
    dict10[letter] = dict10.get(letter, 0) + 1

print(dict10)

print(sorted(dict10, key=lambda x: x[0]))

print(sorted(dict10.items(), key=lambda x: x[0]))

dict11 = {}
for letter in string1:
    if letter in dict11.keys():
        dict11[letter] += 1
    else:
        dict11[letter] = 1

dict11 = (dict9.fromkeys(countries, capitals))
print(dict11)

print(dict11["USA"] >= dict11["CANADA"])

dict9["Russia"] = "St.Petersburg"
print(dict9)

print(dict11["USA"][2])