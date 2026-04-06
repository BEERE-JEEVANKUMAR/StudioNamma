from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = []

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET','POST'])
def add_book():
    if request.method == 'POST':
        book_name = request.form['book']
        books.append(book_name)
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/borrow/<book>')
def borrow(book):
    if book in books:
        books.remove(book)
    return redirect(url_for('index'))

@app.route('/return', methods=['POST'])
def return_book():
    book = request.form['book']
    books.append(book)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)