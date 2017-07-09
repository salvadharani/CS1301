#Creates myDictionary with sprockets=5, widgets=11, cogs=3, and gizmos=15
myDictionary = {"sprockets" : 5, "widgets" : 11,
                "cogs" : 3, "gizmos": 15}
print(myDictionary)

#Creates the new key "gadgets" with value 1
myDictionary["gadgets"] = 1
print(myDictionary)
del myDictionary["gadgets"]
print(myDictionary)
