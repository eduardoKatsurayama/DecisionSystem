from abc import ABC, abstractmethod


class MasterPolicyCreator(ABC):
    @abstractmethod
    def factory_method(self, events, challenger):
        pass

    def run_master_policy(self, events, challenger):
        master_policy = self.factory_method(events, challenger)
        master_policy.run_master_policy_flow()


class MasterPolicyProduct(ABC):
    def __init__(self, events, challenger):
        self.events = events
        self.master_policy_type = 'Challenger' if challenger else 'Champion'
        self.flow = None
        self.mis = None

    @abstractmethod
    def generate_flow(self):
        pass

    @abstractmethod
    def apply_rules(self):
        pass

    @abstractmethod
    def apply_model_policies(self):
        pass

    @abstractmethod
    def run_master_policy_flow(self):
        pass
