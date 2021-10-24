from src.column_generator.column_generator import execute_column_generator
from src.column_generator.columns.policy_column_generator import (
    MasterPolicyColumnGeneratorCreator,
)
from src.column_generator.columns.strategy_column_generator import (
    StrategyColumnGeneratorCreator,
)
from src.utils.logger import logger


def add_mis_columns(mis, master_policy_type, master_policy_name):
    logger.info('Started mis column Generator')
    columns = [
        
        MasterPolicyColumnGeneratorCreator(master_policy_name),
        StrategyColumnGeneratorCreator(master_policy_type)
    ]

    for column in columns:
        execute_column_generator(column, mis)
        logger.info(f'Added {mis.columns[-1]} to mis')

    logger.info(f'Added all {len(columns)} columns to mis with success')
