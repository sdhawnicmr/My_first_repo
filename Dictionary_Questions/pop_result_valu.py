mystock= dict({"Product" : "Earphone",
              "Price": 3000,
              "Quantity": 5,
              "InStock": "Yes"
})
result = mystock.pop("Quantity")
print("The corresponding value of deleted key:",  str(result))
print(mystock)