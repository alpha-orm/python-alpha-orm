from interface import implements
from .QueryBuilderInterface import QueryBuilderInterface
import json, re
from ..utilities.constants import *
from ..utilities.functions import *
from ..AlphaRecord import AlphaRecord

class MySQLQueryBuilder(implements(QueryBuilderInterface)):

	DATA_TYPE = { 'float': 'double', 'str': 'text', 'bool': 'smallint', 'int': 'int' }
	
	@staticmethod
	def createTable(tablename):
		return f"CREATE TABLE IF NOT EXISTS `{tablename}` ( `id` INT UNSIGNED NOT NULL AUTO_INCREMENT , PRIMARY KEY (`id`))"
	
	@staticmethod
	def deleteRecord(alpha_record):
		return f"DELETE FROM `{alpha_record.getTableName()}` WHERE `id` = {alpha_record.getID()}"

	@staticmethod
	def deleteAllRecords(tablename): 
		return f"DELETE FROM `{tablename}`"


	@staticmethod
	def getColumns(tablename):
		return f"DESCRIBE `{tablename}`"


	@staticmethod
	def getAllRecords(tablename):
		return f"SELECT * FROM `{tablename}`"


	@staticmethod
	def find(single, tablename, where, dict_map=[]):
		sql = f"SELECT * FROM `{tablename}` WHERE "
		columns = list(dict_map.keys())
		matches = re.findall(r':[a-zA-Z]+',where)

		if (len(dict_map) == 0):
			sql += where
			sql +=  ' LIMIT 1' if single else ''
			return sql

		if len(matches) != len(columns):
			raise RuntimeError(UNEQUAL_BOUNDED_PARAMETER)

		for match in matches:
			i = match.replace(':','')
			if i not in dict_map:
				raise RuntimeError(VARIABLE_NOT_PRESENT(i))
			val = dict_map[i]
			val = val.replace("'","\'") if isinstance(val, str) else val
			val = 1 if val is True else 0 if isinstance(val, bool) else val
			val = json.dumps(val)
			where = where.replace(match, val)
		sql += where
		sql += ' LIMIT 1' if single else ''
		return sql

	@staticmethod
	def updateRecord(tablename, dict_map, id):
		sql = f"UPDATE `{tablename}` SET "
		columns = getProperties(dict_map)
		for column in columns:
			if column in [ '_id', 'id', '_tablename' ]:
				continue
			colVal = getattr(dict_map, column)
			if isinstance(colVal, AlphaRecord) :
				continue	
			colVal = 1 if colVal is True else 0 if isinstance(colVal, bool) else colVal
			colVal = json.dumps(colVal)
			if column in  [ '_id', '_tablename', 'id' ]:
				continue
			sql += f"`{column}` = {colVal}"
			sql += f" WHERE `id` = {id}" if column == columns[-1] else ', ' 
		if sql.endswith(', '):
			sql = sql[:-2] + f" WHERE `id` = {id}"
		return sql

	@staticmethod
	def insertRecord(tablename, dict_map):
		sql = f"INSERT INTO `{tablename}` ("
		columns = getProperties(dict_map)
		for column in columns :
			if column in  [ '_tablename', '_id' ]:
				continue
			if column != 'id' and isinstance(getattr(dict_map, column), AlphaRecord):
				column += '_id'
			sql += f"`{column}`"
			sql += ') VALUES (' if column.replace('_id','') == columns[-1] else ','
		for column in columns:
			if column in [ '_tablename', '_id' ]:
				continue
			if column == 'id':
				colVal = dict_map.getID()
			else:
				colVal = getattr(dict_map, column)
				if column != 'id' and isinstance(getattr(dict_map, column), AlphaRecord):
					colVal = getattr(dict_map, column).getID()
			colVal = 1 if colVal is True else 0 if isinstance(colVal, bool) else colVal
			sql += json.dumps(colVal)
			sql += ')' if column == columns[-1] else ','
		return sql

	@staticmethod
	def updateColumns(tablename, dict_map):
		sql = f"ALTER TABLE `{tablename}`"
		columns = list(dict_map.keys())
		for column in columns:
			sql += f"MODIFY COLUMN `{column}` {dict_map[column]}"
			sql += '' if   column == columns[-1] else ','
		return sql

	@staticmethod
	def createColumns(tablename, dict_map):
		sql = f"ALTER TABLE `{tablename}` "
		columns = list(dict_map.keys())
		for column in columns:
			if column in [ '_id', '_tablename' ]:
				continue
			sql += f"ADD COLUMN IF NOT EXISTS `{column}` {dict_map[column]}"
			sql += '' if column == columns[-1] else ','
		return sql

	@staticmethod
	def getQueryBuilder(driver):
		pass