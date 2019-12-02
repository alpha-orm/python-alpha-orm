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