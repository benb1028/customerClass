from customer import customerList

cl = customerList()
d = {'fanme':'Testguy', 'lname':'test', 'email':'no@clarkson.edu',\
     'password':'12345', 'subscribed':'1'}
cl.add(d)
print(cl.data)