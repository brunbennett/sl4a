# This script checks the operation of the new supported attributes for the GridLayout class.
# See https://developer.android.com/reference/android/support/v7/widget/GridLayout.html

import android
import time
from xml_loader import getXML

droid = android.Android()

xml = getXML("layouts/layout_grid_layout.xml")

droid.fullShow(xml)

# Debug

gl = "gridLayout"

droid.makeToast("Testing New Supported GridLayout Attributes")
time.sleep(2)

# -----------------------------------------------------------------------------
# alignmentMode

prop = "alignmentMode"
val = "alignMargins"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(gl, prop, val)
print gl + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

val = "alignBounds"
droid.fullSetProperty(gl, prop, val)

# -----------------------------------------------------------------------------
# GridLayout.LayoutParams (inner class) 
# -----------------------------------------------------------------------------

# NOTHING BELOW WORKS

# -----------------------------------------------------------------------------
# layout_column

btn = "button"
tv = "textView"
et = "editText"

prop = "layout_column"
val = "1"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(gl, prop, val)
print gl + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# layout_columnSpan

prop = "layout_columnSpan"
val = "5"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# layout_columnWeight 

prop = "layout_columnWeight"
val = "2"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(et, prop, val)
print et + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# layout_row

btn = "button"
tv = "textView"
et = "editText"

prop = "layout_row"
val = "1"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(btn, prop, val)
print btn + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# layout_rowSpan

prop = "layout_rowSpan"
val = "5"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# layout_rowWeight 

prop = "layout_rowWeight"
val = "2"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(et, prop, val)
print et + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------

droid.fullDismiss()
