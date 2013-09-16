from bottle import route, run

# simple list of books we can offer
books = ['Lord of the Webdev', 
  'HitchHiker\'s Guide to Webdev', 
  'Webdev: the Good Parts']
pizza_counter = 0


@route('/')
@route('/books')
def index():
  """The index page should show all the books, also accessible through /books"""
  return "This is where I show all the books I have!"

@route('/books/<book_id>')
def add_item(book_id):
  """this page should show information about a single book"""
  return "You requested the page for the book: %s" % book_id

run(host='localhost', port=8080)
