from .drivers.DriverInterface import DriverInterface
from .AlphaRecord import AlphaRecord
from .utilities.constants import *
from .utilities.functions import *
import warnings
warnings.filterwarnings("ignore")


class AlphaORM():
    DATA_TYPES = ['float', 'str', 'bool', 'int']

    @staticmethod
    def setup(driver, options):
        AlphaORM.DRIVER = driver
        AlphaORM.OPTIONS = options
        missing = array_diff(DriverInterface.getDriver(
            driver).REQUIRED_OPTIONS, list(options.keys()))
        if len(missing):
            raise RuntimeError(SETUP_PARAMETER_MISSING(missing[0]))
        return DriverInterface.getDriver(AlphaORM.DRIVER).connect(AlphaORM.OPTIONS)

    @staticmethod
    def create(tablename):
        DriverInterface.getDriver(AlphaORM.DRIVER).createTable(tablename)
        return AlphaRecord(tablename)

    @staticmethod
    def store(alpha_record):
        if len(getProperties(alpha_record)) == 0:
            return
        try:
            if ((type(alpha_record) == AlphaRecord) == False):
                raise RuntimeError(DATA_TYPE_ERROR('store'))

            for col in getProperties(alpha_record):
                if col == '_tablename' or col == '_id':
                    continue

                # if '_' in col :
                # 	raise RuntimeError(UNDERSCORE_NOT_SUPPORTED_ERROR)

                if ' ' in col:
                    raise RuntimeError(SPACE_NOT_SUPPORTED_ERROR)

            alpha_record = DriverInterface.getDriver(
                AlphaORM.DRIVER).store(alpha_record)
        except Exception as e:
            raise e

    @staticmethod
    def drop(alpha_record):
        if ((type(alpha_record) == AlphaRecord) == False):
            raise RuntimeError(DATA_TYPE_ERROR('drop'))
        DriverInterface.getDriver(AlphaORM.DRIVER).drop(alpha_record)

    @staticmethod
    def dropAll(table_name):
        DriverInterface.getDriver(AlphaORM.DRIVER).dropAll(table_name)

    @staticmethod
    def getAll(table_name):
        return DriverInterface.getDriver(AlphaORM.DRIVER).getAll(table_name)

    @staticmethod
    def find(table_name, where, dict_map):
        return DriverInterface.getDriver(AlphaORM.DRIVER).find(table_name, where, dict_map)

    @staticmethod
    def findAll(table_name, where, dict_map):
        return DriverInterface.getDriver(AlphaORM.DRIVER).findAll(table_name, where, dict_map)

    @staticmethod
    def query(sql):
        return DriverInterface.getDriver(AlphaORM.DRIVER).query(sql)
