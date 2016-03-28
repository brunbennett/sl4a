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

xml = getXML("fullShowToolbar.xml")

droid.fullShow(xml)

toolbarID = "toolbar"
toolbarTitle = "Toolbar Title"
toolbarSubtitle = "Testing Toolbar Subtitle"
toolbarTitleColor = "#0A0"
toolbarSubtitleColor = "#FFF"

call = droid.fullSetToolbarTitle(toolbarID, toolbarTitle)
print call

call = droid.fullSetToolbarSubtitle(toolbarID, toolbarSubtitle)
print call

call = droid.fullSetToolbarTitleColor(toolbarID, toolbarTitleColor)
print call

call = droid.fullSetToolbarSubtitleColor(toolbarID, toolbarSubtitleColor)
print call

time.sleep(5)

droid.fullDismiss()
