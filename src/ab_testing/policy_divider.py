import numpy as np

from src.utils.constants import A_EVENT, B_EVENT


def generate_samples(event, rate):
    if rate > 1:
        raise Exception('The maximum rate is 1')
    group_a = np.random.choice(
        event,
        size=int(len(event)*rate),
        replace=False
    )
    group_b = list(set(event) - set(group_a))
    return list(group_a), group_b


def split_events(events, rate):
    example_event_a = list(events[events.origin == A_EVENT].index)
    example_event_b = list(events[events.origin == B_EVENT].index)

    event_a_groups = generate_samples(example_event_a, rate)
    event_b_groups = generate_samples(example_event_b, rate)
    groups = list()
    
    for count, event_a, event_b in zip(
            [0, 1], event_a_groups, event_b_groups
    ):
        groups.append(
         events.loc[event_a + event_b].copy()
        )
        groups[count].reset_index(drop=True, inplace=True)

    return groups
