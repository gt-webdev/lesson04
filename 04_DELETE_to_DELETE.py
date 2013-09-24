from bottle import route, run, request, redirect, abort

# simple list of books we can offer
books = ['Lord of the Webdev', 
  'HitchHiker\'s Guide to Webdev', 
  'Webdev: the Good Parts']
pizza_counter = 0


@route('/')
@route('/books')
def index():
  """The index page should show all the books, also accessible through /books"""
  books_list = '<ul>'
  for id, book in enumerate(books):
    books_list = books_list + '<li><a href="/books/%i">%s</a></li>' % (id, book)
  books_list = books_list + '</ul>'

  form = '''<form action="/books" method="POST">
    <input type="text" name="title" />
    <br />
    <input type="submit" value="add book" />
  </form>
  <form action="/delete/books" method="GET">
    <input type="submit" value="Clear List" />
  </form>
  '''
  return books_list + form


@route('/books/<book_id:int>')
def get_item(book_id):
  """this page should show information about a single book"""
  if book_id < len(books):
    form = '''<form action="/put/books/%i" method="POST">
      <input type="text" name="title" />
      <br />
      <input type="submit" value="edit book" />
      </form>
      <form action="/delete/books/%i" method="GET">
        <input type="submit" value="delete book" />
      </form>
      ''' % (book_id, book_id)
    message = "<p>You requested the page for the book: %s</p>" % books[book_id]
    return message + form
  abort(404)


@route('/books', method='POST')
def add_item():
  """this function handles adding a new book to the list"""
  book_title = request.forms.get('title')
  books.append(book_title)
  redirect('/books')


@route('/put/books/<book_id:int>', method="POST") #dirty workaround 
def update_book(book_id):
  """this function handles updating the title of an existing book"""
  if book_id < len(books):
    book_title = request.forms.get('title')
    books[book_id] = book_title
    redirect('/books/%i' % book_id)
  abort(404)


@route('/delete/books/<book_id:int>')
def delete_book(book_id):
  """This function handles deleting a book from the list"""
  if book_id < len(books):
    del books[book_id]
    redirect('/books')
  abort(404)


@route('/delete/books')
@route('/delete')
def delete_all():
  global books
  books = []
  redirect('/books')


run(host='localhost', port=8080)
