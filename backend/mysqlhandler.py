import mysql.connector


class dbhandler:

  def __init__(self):
       self.mydb = None

  def connect(self):
    try:
      self.mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="Sarababy@2021",
          port = 3006,
          database = "student_details"
        )
      print(self.mydb)  
    except:
      print("Connection to db failed")

  def insertstudentdata(self,val):

    try:

      mycursor = self.mydb.cursor()
      sql = "INSERT INTO students (name,date,status) VALUES (%s, %s,%s)"
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
      sql = "INSERT INTO drive (name,date_vac,count) VALUES (%s, %s,%s)"
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
       sql = "UPDATE students SET date = %s ,status=%s  WHERE name = %s"
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
       sql = "UPDATE drive SET date_vac = %s ,count=%s  WHERE name = %s"
       mycursor.execute(sql,val)
       self.mydb.commit() 
       res = {"code":200}
       return res    
    
    except Exception as e:

       res ={"code":400}
       print(e)
       return res  


  def closeconnection(self):

    try:

       self.mydb.close()   
    
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
     

