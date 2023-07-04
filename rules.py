class Rule:
    
    def __init__(self, name, condition, action):
        self.name = name
        self.condition = condition
        self.action = action

    def evaluate(self, working_memory):
        if self.condition(working_memory):
            self.action(working_memory, self.name)
            