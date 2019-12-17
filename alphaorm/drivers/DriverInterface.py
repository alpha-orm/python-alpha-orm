import interface
from ..generators.GeneratorInterface import GeneratorInterface


class DriverInterface(interface.Interface):

    @staticmethod
    def connect(options):
        pass

    @staticmethod
    def query(sql, return_val=False):
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
    def createColumnsForFind(tablename, where):
	    alpha_record = AlphaORM.create(tablename)
	    columns = re.findall(r'(\w+\s*)(=|!=|>|<|>=|<=)', where)
	    for column in columns:
	        setattr(alpha_record, column[0].strip(), False)

	    columns_db = DriverInterface.getDriver(
	        AlphaORM.DRIVER).getColumns(tablename)
	    _, new_columns = GeneratorInterface.getGenerator(AlphaORM.DRIVER).columns(
	        columns_db, alpha_record)

	    if new_columns:
	        DriverInterface.getDriver(AlphaORM.DRIVER).createColumns(
	            tablename, new_columns)

    @staticmethod
    def find(tablename, where, dict_map):
        pass

    @staticmethod
    def findAll(tablename, where, dict_map):
        pass

    @staticmethod
    def store(alpha_record, base=True):
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
