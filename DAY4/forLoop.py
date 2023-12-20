# name = ['krishna' , 'sahil' ,'sagar' ,'karan' ,'kapil']
# for i in name:
#     if i == "sahil":
#         continue
#     print(f"name is : {i} ")

details = {"name":"sahil",
           "surname":"mulchandani",
           "age": 19,
           "phone_no": 9999999999,
           "course" : "btech",
           "address" : "jaripatka, nagpur",
           "pincode": 444444}
for key,value in details.items():
    print (f"{key} : {value}")
