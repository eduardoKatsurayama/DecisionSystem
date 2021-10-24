from time import sleep

from src.ab_testing.policy_divider import split_events
from src.event_collector import event_collector
from src.master_policy import master_policy
from src.master_policy.master_policies.master_policy_a import MasterPolicyACreator
from src.master_policy.master_policies.master_policy_b import MasterPolicyBCreator
from src.utils.logger import logger

master_policies = {
    'Champion': MasterPolicyACreator,
    'Challenger': MasterPolicyBCreator
}

batch_count = 1

while True:
    logger.info(
        f'{"#" * 20} Batch {batch_count} {"#" * 20}'
    )
    events = event_collector.collect_events()

    if not events.empty:
        if len(master_policies) == 2:
            events = split_events(events=events, rate=.5)
        else:
            events = [events]

        for challenger, unique_master_policy, df in zip(range(2), master_policies.values(), events):
            master_policy.execute_master_policy(
                creator=unique_master_policy(),
                events=df,
                challenger=challenger
            )
    else:
        break
    batch_count += 1

    sleep(10)
