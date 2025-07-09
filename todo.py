import os
import json

class TODO:
    def __init__(self, filename = "todo_data.json"):
        self.filename = filename
        self.todo = self.load()

    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.todo, f, ensure_ascii=False, indent=2)

    def add(self, task):
        if task in self.todo:
            return False
        self.todo.append(task)
        self.save()
        return True

    def del_task(self, task):
        if task not in self.todo:
            return False
        self.todo.remove(task)
        self.save()
        return True

    def del_idx(self, idx):
        if idx > len(self.todo):
            return False
        self.todo.pop(idx - 1)
        self.save()
        return True

    def printt(self):
        print("Rozmiar listy: ", len(self.todo))
        for i in range(len(self.todo)):
            print(i + 1, self.todo[i])


lista = TODO()
lista.add("matma")
lista.add("Polski")
text = ""
for i in range(len(lista.todo)):
    text += str(i + 1) + " "  + lista.todo[i] + " "
