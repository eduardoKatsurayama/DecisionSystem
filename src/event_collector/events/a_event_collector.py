import pandas as pd

from src.event_collector.abstract_event_collector import (
    EventCollectorCreator,
    EventCollectorProduct,
)
from src.utils.constants import (
    A_EVENT
)
from src.utils.logger import logger


class EventACollectorCreator(EventCollectorCreator):
    def factory_method(self):
        return EventACollectorProduct()


class EventACollectorProduct(EventCollectorProduct):
    def query_event(self):
        query = {
            'id': [1, 2, 3, 4],
            'example_feature': [1, 3, 5, 7]
        }
        return pd.DataFrame(query)

    def add_event_type(self):
        df = self.query_event()
        df['origin'] = A_EVENT

        logger.info(
            f'Inserted {df.shape[0]} event_a customers'
        )

        return df
