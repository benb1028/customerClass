from customer import customerList

cl = customerList()
cl.set('fname', 'TYestguy')
cl.set('lname', 'test')
cl.set('email', 'a@a.com')
cl.set('password', '123')
cl.set('subscribed', 'True')
cl.add()
cl.insert()