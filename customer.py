import pymysql



class customerList:
    def __init__(self):
        self.data = []
        self.tempdata = {}
        self.tn = 'customers'
        self.fnl = ['fname', 'lname', 'email', 'password', 'subscribed']
        self.errorlist = []
        
    def connect(self):
        import config
        return pymysql.connect(host=config.DB['host'], port=config.DB['port'], user=config.DB['user'], passwd=config.DB['passwd'], db=config.DB['db'], autocommit=True) #setup our credentials

        
    def add(self):
        self.data.append(self.tempdata)
        
    def set(self, fn, val):
        if fn in self.fnl:
            self.tempdata[fn] = val
        else:
            print("Invalid field: " + str(fn))
            
    def update(self, n, fn, val):
        if len(self.data) >= (n + 1) and fn in self.fnl:
            self.data[n][fn] = val
        else:
            print("Could not set value at row " + str(n) + " col " + str(fn))
            
    def insert(self, n = 0):
        cols = '`,`'.join(self.fnl)
        cols = '`' + cols + '`'
        vals = ('%s,' * len(self.fnl))[:-1]
        tokens = []
        for fn in self.fnl:
            tokens.append(self.data[n][fn])
        sql = 'INSERT INTO `' + self.tn + '` (' + cols + ') VALUES (' + vals + ');'
        conn = self.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(sql, tokens)
        
    def verifyNew(self, n = 0):
        if len(self.data[n]['fname']) == 0:
            self.errorlist.append("First name cannot be blank.")
        if len(self.data[n]['lname']) == 0:
            self.errorlist.append("Last name cannot be blank.")
        if len(self.data[n]['email']) == 0:
            self.errorlist.append("Email cannot be blank.")
        if len(self.data[n]['password']) == 0:
            self.errorlist.append("Password cannot be blank.")
            
        if len(self.data[n]['fname']) > 50:
            self.errorlist.append("First name must be less than 50 characters.")
        if len(self.data[n]['lname']) > 50:
            self.errorlist.append("Last name must be less than 50 characters.")
        if len(self.data[n]['email']) > 50:
            self.errorlist.append("Email must be less than 50 characters.")
        if len(self.data[n]['password']) > 100:
            self.errorlist.append("Password must be less than 100 characters.")
            
        if self.data[n]['subscribed'] not in ['True', 'False']:
            self.errorlist.append("Subscribed field must be True or False.")
            
        if len(self.errorlist) > 0:
            for error in self.errorlist:
                print(error)
            self.errorlist = []
            return False
        else:
            return True