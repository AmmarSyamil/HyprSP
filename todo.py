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
        # print(self.load_item())
        # print(uuid)

        data = self.tw.tasks.get(uuid=uuid)

        # data = self.load_item()
        # current = data["s"]
        # print('\n', data["uuid"])
        return data
    
    def edit_item(self, task, title=None, description=None, due=None, status=None):
        print('\n',task)
        if title:
            # print("title")
            task["title"] = title

        if description:
            # print("desc")
            task["description"] = description

        if due:
            # print("due")
            task["due"] = due

        try:
            if status:
                print(status, "here")
                task["status"] = status

        except Exception as e:
            print(e)

        # for i in [title, description, due, status]:

        #     if i:
        #         task[i] = str(i)
        # # task["title"] = str(title)
        # # task["description"] = str(desc)
        # # task["deadline"] = str(deadline)
        # # task["status"] = str(status)

        try:
            # print("save u lil  nifa")
            task.save()
            print(task)
            # self.load_item()
        except Exception as e:
            return e



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
        # idk = [task for task in self.tw.tasks.all() if task["status"] != 'deleted']
        return self.tw.tasks.pending()

    def delete_item(self, task):
        if task:
            task_current = task
        # else:
            # task_current = self.tw.tasks.get(description=desc, status=status, due=deadline)
        task_current.delete()
        # task_current.save()
        
#different between get and filter


if __name__ == "__main__":
    app = Todo()
    app.add_item(title= "title test", desc="tes", status="pending", deadline=datetime(year=2025, month=9, day=2))
    print(app.load_item())
        
