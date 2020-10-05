from flask import *
import sqlite3
import os
app = Flask(__name__,static_url_path = "", static_folder = "")
@app.route("/")
def index():
    con = sqlite3.connect("product.db")
    con.row_factory = sqlite3.Row
    result = con.cursor()
    result.execute("select * from product")
    rows = result.fetchall()
    return render_template("index.html", rows=rows)


@app.route('/savedetails',methods = ["POST","GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.files['file'].filename
            print(name)
            imagepath = request.files['file']
            with sqlite3.connect("product.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into product (imgname,ImgURL) values (?,?)", (name, name))
                con.commit()
                msg = "Image Save successfully"
                imagepath.save(imagepath.filename)

        except:
            con.rollback()
            msg = "We can not add the product to the list"
        finally:
            con = sqlite3.connect("product.db")
            con.row_factory = sqlite3.Row
            result = con.cursor()
            result.execute("select * from product")
            rows = result.fetchall()
            print("hi")
            return render_template("index.html", msg=msg, rows=rows)
            con.close()


if __name__ == "__main__":
    app.run(debug=True)

