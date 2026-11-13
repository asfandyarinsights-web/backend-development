import importlib

import filechages

def changes():
    try:
        importlib.reload(filechages)
        filechages.print_changes()
    except:
        pass
for i in range(5):
    changes()
    input("Hit enter to reload.....")