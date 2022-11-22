# main page
# displays all books
@bp.route('/', methods=['GET', 'POST'])
def index():
    books = Book.query.all()
    return render_template('index.html', title='Home', books=books)