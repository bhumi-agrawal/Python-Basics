bhumi = {
    "name": "Bhumi" ,
    "age": 18 ,
    "branch": "cs"
}
print(bhumi["name"])
bhumi["city"] = "agra"
print(bhumi)
bhumi["age"] = 19
print(bhumi)
del bhumi["age"]
print(bhumi)
print(len(bhumi))
print(bhumi.get("name"))
print(bhumi.keys())
print(bhumi.values())