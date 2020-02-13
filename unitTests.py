from customer import customerList

cl = customerList()
cl.set('fname', '')
cl.set('lname', '')
cl.set('email', '')
cl.set('password', '')
cl.set('subscribed', 'true')
cl.add()
canInsert = cl.verifyNew()
if canInsert == True:
    cl.insert()
cl.set('fname', 'a')
cl.set('lname', 'b')
cl.set('email', 'c')
cl.set('password', 'd')
cl.set('subscribed', 'True')
cl.add()
canInsert = cl.verifyNew(1)
if canInsert == True:
    cl.insert()