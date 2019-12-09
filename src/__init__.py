from alphaorm.AlphaORM import AlphaORM as DB

DB.setup('mysql', {
	'host' : 'localhost',
	'user' : 'root',
	'password' : '',
	'database' : 'alphaorm'
})

# author = DB.create('author')
# author.name = 'Chimamanda Adichie'

# book = DB.create('book')
# book.title = 'Purple Hibiscus'
# book.author = author

# DB.store(book)


# book = DB.find('book','id = :tid', { 'tid' : 1 })
# print(book.author)

# books = DB.getAll('book')
# print(books[0].title)

book = DB.find('book','id = :tid', { 'tid' : 1 })
book.title = 'Alpha'
book.author.name = 'Bravo'
DB.store(book)
print(book)