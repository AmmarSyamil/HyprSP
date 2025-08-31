from tasklib import TaskWarrior, Task
from datetime import datetime

#Setup the file path for the todo file
tw = TaskWarrior(data_location="./.todo")
task = Task(tw, desc="tes")
task.save()

