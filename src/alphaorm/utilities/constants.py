UNDERSCORE_NOT_SUPORRTED_ERROR = 'Column names cannot contain `_` symbol'
SPACE_NOT_SUPORRTED_ERROR = 'Column names should not have a space'

def SETUP_PARAMETER_MISSING(paremeter):
	return f"The '{paremeter}' is required!"

def DATA_TYPE_ERROR(method):
	return f"Parameter passed into method `{method}` must be of type `AlphaRecord`"