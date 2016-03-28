import os.path
import android
import time
from string import join

cur_dir = os.path.dirname(os.path.realpath(__file__)) + "/"

def getXML(filename):
    fin = open(cur_dir + filename, "r")
    lines = fin.readlines()
    fin.close()
    return join(lines)

droid = android.Android()

xml = getXML("layoutFullSetList.xml")

droid.fullShow(xml)

# Lists

view_id = "spinner"
items = ["item 1", "item 2", "item 3", "item 4", "item 5"]
call = droid.fullSetList(view_id, items)
print call.result

view_id = "listView"
items = ["item 1", "item 2", "item 3", "item 4", "item 5", "item 6", "item 7", "item 8", "item 9", "item 10", "item 11", "item 12", "item 13", "item 14", "item 15"]
call = droid.fullSetList(view_id, items)
print call.result

time.sleep(8)

droid.fullDismiss()
