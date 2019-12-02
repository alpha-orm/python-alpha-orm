import interface

class QueryBuilderInterface(interface.Interface):

    @staticmethod
    def createTable(tablename):
        pass

    @staticmethod
    def createColumns(tablename, dict_map):
        pass

    @staticmethod
    def getColumns(tablename):
        pass

    @staticmethod
    def updateColumns(tablename, dict_map):
        pass

    @staticmethod
    def getAllRecords(tablename):
        pass

    @staticmethod
    def insertRecord(tablename, dict_map):
        pass

    @staticmethod
    def updateRecord(tablename, dict_map, id):
        pass

    @staticmethod
    def deleteRecord(alpha_record):
        pass

    @staticmethod
    def find(single, tablename, where, dict_map = []):
        pass

    @staticmethod
    def getQueryBuilder(driver):
        driver = driver.lower()
        if driver ==  'mysql':
            from .MySQLQueryBuilder import MySQLQueryBuilder
            return MySQLQueryBuilder
        
    
