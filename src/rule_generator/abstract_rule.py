from abc import ABC, abstractmethod

from src.utils import general_functions
from src.utils.logger import logger


class RuleCreator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def apply_rule(self, flow, mis):
        product = self.factory_method()
        to_deny, na_code = product.filter_denied_cpfs(flow)
        if len(to_deny):
            general_functions.deny_customer(flow, mis, to_deny, na_code)

        logger.info(f'Applied {na_code} rule on {len(to_deny)} customers')


class RuleProduct(ABC):
    @abstractmethod
    def query_feature(self, flow):
        pass

    @abstractmethod
    def transform_feature(self, flow):
        pass

    @abstractmethod
    def filter_denied_cpfs(self, flow):
        pass
