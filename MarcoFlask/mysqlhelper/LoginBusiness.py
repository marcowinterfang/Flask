import pymysql

class LoginBusiness(object):
    """login module about users management"""
    
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def login(self,dict):
        try:
            username = dict["username"]
            password = dict["password"]
            db = MySQLdb.connect("localhost", "root", "Unlock@10", "circle", charset='utf8' )
            cursor = db.cursors()
            sql = "select * from loginfo where username = '" + username + "'"
            cursor.execute(sql)
            info = cursor.fetchone()

      except:
            pass
            


