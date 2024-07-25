from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
]

@app.route("/books", methods=["GET"])
def get_books():
    # add code here

@app.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    for book in books:
        if book["id"] == id:
            # add code here
    return jsonify({})

@app.route("/books", methods=["POST"])
def add_book():
    if request.method == "POST":
        # add code here
    return render_template("books.html", books=books)

@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    if request.method == "PUT":
        target = request.json
        # add code here
    return jsonify({})

@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    response = {}
    # add code here
    return jsonify({})

@app.route("/", methods=["GET"])
def view_books():
   # add code here



if __name__ == "__main__":
    app.run(debug=True)
