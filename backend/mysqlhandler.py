import mysql.connector


class dbhandler:

  def __init__(self):
       self.mydb = None

  def connect(self):
    try:
      self.mydb = mysql.connector.connect(
          host="localhost",
          user="cpaduser",
          password="cpad@2022",
          port = 3306,
          database = "vacc_drive"
        )
      print(self.mydb)  
    except:
      print("Connection to db failed")

  def insertstudentdata(self,val):

    try:

      mycursor = self.mydb.cursor()
      sql = "INSERT INTO students (name,date,status,vacc_name) VALUES (%s, %s,%s,%s)"
      mycursor.execute(sql, val)
      self.mydb.commit()
      res = {"code":200}
      return res

    except Exception as e:

       res ={"code":400}
       print(e)
       return res
       
  def insertdrivedata(self,val):

    try:

      mycursor = self.mydb.cursor()
      sql = "INSERT INTO drive (name,date_vac,count,used_vacc) VALUES (%s, %s,%s,%s)"
      mycursor.execute(sql, val)
      self.mydb.commit()
      res = {"code":200}
      return res

    except Exception as e:

       res ={"code":400}
       print(e)
       return res   

  def getstudentsdata(self):

    try:

       mycursor = self.mydb.cursor()
       mycursor.execute("SELECT * FROM students")
       myresult = mycursor.fetchall()
       out = []  
       for x in myresult:
           out.append(list(x)) 
       res = {"code":200,"output":out}
       return res    
    
    except Exception as e:

       res ={"code":400}
       print(e)
       return res

  def getdrivedata(self):

    try:

       mycursor = self.mydb.cursor()
       mycursor.execute("SELECT * FROM drive")
       myresult = mycursor.fetchall()
       out = []  
       for x in myresult:
           out.append(list(x))    
       res = {"code":200,"output":out}
       return res    
    
    except Exception as e:

       res ={"code":400}
       print(e)
       return res  


  def updatestudentsdata(self,val):

    try:

       mycursor = self.mydb.cursor()
       sql = "UPDATE students SET date = %s ,status=%s ,vacc_name =%s WHERE name = %s"
       mycursor.execute(sql,val)
       self.mydb.commit()  
       res = {"code":200}
       return res    
    
    except Exception as e:

       res ={"code":400}
       print(e)
       return res 


  def updatedrivedata(self,val):

    try:

       mycursor = self.mydb.cursor()
       sql = "UPDATE drive SET date_vac = %s ,count=%s,used_vacc=%s  WHERE name = %s"
       mycursor.execute(sql,val)
       self.mydb.commit() 
       res = {"code":200}
       return res    
    
    except Exception as e:

       res ={"code":400}
       print(e)
       return res

  def insertuserdetails(self, val):

      try:

          mycursor = self.mydb.cursor()
          sql = "INSERT INTO users (name,password) VALUES (%s, %s)"
          mycursor.execute(sql, val)
          self.mydb.commit()
          res = {"code": 200}
          return res

      except Exception as e:

          res = {"code": 400}
          print(e)
          return res

  def authenticate(self,val):

      try:
          mycursor = self.mydb.cursor()
          sql = "SELECT * FROM users where name = %s"
          mycursor.execute(sql,val[0])
          myresult = mycursor.fetchone()
          if myresult:
             password  = myresult[1]
             testpass = val[1]
             if password == testpass:
                res = {"code": 200}
             else:
               res = {"code": 201}

             return res

          else:
              res = {"code": 201}
              return  res

      except Exception as e:

          res = {"code": 400}
          print(e)
          return res


  def closeconnection(self):

    try:

       self.mydb.close()   
    
    except Exception as e:

       print(e)

  def getusersdata(self):

      try:

          mycursor = self.mydb.cursor()
          mycursor.execute("SELECT * FROM users")
          myresult = mycursor.fetchall()
          out = []
          for x in myresult:
              out.append(list(x))
          res = {"code": 200, "output": out}
          return res

      except Exception as e:

          res = {"code": 400}
          print(e)
          return res

  def getcolumns(self):

      try:

          mycursor = self.mydb.cursor()
          sql = "SHOW COLUMNS FROM students"
          out = mycursor.execute(sql)
          print(out)

      except Exception as e:
          print(e)


  def addcolumn(self):

      try:

          mycursor = self.mydb.cursor()
          sql = "ALTER TABLE students ADD vacc_name VARCHAR(100)"
          mycursor.execute(sql)
          self.mydb.commit()

      except Exception as e:
          print(e)


  def getcounts(self):

      try:

          mycursor = self.mydb.cursor()
          sql = "select count(*) as total_count,count(if(status='yes',1,null)) as A_count,count(if(status='no',1,null)) as B_count from students"
          mycursor.execute(sql)
          myresult = mycursor.fetchall()
          # print(myresult)
          res={"code":200,"output":list(myresult[0])}
          return res
      except Exception as e:
          print(e)

               

# db = dbhandler()
# db.connect()
# # db.insertstudentdata(['raghul','15/10/22','yes'])
# # db.insertdrivedata(['mid','15/10/22',100])
# # print(db.getstudentsdata())
# print(db.getdrivedata())
# # db.updatestudentsdata(['15/10/22','no','raghul'])
# # db.updatedrivedata(['15/10/22',500,'mid'])
# db.closeconnection()
     

