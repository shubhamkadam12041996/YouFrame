import sqlite3 
con = sqlite3.connect("product.db")  
print("Database opened successfully")  
con.execute("create table product (TID INTEGER PRIMARY KEY AUTOINCREMENT, imgname TEXT NOT NULL, ImgURL TEXT NOT NULL,imgDate DATETIME DEFAULT CURRENT_TIMESTAMP)") 
print("Table created successfully")   
con.close()