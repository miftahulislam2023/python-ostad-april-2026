person1 = {
    "name": "Miftahul Islam",
    "phone": "01742855755",
    "address": "Dingadoba, Rajpara, Rajshahi",
    "age": 34
}

"""
* Wrong approaches
person1.update("name", "Pradip") 
person1.update("name") = "Pradip" 
"""

person1.update({
    "name": "Pradip"
})

person1.update({
    "age": 22
})

print(person1)