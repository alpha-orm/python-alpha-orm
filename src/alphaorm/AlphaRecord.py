from .utilities.constants import *
from .utilities.functions import *

class AlphaRecord():

    def setID(self,t_id):
        self.__id = t_id;

    def deleteID(self):
        self.__id = None;

    def getID(self):
        return self.__id;

    def getTableName(self):
        return self.__tablename;

    def __init__(self, tablename, t_id = None):
        self.__tablename = tablename;
        self.__id = t_id;

    # @staticmethod
    # def create(tablename, rows, single = False):
    #     let records = []
    #     for  row in rows :
    #         record = AlphaRecord(tablename)
    #         columns = getProperties(row)
    #         for column in columns:
    #             if (column.endsWith('_id')):
    #                 table = column.replace('_id', '')
    #                 record[table] = self.handleEmbedding(AlphaORM.DRIVER, table, row[column])
    #                 continue
    #             record[column] = row[column]
    #         record._id = row.id
    #         records.append(record)
    #     return single ? records[0] : records
    