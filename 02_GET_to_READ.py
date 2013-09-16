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
    print(id, book)
    books_list = books_list + '<li><a href="/books/%i">%s</a></li>' % (id, book)
  books_list = books_list + '</ul>'

  form = '''<form action="/books" method="POST">
    <input type="text" name="title" />
    <br />
    <input type="submit" value="add book" />
  </form>'''
  return books_list + form


@route('/books/<book_id:int>')
def get_item(book_id):
  """this page should show information about a single book"""
  if book_id < len(books):
    return "You requested the page for the book: %s" % books[book_id]
  abort(404)


@route('/books', method='POST')
def add_item():
  book_title = request.forms.get('title')
  books.append(book_title)
  redirect('/books')

run(host='localhost', port=8080)
