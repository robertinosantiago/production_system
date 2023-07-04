class Memory:
    
    def __init__(self):
        self.facts = {}
        self.expression = ''
        self.errors = []
        

    def add_fact(self, fact, value):
        self.facts[fact] = value

    def get_fact(self, fact):
        return self.facts.get(fact)