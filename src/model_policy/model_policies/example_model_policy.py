from src.model_policy.abstract_model_policy import (
    ModelPolicyCreator,
    ModelPolicyProduct,
)
from src.utils import general_functions
from src.utils.logger import logger


class ExampleModelPolicyCreator(ModelPolicyCreator):
    def factory_method(self):
        return ExampleModelPolicyProduct()


class ExampleModelPolicyProduct(ModelPolicyProduct):
    def make_decision(self, mis):
        predictions = [0, 1, 1, 0]
        mis['predictions'] = predictions
        f'Predicted {mis.shape[0]} rows with success'

    def apply_denied(self, flow, mis):
        to_deny = mis.loc[mis.predictions == 0, 'id'].to_list()
        general_functions.deny_customer(
            flow, mis, to_deny, 'DENIED_BY_MAIN_POLICY'
        )

        logger.info(
            f'Denied into main master_policy on {len(to_deny)} customers'
        )

