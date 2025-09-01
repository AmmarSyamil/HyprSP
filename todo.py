from tasklib import TaskWarrior, Task
from datetime import datetime
import os

#Setup the file path for the todo file
# tw = TaskWarrior(data_location="./.todo")
# task = Task(tw, desc="tes")
# task.save()
proj = os.path.abspath("./") 
class Todo():
    def __init__(self):
        super().__init__()
        self.tw = TaskWarrior(
            data_location=f"{proj}/.todo",
            taskrc_location=f"{proj}/.taskrc",
            create=True
            )
        
    def find_item(self, uuid):
        print(self.load_item())
        print(uuid)

        data = self.tw.tasks.get(uuid=uuid)

        # data = self.load_item()
        # current = data["s"]
        print('\n', data["uuid"])
        return data

    def add_item(self, desc, deadline, status, title):
        """deadline must be in datetime format, like this (2025, 2, 14, 8, 0, 0)"""
        # if status is None:
        #     print(len(self.tw.tasks.all()))
        # print(len(self.tw.tasks.all()))
        # print(self.tw.tasks.all())
        # Validate status before creating the task
        # valid_statuses = ['completed', 'not_completed']
        # if status not in valid_statuses:
        #     raise ValueError(f"The status '{status}' is not valid. Valid statuses are: {valid_statuses}")
        task = Task(self.tw, title=title, description=desc, status=status, due=deadline)
        task.save()

    def load_item(self):
        return self.tw.tasks.all()
    
    def delete_item(self, desc=None, status=None, deadline=None):

        task = self.tw.tasks.get(description=desc, status=status, due=deadline)
        task.delete()
        
#different between get and filter


if __name__ == "__main__":
    app = Todo()
    app.add_item(title= "title test", desc="tes", status="pending", deadline=datetime(year=2025, month=9, day=2))
    print(app.load_item())
        
