# This script checks the operation of the new supported attributes for the GridLayout class.
# See https://developer.android.com/reference/android/support/v7/widget/GridLayout.html

import android
import time
from xml_loader import getXML

droid = android.Android()

xml = getXML("layouts/layout_linear_layout.xml")

droid.fullShow(xml)

# Debug

ll = "linearLayout"
ll2 = "linearLayout2"

droid.makeToast("Testing New Supported LinearLayout Attributes")
time.sleep(2)

# -----------------------------------------------------------------------------
# showDividers

prop = "showDividers"
val = "middle"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(ll2, prop, val)
print ll2 + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

# -----------------------------------------------------------------------------
# divider

prop = "divider"
val = "@android:drawable/title_bar"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(ll2, prop, val)
print ll2 + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

# -----------------------------------------------------------------------------
# measureWithLargestChild

prop = "measureWithLargestChild"
val = "true"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(ll, prop, val)
print ll + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

# -----------------------------------------------------------------------------

droid.fullDismiss()
