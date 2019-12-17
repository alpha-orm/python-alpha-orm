from .DriverInterface import DriverInterface
from ..query_builders.MySQLQueryBuilder import MySQLQueryBuilder
from interface import implements
import pymysql.cursors
from ..utilities.constants import *
from ..utilities.functions import *
from ..AlphaRecord import AlphaRecord
from ..AlphaORM import AlphaORM
from ..generators.MySQLGenerator import MySQLGenerator


class MySQLDriver(implements(DriverInterface)):

    REQUIRED_OPTIONS = ['host', 'user', 'password', 'database']

    @staticmethod
    def connect(options):
        MySQLDriver.con = pymysql.connect(host=options['host'], user=options['user'], password=options[
                                          'password'], db=options['database'], charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        MySQLDriver.db = MySQLDriver.con.cursor()
        return MySQLDriver.db

    @staticmethod
    def query(sql, return_val=False):
        MySQLDriver.connect(AlphaORM.OPTIONS)
        MySQLDriver.db.execute(sql)
        MySQLDriver.con.commit()
        lastInsert = 0
        if return_val:
            retval = MySQLDriver.db.fetchall()
            lastInsert = MySQLDriver.db.lastrowid
        else:
            retval = None
        MySQLDriver.db.close()
        return retval, lastInsert

    @staticmethod
    def createTable(tablename):
        return MySQLDriver.query(MySQLQueryBuilder.createTable(tablename), True)

    @staticmethod
    def getAll(tablename):
        rows, _ = MySQLDriver.query(
            MySQLQueryBuilder.getAllRecords(tablename), True)
        return AlphaRecord.create(tablename, rows)

    @staticmethod
    def insertRecord(tablename, alpha_record):
        return MySQLDriver.query(MySQLQueryBuilder.insertRecord(tablename, alpha_record), True)

    @staticmethod
    def updateRecord(alpha_record):
        for col in getProperties(alpha_record):
            if isinstance(getattr(alpha_record, col), AlphaRecord):
                setattr(alpha_record, col, MySQLDriver.updateRecord(
                    getattr(alpha_record, col)))
        update = MySQLDriver.query(MySQLQueryBuilder.updateRecord(
            alpha_record.getTableName(), alpha_record, alpha_record.getID()))
        return alpha_record

    @staticmethod
    def getColumns(tablename):
        retval, _ = MySQLDriver.query(
            MySQLQueryBuilder.getColumns(tablename), True)
        return retval

    @staticmethod
    def updateColumns(tablename, updated_columns):
        MySQLDriver.query(MySQLQueryBuilder.updateColumns(
            tablename, updated_columns))

    @staticmethod
    def createColumns(tablename, new_columns):
        MySQLDriver.query(
            MySQLQueryBuilder.createColumns(tablename, new_columns))

    @staticmethod
    def find(tablename, where, dict_map):
        columns_db = MySQLDriver.getColumns(tablename)
        updated_columns, new_columns = MySQLGenerator.columns(
            columns_db, dict_map)
        if updated_columns:
            MySQLDriver.updateColumns(tablename, updated_columns)
        if new_columns:
            MySQLDriver.createColumns(tablename, new_columns)

        row, _ = MySQLDriver.query(MySQLQueryBuilder.find(
            True, tablename, where, dict_map), True)
        if len(row) == 0:
            raise RuntimeError('No record found for corresponding query')
        return AlphaRecord.create(tablename, row, True)

    @staticmethod
    def findAll(tablename, where, dict_map):
        columns_db = MySQLDriver.getColumns(tablename)
        updated_columns, new_columns = MySQLGenerator.columns(
            columns_db, dict_map)
        if updated_columns:
            MySQLDriver.updateColumns(
                tablename, updated_columns)
        if new_columns:
            MySQLDriver.createColumns(
                tablename, new_columns)

        rows, _ = MySQLDriver.query(MySQLQueryBuilder.find(
            False, tablename, where, dict_map), True)
        return AlphaRecord.create(tablename, rows)

    @staticmethod
    def store(alpha_record, base=True):
        try:
            for a in getProperties(alpha_record):
                if isinstance(getattr(alpha_record, a), AlphaRecord):
                    setattr(alpha_record, getattr(alpha_record, a).getTableName(
                    ), MySQLDriver.store(getattr(alpha_record, a), False))
                    if getattr(alpha_record, a).getTableName() != a:
                        delattr(alpha_record, a)

            columns_db = MySQLDriver.getColumns(alpha_record.getTableName())
            updated_columns, new_columns = MySQLGenerator.columns(
                columns_db, alpha_record)
            if updated_columns:
                MySQLDriver.updateColumns(
                    alpha_record.getTableName(), updated_columns)

            if new_columns:
                MySQLDriver.createColumns(
                    alpha_record.getTableName(), new_columns)

            if alpha_record.getID() != None:
                for col in getProperties(alpha_record):
                    if isinstance(getattr(alpha_record, col), AlphaRecord):
                        setattr(alpha_record, col, MySQLDriver.store(
                            getattr(alpha_record, col)))
                    return MySQLDriver.updateRecord(alpha_record)

            retval, last = MySQLDriver.insertRecord(
                alpha_record.getTableName(), alpha_record)
            alpha_record.setID(last)
            return alpha_record
        except Exception as e:
            raise e

    @staticmethod
    def drop(alpha_record):
        try:
            if alpha_record.getID() == None:
                raise RuntimeError(
                    'MySQLDriver Record has not been stored yet!')
            MySQLDriver.query(MySQLQueryBuilder.deleteRecord(alpha_record))
            alpha_record.deleteID()
        except Exception as e:
            raise e

    @staticmethod
    def dropAll(tablename):
        return MySQLDriver.query(MySQLQueryBuilder.deleteAllRecords(tablename))

    @staticmethod
    def getDriver(driver):
        pass
