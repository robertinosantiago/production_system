import time
from datetime import datetime;

class Error:
    
    def __init__(self, type = None, subtype = None):
        self.type = type
        self.subtype = subtype
        self.timestamp = time.time()
        
    def __repr__(self):
        date_time = datetime.fromtimestamp(self.timestamp)
        strtime = date_time.strftime("%d/%m/%Y %H:%M") 
        return f"Error type: {self.type}, subtype: {self.subtype}, datetime: {strtime}"