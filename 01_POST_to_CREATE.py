from bottle import route, run, request, redirect

# simple list of books we can offer
books = ['Lord of the Webdev', 
  'HitchHiker\'s Guide to Webdev', 
  'Webdev: the Good Parts']
pizza_counter = 0


@route('/')
@route('/books')
def index():
  """The index page should show all the books, also accessible through /books"""
  return ', '.join(books)

@route('/books/<book_id>')
def get_item(book_id):
  """this page should show information about a single book"""
  return "You requested the page for the book: %s" % book_id

@route('/books', method='POST')
def add_item():
  book_title = request.forms.get('title')
  books.append(book_title)
  redirect('/books')

run(host='localhost', port=8080)
