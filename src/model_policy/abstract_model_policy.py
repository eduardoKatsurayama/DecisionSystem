from abc import ABC, abstractmethod


class ModelPolicyCreator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def apply_model_policy(self, flow, mis):
        product = self.factory_method()
        return product.run_model_policy(flow, mis)


class ModelPolicyProduct(ABC):
    @abstractmethod
    def make_decision(self, mis):
        pass

    @abstractmethod
    def apply_denied(self, flow, mis):
        pass
    
    def run_model_policy(self, flow, mis):
        self.make_decision(mis)
        self.apply_denied(flow, mis)