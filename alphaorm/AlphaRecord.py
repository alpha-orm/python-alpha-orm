from .utilities.constants import *
from .utilities.functions import *
from .query_builders.QueryBuilderInterface import QueryBuilderInterface


class AlphaRecord():

    def setID(self, t_id):
        self.__id = t_id

    def deleteID(self):
        self.__id = None

    def getID(self):
        return self.__id

    def getTableName(self):
        return self.__tablename

    def __init__(self, tablename, t_id=None):
        self.__tablename = tablename
        self.__id = t_id

    @staticmethod
    def create(tablename, rows, single=False):
        dict_map = getTableMap(tablename)
        records = []
        for row in rows:
            record = AlphaRecord(tablename, row['id'])
            del row['id']
            for column in list(row.keys()):
                from .AlphaORM import AlphaORM
                if column.endswith('_id'):
                    table = column.replace('_id', '')
                    setattr(record, table, AlphaRecord.handleEmbedding(
                        AlphaORM.DRIVER, table, row[column]))
                    continue
                data =  (row[column] == 1)  if dict_map[column].startswith(QueryBuilderInterface.getQueryBuilder(
                    AlphaORM.DRIVER).DATA_TYPE['bool']) else row[column]
                setattr(record, column, data)
            records.append(record)
        return records[0] if single else records

    @staticmethod
    def handleEmbedding(driver, tablename, t_id):
        from .AlphaORM import AlphaORM
        return AlphaORM.find(tablename, 'id = :id', {'id': t_id})

    def __str__(self):
        return f'<AlphaRecord _tablename : {self.getTableName()}, _id : {self.getID()}>'
