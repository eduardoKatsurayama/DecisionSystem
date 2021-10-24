from abc import ABC, abstractmethod


class ColumnGeneratorCreator(ABC):
    @abstractmethod
    def factory_method(self, df):
        pass

    def generate_column(self, df):
        product = self.factory_method(df)
        return product.collect_column_product()


class ColumnGeneratorProduct(ABC):
    def __init__(self, df):
        self.df = df

    @abstractmethod
    def query_column(self):
        pass

    @abstractmethod
    def transform_column(self):
        pass

    def collect_column_product(self):
        return self.transform_column()
