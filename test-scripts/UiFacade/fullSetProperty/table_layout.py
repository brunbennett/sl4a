# This script checks the operation of the stretchColumn property
# used in TableLayout.

import android
import time
from xml_loader import getXML

droid = android.Android()

xml = getXML("layouts/layout_table_layout.xml")

droid.fullShow(xml)

# Debug

v = "tableLayout"

# -----------------------------------------------------------------------------
# stretchColumns

prop = "stretchColumns"
cols = "*"
droid.makeToast(prop)

time.sleep(3)

call = droid.fullSetProperty(v, prop, cols)
print v + " " + prop + " set for " + cols + " = " + call.result

time.sleep(3)

# -----------------------------------------------------------------------------
# shrinkColumns

prop = "shrinkColumns"
cols = "0, 2"
droid.makeToast(prop)

time.sleep(3)

call = droid.fullSetProperty(v, prop, cols)
print v + " " + prop + " set for " + cols + " = " + call.result

time.sleep(3)

# -----------------------------------------------------------------------------
# collapseColumns

prop = "collapseColumns"
cols = "1"
droid.makeToast(prop)

time.sleep(3)

call = droid.fullSetProperty(v, prop, cols)
print v + " " + prop + " set for " + cols + " = " + call.result

time.sleep(4)

droid.fullDismiss()
