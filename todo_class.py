from datetime import datetime, timedelta
from config import DATA

class Todo:
    def __init__(self,data):
        self.todos = data
        self.counter = len(self.todos)
        self.load()

    def add_todo(self, title, description, deadline: datetime, importance, status):
        try:
            todo = {
                "title": title,
                "description": description,
                "deadline": deadline,
                "created": datetime.now(),
                "status": status,
                "importance": importance
            }
            try:
                # Generate unique ID
                self.counter += 1
                todo_id = f"todo{self.counter}"
                self.todos[todo_id] = todo
                print(self.todos[todo_id])
                self.save()

            except Exception as e:
                print("done")
                print(self.todos[todo_id])
            # self.save()
        except Exception as e:
            return e
        # self.counter += 1

    def list_todos(self):
        data = {}
        if not self.todos:
            return data
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
        if id in self.todos:
            del self.todos[id]
            self.save()
            return None
        else:
            raise ValueError("Invalid id")
        
    def find_closest(self):
        now = datetime.now()
        closest_deadline = None
        current_id = None
        min_diff = None

        for id, todo in self.todos.items():
            current_deadline = todo.get("deadline")
            if current_deadline:
                diff = abs((current_deadline - now).total_seconds())
                if min_diff is None or diff < min_diff:
                    min_diff = diff
                    closest_deadline = current_deadline
                    current_id = id

        if current_id is not None:
            return current_id, self.todos[current_id]
        else:
            return None
        
    def search_todos(self, id = None,title=None, description=None, deadline=None, created=None, status=None, importance=None):
        data = []
        if id:
            return self.todos[id]
        
        for x in [id, title, description, deadline, created, status, importance]:
            if x:
                for i in ["title", "description", "deadline", "created", "status", "importance"]:
                    if i:
                        for ids, todo in self.todos.items():
                            if 1 < 0:
                                pass
                            # if x  == id and id and id == ids: #  idk if this will works or not but hopefullt i could make it happen wihtout any 
                            #     data.append(self.todos[id])
                            else:
                                miaw = self.todos[ids].get(i)
                                
                                if miaw:
                                    if str(miaw).lower() == str(x).lower():
                                        # print(miaw)
                                        data.append(ids)
                                    else:
                                        print("sybau")
                                else:
                                    print("pmo")
        return data

    def get_top_priority(self):
        valid_priorities = ["Important", "Normal", "Not important"]

        filtered_todos = []
        for id, todo in self.todos.items():
            priority = todo.get("importance")
            if priority in valid_priorities:
                filtered_todos.append((id, todo, priority))

        # Sort by priority (Important > Normal > Not important), then by deadline ascending
        priority_order = {"Important": 0, "Normal": 1, "Not important": 2}
        filtered_todos.sort(key=lambda x: (priority_order[x[2]], x[1]["deadline"]))

        # Get top 5 priorities
        top_priorities = {id:todo for id, todo, pri in filtered_todos[:5]}


                    # closest_deadline = todo

        return top_priorities

    def save(self):
        import json
        from datetime import datetime

        def json_serial(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            raise TypeError("Type not serializable")

        with open("todos.json", "w") as f:
            json.dump(self.todos, f, default=json_serial)

    def load(self):
        import json
        from datetime import datetime

        def json_deserial(dct):
            for key in ['deadline', 'created']:
                if key in dct:
                    dct[key] = datetime.fromisoformat(dct[key])
            return dct

        try:
            with open("todos.json", "r") as f:
                self.todos = json.load(f, object_hook=json_deserial)
        except FileNotFoundError:
            self.todos = {}
        

if __name__ == "__main__":
    app = Todo(DATA)
    # print(app.find_closest())
    # print(app.list_todos())
    result = app.get_top_priority()
    print(type(result))
    print(result)

    
