from src.utils.logger import logger


def rule_enforcer(creator, flow, mis):
    return creator.apply_rule(flow, mis)


def apply_rules(flow, mis, rules):
    logger.info("Started rule enforcer")
    for rule_index, rule in enumerate(rules):
        if not flow.empty:
            rule_enforcer(rule, flow, mis)
        else:
            logger.warning('Flow is empty')
            break

    if len(rules) and len(rules) == rule_index + 1:
        logger.info(f'Applied all {len(rules)} rules with success')
