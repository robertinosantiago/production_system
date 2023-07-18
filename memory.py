class Memory:
    
    def __init__(self):
        self.facts = {}
        self.errors = []
        self.facts['errors'] = []
        
    def add_fact(self, fact, value):
        self.facts[fact] = value

    def get_fact(self, fact):
        return self.facts.get(fact)
    
    def clean_facts(self):
        self.facts = {}
    
    def add_error(self, error):
        self.errors.append(error)
        
    def list_errors(self):
        return self.errors
    
    def clean_errors(self):
        self.errors = []