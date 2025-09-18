from todo_class import Todo
from data import DATA
from datetime import datetime

t = Todo(DATA)
print('Current time:', datetime.now())
print('All todos:', t.list_todos())
print('Closest:', t.find_closest())
