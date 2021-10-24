from src.column_generator import mis_generator


class FlowGenerator:
    def __init__(self, events):
        self.flow = events
        self.mis = self.flow.copy()

    def generate(self, master_policy_type, master_policy_name):
        mis_generator.add_mis_columns(self.mis, master_policy_type, master_policy_name)
