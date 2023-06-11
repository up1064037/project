from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import send_file
from flask import jsonify
from flask import session
import random as rd

import mysql.connector


mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234Abcd!",
        database="dbshopdar",
        charset='utf8')

mycursor=mydb.cursor()


SESSION_TYPE = 'redis'
app = Flask(__name__)
app.secret_key = "1234"  


#roots

@app.route("/")
def firstpage():
    
    if(session.get("u")!=None):
        u=session.get("u")
        t=session.get("t")
        return render_template('main.html', menu=t, user=u)
    else:
        return render_template('index.html', menu="")

@app.route("/js/<file>")
def jsfile(file):
    return send_file(file)


@app.route("/img/<file>")
def images(file):
    return send_file(file)

@app.route("/css/<file>")
def cssread(file):  
    return send_file(file)


@app.route("/login")
def login1():
    return render_template('login.html',menu=1)


@app.route("/loginadmin")
def showdataadmin():
    return render_template('loginadmin.html',menu=1)



@app.route("/signup")
def signup():
    return render_template('signup.html',menu=1)


@app.route("/signup2", methods=['POST', 'GET'])
def singup2():
    if request.method == 'POST':
        e=str(request.form.get('username'))
        p=str(request.form.get('pwd'))
       
        sql="insert into admin set "
        sql=sql+"username='"+e+"',"
        sql=sql+"password='"+p+"'"
        
        print(sql)
        try:
            
            mycursor.execute(sql)
            mydb.commit()
            error=0
        except:
            error=1
        
       
    return jsonify({"err": error})

@app.route("/data")
def datajs():
    L=[]
    for i in range(10):
        x=rd.randint(1,10)
        y=rd.randint(1,20)
        o={"x":x,"y":y}
        L.append(o)
    return jsonify(L)

@app.route("/checklogin", methods=['POST', 'GET'])
def checklogin():
    if request.method == 'POST':
        e=str(request.form.get('username'))
        p=str(request.form.get('pwd'))
       
        try:
            sql="select * from admin where username='"+e+"' and password='"+p+"'"
            print(sql)
            mycursor.execute(sql)
            r=mycursor.fetchone()
            session['u']=r[1]
            session['t']="admin"
            u=r[1]
            m="admin"
            return render_template('main.html',menu=m, user=u)
        except:
            print("Not found")
            session['u']=None
            error=1
            m=""
            return render_template('login.html',menu=m,error=1)

@app.route("/putpoint")
def putpoint():
    if(session.get("u")!=None):
        return render_template('putpoint.html', menu=2)
    else:
        return render_template('index.html', menu=1)

    

@app.route("/logout")
def logout():
    session['u']=None
    return render_template('index.html', menu="")

    
@app.route("/admindata")
def admindata():
    sql="select * from admin where username='"+session['u']+"'"
    mycursor.execute(sql)
    r=mycursor.fetchone()  
    return jsonify(r)


@app.route("/profile")
def profile():
    if(session.get("u")!=None):
        return render_template('profile.html', menu="admin")
    else:
        return render_template('index.html', menu="")
    
@app.route("/sales")
def sales():
    if(session.get("u")!=None):
        return render_template('sales.html', menu="admin")
    else:
        return render_template('index.html', menu="")


@app.route("/orders")
def orders():
   if(session.get("u")!=None):
        return render_template('orders.html', menu="admin")
   else:
        return render_template('index.html', menu="")

        

@app.route("/stats")
def stats():
    if(session.get("u")!=None):
        return render_template('profile.html', menu="admin")

@app.route("/getdata", methods=['POST', 'GET'])
def getdata():
    if request.method == 'POST':
        print(str(request.form.get('email'))+" "+str(request.form.get('pwd')))
    return render_template('login.html')


@app.route("/updateadmin", methods=['POST', 'GET'])
def updateadmin():
    if request.method == 'POST':
        e=str(request.form.get('username'))
        p=str(request.form.get('pwd'))    
        sql="update admin set username='"+e+"', password='"+p+"' where username='"+session['u']+"'";
        print(sql)
        try:
            mycursor.execute(sql)
            mydb.commit()
            session['u']=e
            error=0
        except:
            error=1
    return jsonify({"err": error})



@app.route("/updateadmin2", methods=['POST', 'GET'])
def updateadmin2():
    if request.method == 'POST':
        id1=str(request.form.get('id1'))
        e=str(request.form.get('username'))
        p=str(request.form.get('pwd'))  
        sv=str(request.form.get('sv'))   
        print(sv)
        if sv=="0": 
        	sql="update admin set username='"+e+"', password='"+p+"' where id='"+id1+"'"
        	
        if sv=="1": 
        	sql="delete from admin  where id='"+id1+"'"
        
        
        print(sql)
        try:
            mycursor.execute(sql)
            mydb.commit()
            
            error=0
        except:
            error=1
    return jsonify({"err": error})


@app.route("/users")
def users():
    if(session.get("u")!=None):
        return render_template('users.html', menu="admin")
    else:
        return render_template('index.html', menu="")
        
        

        

@app.route("/getusers")
def getusers():
    sql="select * from admin"

    mycursor.execute(sql)
    r=mycursor.fetchall()
    return jsonify(r)
    
@app.route("/getuser/<id>")
def getuser(id):
    sql="select * from admin where id="+str(id)
    
    mycursor.execute(sql)
    r=mycursor.fetchone()
    return jsonify(r)
    
    
#categories
###########################################################



@app.route("/newcat", methods=['POST', 'GET'])
def newcat():
    if request.method == 'POST':
        e=str(request.form.get('cat'))
        p=str(request.form.get('catdescr'))
       
        sql="insert into categories set "
        sql=sql+"title='"+e+"',"
        sql=sql+"descr='"+p+"'"
        
        print(sql)
        try:
            
            mycursor.execute(sql)
            mydb.commit()
            error=0
        except:
            error=1
        
       
    return jsonify({"err": error})


@app.route("/categories")
def categories():
    if(session.get("u")!=None):
        return render_template('categories.html', menu="admin")
    else:
        return render_template('index.html', menu="")
        
        

        

@app.route("/getcategories")
def getcategories():
    sql="select * from categories"
  
    mycursor.execute(sql)
    r=mycursor.fetchall()
    return jsonify(r)
    

@app.route("/getcategory/<id>")
def getcategory(id):
    sql="select * from categories where id="+str(id)
   
    mycursor.execute(sql)
    r=mycursor.fetchone()
    return jsonify(r)
    

@app.route("/updatecat", methods=['POST', 'GET'])
def updatecat():
   if request.method == 'POST':
        id1=str(request.form.get('id1'))
        e=str(request.form.get('cat1'))
        p=str(request.form.get('catdescr1'))  
        sv=str(request.form.get('sv'))   
        print(sv)
        if sv=="0": 
        	sql="update categories set title='"+e+"', descr='"+p+"' where id='"+id1+"'"
        	
        if sv=="1": 
        	sql="delete from categories where id='"+id1+"'"
        
        
        print(sql)
        try:
            mycursor.execute(sql)
            mydb.commit()
            
            error=0
        except:
            error=1
    
   return jsonify({"err": error})



#matirials
###########################################################



@app.route("/newmat", methods=['POST', 'GET'])
def newmat():
    if request.method == 'POST':
        e=str(request.form.get('mat'))
        p=str(request.form.get('mdescr'))
       
        sql="insert into materials set "
        sql=sql+"mtitle='"+e+"',"
        sql=sql+"mdescr='"+p+"'"
        
        print(sql)
        try:
            
            mycursor.execute(sql)
            mydb.commit()
            error=0
        except:
            error=1
        
       
    return jsonify({"err": error})


@app.route("/materials")
def materials():
    if(session.get("u")!=None):
        return render_template('materials.html', menu="admin")
    else:
        return render_template('index.html', menu="")
        
        

        

@app.route("/getmaterials")
def getmaterials():
    sql="select * from materials"
  
    mycursor.execute(sql)
    r=mycursor.fetchall()
    return jsonify(r)
    
@app.route("/getmaterial/<id>")
def getmaterial(id):
    sql="select * from materials where id="+str(id)
   
    mycursor.execute(sql)
    r=mycursor.fetchone()
    return jsonify(r)
    

@app.route("/updatemat", methods=['POST', 'GET'])
def updatemat():
   if request.method == 'POST':
        id1=str(request.form.get('id1'))
        e=str(request.form.get('mat1'))
        p=str(request.form.get('mdescr1'))  
        sv=str(request.form.get('sv'))   
        print(sv)
        if sv=="0": 
        	sql="update materials set mtitle='"+e+"', mdescr='"+p+"' where id='"+id1+"'"
        	
        if sv=="1": 
        	sql="delete from materials where id='"+id1+"'"
        
        
        print(sql)
        try:
            mycursor.execute(sql)
            mydb.commit()
            
            error=0
        except:
            error=1
    
   return jsonify({"err": error})



#Products
###########################################################



@app.route("/newprd", methods=['POST', 'GET'])
def newprd():
    if request.method == 'POST':
        e=str(request.form.get('ptitle'))
        p=str(request.form.get('pdescr'))
       
        sql="insert into products set "
        sql=sql+"title='"+e+"',"
        sql=sql+"descr='"+p+"'"
        
        print(sql)
        try:
            
            mycursor.execute(sql)
            mydb.commit()
            error=0
        except:
            error=1
        
       
    return jsonify({"err": error})



@app.route("/newprdmat", methods=['POST', 'GET'])
def newprdmat():
    if request.method == 'POST':
        m=str(request.form.get('mat1'))
        q=str(request.form.get('quant'))
        id2=str(request.form.get('id2'))
       
        sql="insert into prod_mat set "
        sql=sql+"idp='"+id2+"',"
        sql=sql+"idm='"+m+"',"
        sql=sql+"quant='"+q+"'"
        
        print(sql)
        try:
            
            mycursor.execute(sql)
            mydb.commit()
            error=0
        except:
            error=1
        
       
    return jsonify({"err": error})


@app.route("/products")
def products():
    if(session.get("u")!=None):
        return render_template('products.html', menu="admin")
    else:
        return render_template('index.html', menu="")
        
        

        

@app.route("/getproducts")
def getproducts():
    sql="select * from products"
  
    mycursor.execute(sql)
    r=mycursor.fetchall()
    return jsonify(r)
    
    
@app.route("/getprdmat/<id>")
def getprdmat(id):

    sql="select * from materials,prod_mat where prod_mat.idm=materials.id and prod_mat.idp="+str(id)
  
    mycursor.execute(sql)
    r=mycursor.fetchall()
    return jsonify(r)



@app.route("/delprdmat/<id>")
def delprdmat(id):

    sql="delete from prod_mat where id="+str(id)
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
    return jsonify({"err": 0})
    
@app.route("/getproduct/<id>")
def getproduct(id):
    sql="select * from products where id="+str(id)
   
    mycursor.execute(sql)
    r=mycursor.fetchone()
    return jsonify(r)
    

@app.route("/updateprd", methods=['POST', 'GET'])
def updateprd():
   if request.method == 'POST':
        id1=str(request.form.get('id1'))
        e=str(request.form.get('ptitle1'))
        p=str(request.form.get('pdescr1'))  
        sv=str(request.form.get('sv'))   
        print(sv)
        if sv=="0": 
        	sql="update products set title='"+e+"', descr='"+p+"' where id='"+id1+"'"
        	
        if sv=="1": 
        	sql="delete from products where id='"+id1+"'"
        
        
        print(sql)
        try:
            mycursor.execute(sql)
            mydb.commit()
            
            error=0
        except:
            error=1
    
   return jsonify({"err": error})



#sales 
    
@app.route("/getsales")
def getsales():
    sql="select * from sales, products where products.id=sales.idp order by dates desc "
   
    mycursor.execute(sql)
    r=mycursor.fetchall()
    return jsonify(r)

@app.route("/newsale", methods=['POST', 'GET'])
def newsale():
    if request.method == 'POST':
        p=str(request.form.get('prod'))
        q=str(request.form.get('qnt'))
        dd=str(request.form.get('dt'))
        sql="insert into sales set "
        sql=sql+"idp='"+p+"',"
        sql=sql+"dates='"+dd+"',"
        sql=sql+"qnt='"+q+"'"
        
        print(sql)
        try:
            
            mycursor.execute(sql)
            mydb.commit()
            error=0
        except:
            error=1
        
       
    return jsonify({"err": error})



#orders 
    
@app.route("/getorders")
def getorders():
    sql="select * from orders, materials where materials.id=orders.idm order by date desc "
   
    mycursor.execute(sql)
    r=mycursor.fetchall()
    return jsonify(r)

@app.route("/neworder", methods=['POST', 'GET'])
def neworder():
    if request.method == 'POST':
        p=str(request.form.get('prod'))
        q=str(request.form.get('qnt'))
        dd=str(request.form.get('dt'))
        sql="insert into orders set "
        sql=sql+"idm='"+p+"',"
        sql=sql+"date='"+dd+"',"
        sql=sql+"qnty='"+q+"'"
        
        print(sql)
        try:
            
            mycursor.execute(sql)
            mydb.commit()
            error=0
        except:
            error=1
        
       
    return jsonify({"err": error})



#api
app.run(debug=True,threaded=True,port=8081, host='135.181.44.190')

    



