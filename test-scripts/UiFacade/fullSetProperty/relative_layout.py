# This script checks the operation of the new supported attributes for the GridLayout class.
# See https://developer.android.com/reference/android/support/v7/widget/GridLayout.html

import android
import time
from xml_loader import getXML

droid = android.Android()

xml = getXML("layouts/layout_relative_layout.xml")

droid.fullShow(xml)

# Debug

rl = "relativeLayout"
et = "editText"

droid.makeToast("Testing New Supported RelativeLayout Attributes")
time.sleep(2)

# -----------------------------------------------------------------------------
# ignoreGravity 

prop = "ignoreGravity"
val = et
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(rl, prop, val)
print rl + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

# -----------------------------------------------------------------------------

droid.fullDismiss()
