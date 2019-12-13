def array_diff(first, second):
	a = list(set(first) - set(second))
	b = list(set(second) - set(first))
	diff = list(set(a + b))
	return (diff)


def getProperties(theObject):
	properties = []
	for prop, _ in vars(theObject).items():
		if prop.startswith('_AlphaRecord__') == False:
			properties.append(prop)
	return properties

def get_type(variable):
	return type(variable).__name__

def getTableMap(tablename):
	from ..drivers.DriverInterface import DriverInterface
	from ..AlphaORM import AlphaORM	
	g = []
	for element in DriverInterface.getDriver(AlphaORM.DRIVER).getColumns(tablename):
		g.append({ element['Field'] : element['Type'] })
	j = []
	for pair in g:
		for key, val in pair.items():
			pass
			j.append({ key : val })
	return j