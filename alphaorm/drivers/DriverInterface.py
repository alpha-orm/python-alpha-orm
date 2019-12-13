import interface

class DriverInterface(interface.Interface):

	@staticmethod
	def connect(options):
		pass

	@staticmethod
	def query(sql,return_val=False):
		pass

	@staticmethod
	def createTable(tablename):
		pass

	@staticmethod
	def getAll(tablename):
		pass

	@staticmethod
	def insertRecord(tablename, alpha_record):
		pass

	@staticmethod
	def updateRecord(alpha_record):
		pass

	@staticmethod
	def getColumns(tablename):
		pass

	@staticmethod
	def updateColumns(tablename, updated_columns):
		pass

	@staticmethod
	def createColumns(tablename, new_columns):
		pass

	@staticmethod
	def find(tablename, where, dict_map):
		pass

	@staticmethod
	def findAll(tablename, where, dict_map):
		pass

	@staticmethod
	def store(alpha_record, base = True):
		pass

	@staticmethod
	def drop(alpha_record):
		pass

	@staticmethod
	def dropAll(tablename):
		pass

	@staticmethod
	def getDriver(driver):
		if driver == 'mysql':
			from .MySQLDriver import MySQLDriver
			return MySQLDriver
