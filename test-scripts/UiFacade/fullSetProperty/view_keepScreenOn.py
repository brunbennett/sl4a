# This script checks the operation of the new supported attributes for the View class.
# Individual test for keepScreenOn.
# See http://developer.android.com/reference/android/view/View.html#lattrs

import android
import time
from xml_loader import getXML

droid = android.Android()

# xml = getXML("layouts/layout.xml")
xml = getXML("layouts/layout_scrollable.xml")

droid.fullShow(xml)

# Debug

ll = "linearLayout"
droid.makeToast("Testing New Supported View Attributes")
time.sleep(2)

# -----------------------------------------------------------------------------
# keepScreenOn

# It's a very long test. Device has to be able to sleep by inactivity.

prop = "keepScreenOn"
val = "true"
droid.makeToast("disallow screen turning off")

call = droid.fullSetProperty(ll, prop, val)
print ll + " " + prop + " set to " + val + " = " + call.result

time.sleep(25)

val = "false"
droid.fullSetProperty(ll, prop, val)

droid.makeToast("allow screen turning off")

time.sleep(20)

droid.fullDismiss()
