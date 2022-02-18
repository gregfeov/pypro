import http
import socket
import socketserver
import http.server
from mysql.connector import connect, Error
import hashlib
import qrcode
import time
import random
import requests
import io
from PIL import Image
import numpy as np



def h256(a):
    b=bytes(a, 'utf-8')
    c=hashlib.sha256(b).hexdigest()
    return c
def h512(a):
    b=bytes(a, 'utf-8')
    c=hashlib.sha512(b).hexdigest()
    return c
def md5(a):
    b=bytes(a,'utf-8')
    c=hashlib.md5(b).hexdigest()
    return c
def r(a,b):
    n=random.randint(a,b)
    return n
def rmd5():
    text=rh()
    a=md5(text)
    return a
def rh():
    a=r(0,1000)
    b=r(0,1000)
    c=r(0,1000)
    d=r(0,1000)
    e=str(a)+"."+str(b)+"."+str(c)+"."+str(d)
    f=h256(e)   
    return f
def createuser():
    try:
        with connect(
            host="localhost",
            user="root",
            password="93029302",
        ) as connection:
            a=rh()
            if connection.is_connected():
                print("Connected to database")
            time.sleep(1)
            print(a)
            with connection.cursor() as cursor:
                cursor.execute("USE gfpdb")
            
                cursor.execute("SELECT address FROM tt WHERE address='"+a+"'")
                row = cursor.fetchone()
                if row==None:
                    cursor.execute("INSERT INTO tt(address,balance,password) VALUES('"+a+"','"+str(1000000)+"','"+rmd5()+"')")
                    connection.commit()
                    print("Token created successfully with start balance 100")
                    return a
                else:
                    print("Token is alredy created!")
    except Error as e:
        print(e)
def getaddressfromid(a):
    try:
        with connect(
            host="localhost",
            user="root",
            password="93029302",
        ) as connection:
            if connection.is_connected():
                print("Connected to database")
            time.sleep(1)
            with connection.cursor() as cursor:
                cursor.execute("USE gfpdb")
                cursor.execute("SELECT address FROM tt WHERE id='"+str(a)+"'")
                row = cursor.fetchone()
                if row==None:
                    return None
                else:
                    print(row)
                    return row
    except Error as e:
        print(e)
def makeqr(data,fn):
    img_name = "C:\\users\\greg\\desktop\\"+fn
    img = qrcode.make(data) #generate QRcode
    img.save(img_name)
    print(data)
def delchar(a):
    d="(),\'\'"
    for char in d:
        a = a.replace(char,"")
    return a
def tgtoken():
    a = '5007275392:AAEwq9Edce2P6try6rqu4uSWKvr77M21XZs'
    return a
def transaction(sa,ra,sume):
    try:
        with connect(
            host="localhost",
            user="root",
            password="93029302",
        ) as connection:
            a=rh()
            if connection.is_connected():
                print("Connected to database")
            time.sleep(1)
            s=int(0)-int(sume)
            print(s)
            with connection.cursor() as cursor:
                cursor.execute("USE gfpdb")
                cursor.execute("UPDATE tt set balance = '"+str(1)+"' WHERE address = '"+str(sa)+"'")
                cursor.execute("UPDATE tt set balance = '"+str(2)+"' WHERE address = '"+str(ra)+"'")
                connection.commit()
    except Error as e:
        print(e)
def getbalance(a):
    try:
        with connect(
            host="localhost",
            user="root",
            password="93029302",
        ) as connection:
            if connection.is_connected():
                print("Connected to database")
            time.sleep(1)
            with connection.cursor() as cursor:
                cursor.execute("USE gfpdb")
                cursor.execute("SELECT balance FROM tt WHERE id='"+str(a)+"'")
                row = cursor.fetchone()
                if row==None:
                    return None
                else:
                    print(row)
                    return row
    except Error as e:
        print(e)
def getpassword(a):
    try:
        with connect(
            host="localhost",
            user="root",
            password="93029302",
        ) as connection:
            if connection.is_connected():
                print("Connected to database")
            time.sleep(1)
            with connection.cursor() as cursor:
                cursor.execute("USE gfpdb")
                cursor.execute("SELECT password FROM tt WHERE address='"+str(a)+"'")
                row = cursor.fetchone()
                if row==None:
                    return None
                else:
                    print(row)
                    return delchar(str(row))
    except Error as e:
        print(e)
def ws(port=9000):

    class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.path = 'index.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

    Handler = MyHttpRequestHandler
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("Server started on port ", port)
        print("http:\\\\"+socket.gethostbyname(socket.gethostname())+":"+str(port))
        httpd.serve_forever()
def ge(inw):
    try:
        url = 'https://api.kraken.com/0/public/Ticker?pair=' + inw
        response = requests.get(url)
        a = response.json()
        b = a['result']
        c = b[inw]
        d = c['a']
        pr = d[0]
        return pr
    except:
        return "Unknown ticker"