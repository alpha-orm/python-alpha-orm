from ..utilities.constants import *
from ..utilities.functions import *
from ..query_builders.MySQLQueryBuilder import MySQLQueryBuilder
from ..AlphaRecord import AlphaRecord
from ..AlphaORM import AlphaORM

class MySQLGenerator ():

    @staticmethod
    def checkColumnUpdates(columns_db, columns_record, alpha_record):
        updated_columns = {}
        existing = []
        print(columns_db)
        for col in columns_db:
            if col['Field'] in columns_record:
                existing.append(col['Field'])
                if col['Field'] != 'id' and ((col['Type'].startswith(MySQLQueryBuilder.DATA_TYPE[get_type(getattr(alpha_record,col['Field']))])) == False):
                    if col['Field'] in AlphaORM.DATA_TYPES:
                        pass
                    elif col['Type'].startswith(MySQLQueryBuilder.DATA_TYPE['int']) and (get_type(getattr(alpha_record,col['Field'])) != 'bool'):
                        updated_columns[col['Field']] = MySQLQueryBuilder.DATA_TYPE[get_type(getattr(alpha_record,col['Field']))]
                    elif col['Type'].startswith(MySQLQueryBuilder.DATA_TYPE['bool']) & (get_type(getattr(alpha_record,col['Field'])) != 'bool'):
                        if get_type(getattr(alpha_record,col['Field'])) not in ['int', 'float'] :
                            updated_columns[col['Field']] = MySQLQueryBuilder.DATA_TYPE[get_type(getattr(alpha_record,col['Field']))]
                        else:
                            updated_columns[col['Field']] = MySQLQueryBuilder.DATA_TYPE['str']
        return updated_columns, existing 

    @staticmethod
    def creatNewColumns(dict_map, alpha_record, tablename):
        new_columns = {}
        for col in dict_map:
            if col == '__tablename':
                continue
            if isinstance(col, AlphaRecord):
                MySQLGenerator.columns(col.getTableName(),col)
            elif get_type(col) not in AlphaORM.DATA_TYPES:
                raise RuntimeError('Values can only be number, string or boolean')
            else:
                if isinstance(getattr(alpha_record, col),AlphaRecord):
                    key = f'{getattr(alpha_record, col).getTableName()}_id'
                    new_columns[key] = MySQLQueryBuilder.DATA_TYPE['int']
                else:
                    new_columns[col] = MySQLQueryBuilder.DATA_TYPE[get_type(getattr(alpha_record,col))]
        return new_columns

    @staticmethod
    def columns(columns_db, alpha_record, base = True):
        columns_record = getProperties(alpha_record)
        updated_columns, existing = MySQLGenerator.checkColumnUpdates(columns_db, columns_record, alpha_record)
        diff_array = array_diff(columns_record, existing)
        new_columns = MySQLGenerator.creatNewColumns(diff_array, alpha_record, alpha_record.getTableName())
        return updated_columns, new_columns