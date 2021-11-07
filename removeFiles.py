import os
import time
import shutil

path = '/C:/Users/C/OneDrive/Pictures/Camera-imports/Camera-Roll'

days = 20
seconds = time.time() - (days * 24 * 60 * 60)

if os.path.exists(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            path = os.path.join(root, name)
            ctime = os.stat(path).st_ctime

            if seconds >= ctime:
                os.remove(path)
                print("Deleted the path successfully")

        for name in dirs:
            path = os.path.join(root, name)
            ctime = os.stat(path).st_ctime

            if seconds >= ctime:
                shutil.rmtree(path)
                print("Deleted the path successfully")
else:
    print("Path not found")