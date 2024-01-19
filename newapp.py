from flask import Flask,request,jsonify
import sqlite3
app=Flask(__name__)

#connectin to database
def db_connection():
    conn=None
    try:
        conn=sqlite3.connect("books.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn

'''
#using an in-memory list of books for first method


books_list=[
    {"id":0,
     "title":'Mama mIa',
     "language":"English"
    },
    {"id":1,
     "title":'Godfather',
     "language":"English"
    },
    {"id":2,
     "title":'Dracula', 
     "language":"Malayalam"
    },
]

'''
 #defining an API to return the list of books=> we use GET Request.
 
 
# @app.route("/books",methods=['GET','POST'])   #this api accepts both read and write operations
# def books():
#     if request.method=='GET':# to view books    
#         if len(books_list)>0:
#             return jsonify(books_list)
#         else:
#             'Sorry! No Records Found,404'
#     if request.method=="POST":
#         new_Title=request.form['title']   #requesting new title and new langauge from the post request
#         new_Lang=request.form['language']
#         iD=books_list[-1]['id']+1
#     new_obj={
#         "id":iD,
#         "title":new_Title,
#         "language":new_Lang   #creation of a new object with the new values
#     }
    
#     books_list.append(new_obj)  #appending the new obj to the in memory list
    
#     return jsonify(books_list),201





# @app.route("/books/<int:id>",methods=['GET','PUT','DELETE'])
# def get_single_book(id):
#     if request.method=='GET':
#         for book in books_list:
#             if book['id']==id:
#                 return jsonify(book)
#             else:
#                 pass
#     if request.method=="PUT":
#         for book in books_list:
#             if book['id']==id:
#                   book['title']=request.form['title']   #requesting new title and new langauge from the post request
#                   book['language']=request.form['language']
#                   updated_book={
#                     "id":id,
#                     "title":book['title'],
#                     "language":book["language"]
#                 }
#                   return jsonify(updated_book)
                
                
'''
important note: 
in this case the added book does not reflect in the inmemory list
it only is avaialable for runtime.
we use databases for data persistance.

'''
#updated function using DB

@app.route("/books", methods=["GET", "POST"])
def books():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM book")
        books = [
            dict(id=row[0], author=row[1], language=row[2], title=row[3])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)
    if request.method == "POST":
        new_author = request.form["author"]
        new_lang = request.form["language"]
        new_title = request.form["title"]
        sql = """INSERT INTO book (author, language, title)
                 VALUES (?, ?, ?)"""
        cursor = cursor.execute(sql, (new_author, new_lang, new_title))
        conn.commit()
        return f"Book with the id: 0 created successfully", 201
    
@app.route("/books/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    book = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM book WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is not None:
            return jsonify(book), 200
        else:
            return "Something wrong", 404

    if request.method == "PUT":
        sql = """UPDATE book
                SET title=?,
                    author=?,
                    language=?
                WHERE id=? """

        author = request.form["author"]
        language = request.form["language"]
        title = request.form["title"]
        updated_book = {
            "id": id,
            "author": author,
            "language": language,
            "title": title,
        }
        conn.execute(sql, (author, language, title, id))
        conn.commit()
        return jsonify(updated_book)

    if request.method == "DELETE":
        sql = """ DELETE FROM book WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "The book with id: {} has been ddeleted.".format(id), 200


if __name__=='__main__':
    app.run(debug=True)
    
        
    
 
     

