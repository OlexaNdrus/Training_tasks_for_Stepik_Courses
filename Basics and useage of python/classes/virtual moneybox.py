class MoneyBox:
    def __init__(self, capacity):
        self.capacity=capacity
        self.counter=0

    def can_add(self, v):
        if self.capacity>=self.counter+v:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.counter+=v