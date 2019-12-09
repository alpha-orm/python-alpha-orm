from .utilities.constants import *
from .utilities.functions import *

class AlphaRecord():

    def setID(self,t_id):
        self.__id = t_id

    def deleteID(self):
        self.__id = None

    def getID(self):
        return self.__id

    def getTableName(self):
        return self.__tablename

    def __init__(self, tablename, t_id = None):
        self.__tablename = tablename
        self.__id = t_id
    
    @staticmethod
    def create(tablename, rows, single = False):
        dict_map = getTableMap(tablename)
        records = []
        for row in rows:
            record = AlphaRecord(tablename, row['id'])
            del row['id']
            for column in list(row.keys()):
                if column.endswith('_id'):
                    table = column.replace('_id', '')
                    from .AlphaORM import AlphaORM
                    setattr(record, table, AlphaRecord.handleEmbedding(AlphaORM.DRIVER, table, row[column]))
                    continue
                data = dict_map[column].startswith(QueryBuilder.getQueryBuilder(AlphaORM.DRIVER.DATA_TYPE['bool'])) if (row[column] == 1) else row[column]
                setattr(record,column,data)
            records.append(record)
        return records[0] if single else records
    
    @staticmethod
    def handleEmbedding(driver, tablename, t_id): 
        from .AlphaORM import AlphaORM
        return AlphaORM.find(tablename, 'id = :id', { 'id' : t_id })

    def __str__(self):
        return f'<AlphaRecord _tablename : {self.getTableName()}, _id : {self.getID()}>'