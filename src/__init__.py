from alphaorm.AlphaORM import AlphaORM,AlphaRecord

AlphaORM.setup('mysql', {
	'host' : 'localhost',
	'user' : 'root',
	'password' : '',
	'database' : 'alphaorm'
})

m = AlphaORM.create('python')
m.name = 'Alpha'
m.age = 10
AlphaORM.store(m)