# This script checks the operation of the new supported attributes for the ImageView class.
# See https://developer.android.com/reference/android/widget/ImageView.html

import android
import time
from xml_loader import getXML

droid = android.Android()

xml = getXML("layouts/layout.xml")
# xml = getXML("layouts/layout_scrollable.xml")

droid.fullShow(xml)

# Debug

ll = "linearLayout"
btn = "button"
img_btn = "imageButton"
et = "editText"
tv = "textView"
img = "imageView"

droid.makeToast("Testing New Supported ImageView Attributes")
time.sleep(2)

# -----------------------------------------------------------------------------
# baseline

# Solved with the mAttrMethods hash map helper.

prop = "baseline"
val = "8dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(img, prop, val)
print img + " " + prop + " set to " + val + " = " + call.result

val = "0dp"
droid.fullSetProperty(img, prop, val)

# -----------------------------------------------------------------------------
# maxHeight

# Solved with the mAttrMethods hash map helper.

prop = "maxHeight"
val = "100dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(img, prop, val)
print img + " " + prop + " set to " + val + " = " + call.result

val = "250dp"
droid.fullSetProperty(img, prop, val)

# -----------------------------------------------------------------------------
# maxWidth

# Solved with the mAttrMethods hash map helper.

prop = "maxWidth"
val = "100dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(img, prop, val)
print img + " " + prop + " set to " + val + " = " + call.result

val = "250dp"
droid.fullSetProperty(img, prop, val)

# -----------------------------------------------------------------------------
# scaleType

# Needs special treatment. Uses an enumeration.

# -----------------------------------------------------------------------------
# src

# Explicitly supported in ViewInflater.
# Now migrated to the hash map helper.

# -----------------------------------------------------------------------------
# tint

# Solved with the mAttrMethods hash map helper.

prop = "tint"
val = "#33FF0000"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(img, prop, val)
print img + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

val = "null"
droid.fullSetProperty(img, prop, val)


# -----------------------------------------------------------------------------
# tintMode


# Not supported: method name != "set" + PCase(attrName).

# -----------------------------------------------------------------------------

droid.fullDismiss()
