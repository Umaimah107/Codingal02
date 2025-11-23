class Bird:
    def __init__(self):
        print("Bird is Ready")

    def whoisThis(self):
        print("Bird")
    
    def swim(self):
        print("Swim Faster")

class Penguin:
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    
    def whoisThis(self):
        print("Penguin")
    
    def run(self):
        print("Run Faster")
    
    def swim(self):
        print("Swim faster")
    
peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()