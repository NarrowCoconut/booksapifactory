# admin page
# has a form for adding, removing, and editing books
@bp.route('/admin', methods=['GET', 'POST'])
def admin():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data, description=form.description.data, rating=form.rating.data, image=form.image.data, url=form.url.data)
        db.session.add(book)
        db.session.commit()
        flash('Book added!')
        return redirect(url_for('books.admin'))
    return render_template('admin.html', title='Admin', form=form)