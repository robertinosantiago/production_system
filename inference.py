class InferenceEngine:
    
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def execute_rules(self, working_memory):
        for rule in self.rules:
            rule.evaluate(working_memory)