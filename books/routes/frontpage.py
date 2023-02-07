# main page
# displays all books
from flask import Blueprint, render_template
bp = Blueprint('index', __name__)
@bp.route('/', methods=['GET', 'POST'])
def index():
    # books = Book.query.all()
    books = [
        {
            "title" : "Cat in the Hat",
            "author" : "Dr. Seuss",
            "rating" : "4.5",
            "description" : "a cat causes some trouble for some kids. also, the cat wears a hat."
        },
                {
            "title" : "Cat in the Hat",
            "author" : "Dr. Seuss",
            "rating" : "4.5",
            "description" : "a cat causes some trouble for some kids. also, the cat wears a hat."
        }
    ]
    return render_template('books.html', title='Home', books=books)