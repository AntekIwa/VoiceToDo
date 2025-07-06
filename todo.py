class TODO:
    def __init__(self):
        self.todo = []
    def add(self, task):
        if task in self.todo:
            return False
        self.todo.append(task)
        return True
    def del_task(self, task):
        if task not in self.todo:
            return False
        self.todo.remove(task)
        return True
    def del_idx(self, idx):
        if idx > len(self.todo):
            return False
        self.todo.pop(idx - 1)
        return True
    def printt(self):
        print("Rozmiar listy: ", len(self.todo))
        for i in range(len(self.todo)):
            print(i + 1, self.todo[i])
        
lista = TODO()
lista.add("matma")
lista.add("Polski")
lista.printt()
lista.del_task("matma")
lista.printt()
lista.del_idx(1)
lista.printt()
