from config import *

if __name__ == '__main__':
    
    for i,v in STRUCTURE.items():
        # print(i,v)
        if i =="ui":
            for u, c in v.items():
                # print("pyside6-uic", {u}, "-o", {c})
                try:
                    print("pyside6-uic", u, "-o", c)
                    run = subprocess.Popen(["pyside6-uic", u, "-o", c])
                    output = run.communicate()[0]
                    print(output)
                except Exception as e:
                    raise e
                # pyside6-uic ui/main.ui -o compiled/ui_main.py
        elif i == "qrc":
            for u, c in v.items():
                # pass
                try:
                    print("pyside6-uic", u, "-o", c)
                    run = subprocess.Popen(["pyside6-rcc", u, "-o", c])
                    output = run.communicate()[0]
                    print(output) 
                except Exception as e:
                    raise e
                # pyside6-rcc resources.qrc -o compiled/resources_rc.py  
        else:
            raise "niga"
