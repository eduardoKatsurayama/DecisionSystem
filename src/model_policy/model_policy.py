from src.utils.logger import logger


def model_policy_enforcer(creator, flow, mis):
    return creator.apply_model_policy(flow, mis)


def apply_model_policy(flow, mis, model_policies):
    logger.info('Started main master_policy enforcer')

    for model_policy in model_policies:
        model_policy_enforcer(model_policy, flow, mis)

    logger.info(f'Applied all {len(model_policies)} main master_policies with success')
