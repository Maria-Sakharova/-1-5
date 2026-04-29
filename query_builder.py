class QueryBuilder:
    @staticmethod
    def select(table):
        return f'SELECT * FROM {table}'
