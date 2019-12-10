from alphaorm.AlphaORM import AlphaORM as DB

DB.setup('mysql', {
	'host' : 'localhost',
	'user' : 'root',
	'password' : '',
	'database' : 'alphaorm'
})

#--------------------------------------
#	CREATE 1
#--------------------------------------
# product = DB.create('product')
# product.name = 'Running shoes'
# product.price = 5000
# DB.store(product)




#--------------------------------------
#	CREATE 2
#--------------------------------------
# author = DB.create('author')
# author.name = 'Chimamanda Adichie'

# book = DB.create('book')
# book.title = 'Purple Hibiscus'
# book.author = author
# DB.store(book)




#--------------------------------------
#	READ 1 [get all records]
#--------------------------------------
# books = DB.getAll('book')
# for book in books:
# 	print(book)




#--------------------------------------
#	READ 1 [filter one]
#--------------------------------------
# book = DB.find('book','id = :bid', { 'bid' : 1 })
# print(book)




#--------------------------------------
#	READ 1 [filter all]
#--------------------------------------
# books = DB.findAll('book','author_id = :aid', { 'aid' : 1 })
# for book in books:
# 	print(book.title)




#--------------------------------------
#	UPDATE
#--------------------------------------
# book = DB.find('book','id = :bid', { 'bid' : 1 })
# book.author.name = 'New author'
# book.author.hee = 'haha'
# book.title = 'New Title'
# DB.store(book)
# print(book)




#--------------------------------------
#	DELETE 1 [delete single record]
#--------------------------------------
# book = DB.find('book','id = :bid', { 'bid' : 1 })
# DB.drop(book)
# print(book)




#--------------------------------------
#	DELETE 2 [delete all records]
#--------------------------------------
# DB.dropAll('book')