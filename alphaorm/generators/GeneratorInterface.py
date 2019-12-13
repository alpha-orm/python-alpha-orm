import interface
class GeneratorInterface (interface.Interface):

    @staticmethod
    def checkColumnUpdates(columns_db, columns_record, alpha_record):
        pass

    @staticmethod
    def creatNewColumns(dict_map, alpha_record, tablename):
        pass

    @staticmethod
    def columns(columns_db, alpha_record, base = True):
        pass