

class Countlist:
    def __init__(self,*value):
        self.list = [x for x in value]
        self.count = {}.fromkeys(range(len(self.list)),0)

    def __len__(self):
        return len(self.list)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.list[key]


