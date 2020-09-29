UNDERSCORE_NOT_SUPPORTED_ERROR = 'Column names cannot contain `_` symbol'
SPACE_NOT_SUPPORTED_ERROR = 'Column names should not have a space'
RECORD_NOT_FOUND = "Record matching query not found"
SETUP_ERROR = 'Connection to database has not been set yet!'
UNEQUAL_BOUNDED_PARAMETER = 'Number of bounded parameters is not equal to variables'
DB_VARIABLE_ERROR = 'Values of can only be number, string or boolean'
RECORD_NOT_STORED = 'This record is not stored yet'


def SETUP_PARAMETER_MISSING(paremeter):
    return f"The '{paremeter}' is required!"


def DATA_TYPE_ERROR(method):
    return f"Parameter passed into method `{method}` must be of type `AlphaRecord`"


def DRIVER_NOT_SUPPORTED(driver):
    return f"'{driver}' is not a supported database. Supported databases includes mysql"


def SETUP_OPTION_MISSING(option):
    return f"The '{option}' option is required for this database!"


def VARIABLE_NOT_PRESENT(var):
    return f"Variable '{var}' is not present in parameters"
