from abc import ABC, abstractmethod


class EventCollectorCreator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def generate_event_df(self):
        product = self.factory_method()
        return product.collect_event_product()


class EventCollectorProduct(ABC):
    @abstractmethod
    def query_event(self):
        pass

    @abstractmethod
    def add_event_type(self):
        pass

    def collect_event_product(self):
        return self.add_event_type()
