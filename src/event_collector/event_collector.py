import pandas as pd

from src.event_collector.events import a_event_collector, b_event_collector
from src.utils.logger import logger


def event_collector(creator):
    return creator.generate_event_df()


def collect_events():
    logger.info('Started event collector')
    flow = pd.DataFrame()
    events = [
        a_event_collector.EventACollectorCreator(),
        b_event_collector.EventBCollectorCreator()
    ]
    for event in events:
        flow = flow.append(event_collector(event), ignore_index=True)

    logger.info(f'Generated {flow.shape[0]} event rows with success')
    return flow
