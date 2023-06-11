import json

import random as rd

import mysql.connector


mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dbshopdar",
        charset='utf8')

mycursor=mydb.cursor()


class users:
	def __init__(self):
		self.fullname=""
		self.password=""
		self.email=""
		self.type=""
		self.id=0
	
	def setData(self,fn,p,e,t,id):
		self.fullname=fn
		self.password=p
		self.email=e
		self.type=t
		self.id=id
	
	def insert_as_userDb(self):
		global mydb
		mycursor=mydb.cursor()
		
		sql="insert into users set "
		sql=sql+"email='"+self.email+"',"
		sql=sql+"password='"+self.password+"',"
		sql=sql+"fullname='"+self.fullname+"',"
		sql=sql+"typeu='user'"
		try:
			mycursor.execute(sql)
			mydb.commit()
			return True
		except:
			return False
	
	def insert_as_adminDb(self):
		global mydb
		mycursor=mydb.cursor()
		sql="insert into users set "
		sql=sql+"email='"+self.email+"',"
		sql=sql+"password='"+self.password+"',"
		sql=sql+"fullname='"+self.fullname+"',"
		sql=sql+"typeu='admin'"
		try:
			mycursor.execute(sql)
			mydb.commit()
			return True
		except:
			return False

		
	def finduser(self,email,pwd):
		global mydb
		mycursor=mydb.cursor()
		sql="select * from users where email='"+email+"' and password='"+pwd+"'"
		mycursor.execute(sql)
		try:
			r=mycursor.fetchone()
			self.setData(r[4],r[2],r[1],r[3],r[0])
		except:
			raise Exception
		

	def getusingId(self,id):
		global mydb
		mycursor=mydb.cursor()
		
		sql="select * from users where id="+str(id)
		print(sql)
		mycursor.execute(sql)
		r=mycursor.fetchone()
		self.email=r[1]
		self.fullname=r[4]
		self.type=r[3]
		
	def getAll(self):
		global mydb
		mycursor=mydb.cursor()
		sql="select * from users"
		mycursor.execute(sql)
		res=mycursor.fetchall()
		P=[]
		for r in res:
				p={}
				p['email']=r[1]
				p['password']=r[2]
				p['type']=r[3]
				p['fullname']=r[4]
				p['id']=str(r[0])
				P.append(p)
		
		return (json.dumps(P))

		
	def getJSON(self):
			x={}
			x['email']=self.email
			x['fullname']=self.fullname
			return json.dumps(x)
    
class categories:
	def __init__(self,
id,title,descr):
		self.id=id
		self.title=title
		self.descr=descr


class materials:
	def __init__(self,
id,mtitle,mdescr):
		self.id=id
		self.mtitle=mtitle
		self.mdescr=mdescr

  
class orders:
	def __init__(self,
id,ids,idm,qnty,date1):
		self.id=id
		self.ids=ids
		self.idm=idm
		self.qnty=qnty
		self.date1=date1

class products:
	def __init__(self,
id,title,descr):
		self.id=id
		self.title=title
		self.descr=descr

class prod_cat:
	def __init__(self,
id,idc,idp):
		self.id=id
		self.idc=idc
		self.idp=idp


class prod_mat:
	def __init__(self,
id,idp,idm,quant):
		self.id=id
		self.idp=idp
		self.idm=idm
		self.quant=quant


class sales:
	def __init__(self,
id,idp,qnt,dates):
		self.id=id
		self.idp=idp
		self.qnt=qnt
		self.dates=dates


class supplier:
	def __init__(self,
id,fullname,phone,addr):
		self.id=id
		self.fullname=fullname
		self.phone=phone
		self.addr=addr

		