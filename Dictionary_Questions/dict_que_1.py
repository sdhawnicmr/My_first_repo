Capitals = {"China": "Beijing",
           "India": "New Delhi",
           "USA": "Washington DC",
           "Russia": "Moscow"}
print(Capitals)
print(Capitals.keys())
print(Capitals.values())

#Using dict() method
mystock= dict({"Product" : "Earphone",
               "Price": 3000,
               "Quantity": 5,
               "InStock": "Yes"
})
print(mystock)
print(mystock["Product"])
print(mystock.get("Product"))

Mutil_dimensional_dict = {1:Capitals,2:mystock}
print("----------")
print(Mutil_dimensional_dict)

mystock["Price"]= 1000
print(mystock)

mystock["Color"] = "Red"
print(mystock)

del mystock["Price"]
print(mystock)
#mystock.clear()
#print(mystock)

result = mystock.pop("Quantity")
print("The coresponding value of deleted key :", str(result))
print(mystock)
