from src.column_generator.abstract_column_generator import (
    ColumnGeneratorCreator,
    ColumnGeneratorProduct,
)


class StrategyColumnGeneratorCreator(ColumnGeneratorCreator):
    def __init__(self, master_policy_type):
        self.strategy = master_policy_type

    def factory_method(self, df):
        return StrategyColumnGeneratorProduct(df, self.strategy)


class StrategyColumnGeneratorProduct(ColumnGeneratorProduct):
    def __init__(self, df, strategy):
        super().__init__(df)
        self.strategy = strategy

    def query_column(self):
        return self.strategy

    def transform_column(self):
        self.df['strategy'] = self.query_column()
