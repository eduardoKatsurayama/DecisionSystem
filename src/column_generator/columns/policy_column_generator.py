from src.column_generator.abstract_column_generator import (
    ColumnGeneratorCreator,
    ColumnGeneratorProduct,
)


class MasterPolicyColumnGeneratorCreator(ColumnGeneratorCreator):
    def __init__(self, master_policy):
        self.master_policy = master_policy

    def factory_method(self, df):
        return MasterPolicyColumnGeneratorProduct(df, self.master_policy)


class MasterPolicyColumnGeneratorProduct(ColumnGeneratorProduct):
    def __init__(self, df, master_policy):
        super().__init__(df)
        self.master_policy = master_policy

    def query_column(self):
        return self.master_policy

    def transform_column(self):
        self.df['master_policy'] = self.query_column()
