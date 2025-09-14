from datetime import datetime, timedelta
from config import DATA

class Todo:
    def __init__(self,data):
        self.todos = data
        # self.counter = 1

    def add_todo(self, title, description, deadline, importance):
        todo = {
            "title": title,
            "description": description,
            "deadline": deadline,
            "created": datetime.now(),
            "status": "pending",
            "importance": importance
        }
        self.todos[datetime.now()] = todo
        # self.counter += 1

    def list_todos(self):
        if not self.todos:
            data = {}
        else:
            for id, todo in self.todos.items():
                data[id] = todo

        return data

    def mark_done(self, id):
        if id in self.todos:
            self.todos[id]["status"] = "completed"
            return f"Succes {id}"
        else:
            return "Invalid id"
    
    def delete(self, id):
        if self.todos[id]:
            del self.todos[id]

            try:
                self.todos[id]
                return "Failed"
            except Exception as e:
                return "Succes"

        else:
            return "Invalid id"
        
    def find_closest(self):
        now = datetime.now()
        closest_deadline = datetime.max

        current_id = "sybau"

        for id, todo in self.todos.items():
            current_deadline = self.todos[id].get("deadline")
            if current_deadline > now:
                closest_deadline = current_deadline
                current_id = id

        if closest_deadline != datetime.max:
            return closest_deadline, current_id
        else:
            return None
        
    def search_todos(self, title=None, description=None, deadline=None, created=None, status=None, importance=None):
        data = []
        for x in [title, description, deadline, created, status, importance]:
            if x:
                for i in ["title", "description", "deadline", "created", "status", "importance"]:
                    if i:
                        for id, todo in self.todos.items():
                            miaw = self.todos[id].get(i)
                            
                            if miaw:
                                if str(miaw).lower() == str(x).lower():
                                    # print(miaw)
                                    data.append(id)
                                else:
                                    print("sybau")
                            else:
                                print("pmo")
        return data
        
if __name__ == "__main__":
    app = Todo(DATA)
    print(app.find_closest())

    
