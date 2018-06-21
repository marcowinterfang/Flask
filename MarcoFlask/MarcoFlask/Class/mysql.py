

class mysql:
    db = pymysql.connect("localhost","root","Unlock@10","circle")
    def __init__(self):
        pass
    
    def signin(self,username,password):
        if(username == "" or password == ""):
            return "AccountId or password is empty,please check"
        cursor = db.cursor()
        sql = "select username,pw from loginfo where username = '" + username + "'"
        nbr = cursor.execute(sql)
        if(nbr == 0):
            return "Your accountId(" + username + ") is NOT EXIST"
        data = cursor.fetchone()
        pw = hashlib.md5(password.encode('utf-8')).hexdigest()
        if(password == pw):
            return "success"
