import pandas as pd

from src.event_collector.abstract_event_collector import (
    EventCollectorCreator,
    EventCollectorProduct,
)
from src.utils.constants import  B_EVENT
from src.utils.logger import logger


class EventBCollectorCreator(EventCollectorCreator):
    def factory_method(self):
        return EventBCollectorProduct()


class EventBCollectorProduct(EventCollectorProduct):
    def query_event(self):
        query = {
            'id': [5, 6, 7, 8],
            'example_feature': [2, 4, 6, 8]
        }
        return pd.DataFrame(query)

    def add_event_type(self):
        df = self.query_event()
        df['origin'] = B_EVENT

        logger.info(
            f'Inserted {df.shape[0]} event_b customers'
        )

        return df
