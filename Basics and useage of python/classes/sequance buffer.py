class Buffer:
    def __init__(self):
        self.sequance=[]

    def add(self, *a):
        for i in a:
            self.sequance.append(i)
            if len(self.sequance)==5:
                print(sum(self.sequance))
                self.sequance=[]

    def get_current_part(self):
        return self.sequance