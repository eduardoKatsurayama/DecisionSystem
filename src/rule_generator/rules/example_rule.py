from src.rule_generator.abstract_rule import RuleCreator, RuleProduct


class ExampleRuleCreator(RuleCreator):
    def factory_method(self):
        return ExampleRuleProduct()


class ExampleRuleProduct(RuleProduct):
    def query_feature(self, flow):
        return flow[['id', 'example_feature']]

    def transform_feature(self, flow):
        return self.query_feature(flow)

    def filter_denied_cpfs(self, flow):
        filtered = self.transform_feature(flow)
        filtered = filtered.loc[
            filtered['example_feature'] % 2 != 0, 'id'
        ].to_list()
        return filtered, 'DENIED_CODE'
