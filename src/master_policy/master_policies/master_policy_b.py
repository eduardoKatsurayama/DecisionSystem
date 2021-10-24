from src.flow_generator.flow_generator import FlowGenerator
from src.master_policy.abstract_master_policy import MasterPolicyCreator, MasterPolicyProduct
from src.model_policy import model_policy
from src.model_policy.model_policies.example_model_policy import ExampleModelPolicyCreator
from src.rule_generator import rule_generator
from src.rule_generator.rules.example_rule import ExampleRuleCreator
from src.utils.logger import logger


class MasterPolicyBCreator(MasterPolicyCreator):
    def factory_method(self, events, challenger):
        return MasterPolicyBProduct(events, challenger)


class MasterPolicyBProduct(MasterPolicyProduct):
    def __init__(self, events, challenger):
        super().__init__(events, challenger)
        self.master_policy_name = 'GENERIC_POLICY-B'
        logger.info(
            f'Started {self.master_policy_name} {self.master_policy_type} with '
            f'{self.events.shape[0]} events'
        )

    def generate_flow(self):
        flow_generator = FlowGenerator(self.events)
        flow_generator.generate(self.master_policy_type, self.master_policy_name)
        self.flow = flow_generator.flow
        self.mis = flow_generator.mis

    def apply_rules(self):
        rules = [ExampleRuleCreator()]
        rule_generator.apply_rules(self.flow, self.mis, rules)

    def apply_model_policies(self):
        model_policies = [ExampleModelPolicyCreator()]
        model_policy.apply_model_policy(self.flow, self.mis, model_policies)

    def run_master_policy_flow(self):
        if not self.events.empty:
            self.generate_flow()
            self.apply_rules()
            self.apply_model_policies()

        logger.info(
            f'Finished {self.master_policy_name} {self.master_policy_type}'
        )
