from alphaorm.AlphaORM import AlphaORM as DB

'''
Implemented for:
-mysql [completed]
-sqlite [undone]
-postgres [undone]
-sqlserver [undone]
'''

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
	# print(f'{book.title} by {book.author.name}')




#--------------------------------------
#	READ 2 [filter one]
#--------------------------------------
# book = DB.find('book','id = :bid', { 'bid' : 1 })
# print(f'{book.title} by {book.author.name}')




#--------------------------------------
#	READ 3 [filter all]
#--------------------------------------
# author = DB.find('author','name = :author_name',{ 'author_name': 'William Shakespare' })
# booksByShakespare = DB.findAll('book', 'author_id : a_id', { 'a_id': author.getID() })
# print('Books by William Shakespare are :')
# for book in booksByShakespare:
# 	print(book.title)



#--------------------------------------
#	UPDATE
#--------------------------------------
# product = DB.find('shop_product', 'id = :pid', { pid: 1 })
# product.price = 500

# book = DB.find('book','id = :bid', { 'bid' : 1 })
# book.author.name = 'New author'
# book.author.isbn = '3847302-SD'
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