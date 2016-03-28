# This script checks the operation of the new supported attributes for the TextView class.
# See http://developer.android.com/reference/android/widget/TextView.html.

import android
import time
from xml_loader import getXML

droid = android.Android()

xml = getXML("layouts/layout_text_view.xml")

droid.fullShow(xml)

# Debug

tv = "textView"
et = "editText"
ll = "linearLayout"

droid.makeToast("Testing New Supported TextView Attributes")
time.sleep(2)

# -----------------------------------------------------------------------------
# autoText

# Solved with the mAttrMethods hash map helper.

prop = "autoText"
val = "false"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "true"
# droid.fullSetProperty(tv, prop, val)
call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result

# -----------------------------------------------------------------------------
# breakStrategy (Warning: API >= 23)

# prop = "breakStrategy"
# val = "high_quality"
# droid.makeToast(prop)
# time.sleep(2)
#
# call = droid.fullSetProperty(et, prop, val)
# print et + " " + prop + " set to " + val + " = " + call.result
#
# val = "simple"
# droid.fullSetProperty(et, prop, val)

# -----------------------------------------------------------------------------
# bufferType

prop = "bufferType"
val = "editable"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "normal"
call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result

# -----------------------------------------------------------------------------
# capitalize

prop = "capitalize"
val = "characters"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "sentences"
call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result

# -----------------------------------------------------------------------------
# drawableBottom

prop = "drawableBottom"
val = "@android:drawable/dialog_frame"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# drawableEnd 

prop = "drawableEnd"
val = "@android:drawable/dialog_frame"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# drawableLeft

prop = "drawableLeft"
val = "@android:drawable/dialog_frame"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# drawablePadding

prop = "drawablePadding"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(et, prop, val)
print et + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "16dp"
droid.fullSetProperty(et, prop, val)

# -----------------------------------------------------------------------------
# drawableRight

prop = "drawableRight"
val = "@android:drawable/dialog_frame"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# drawableStart

prop = "drawableStart"
val = "@android:drawable/dialog_frame"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# drawableTop

prop = "drawableTop"
val = "@android:drawable/dialog_frame"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# ellipsize

prop = "ellipsize"
val = "marquee"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "none"
call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result

val = "none"
call = droid.fullSetProperty(ll, prop, val)
print ll + " " + prop + " set to " + val + " = " + call.result

# -----------------------------------------------------------------------------
# imeActionId

prop = "imeActionId"
val = "105"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(et, prop, val)
print et + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# imeActionLabel

prop = "imeActionLabel"
val = "Some IME action"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(et, prop, val)
print et + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)


# -----------------------------------------------------------------------------
# imeOptions

prop = "imeOptions"
val = "flagNoFullscreen"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(et, prop, val)
print et + " " + prop + " set to " + val + " = " + call.result

val = "actionNone"
call = droid.fullSetProperty(et, prop, val)
print et + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# lineSpacingExtra

prop = "text"
val = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam viverra nec consectetur ante hendrerit. Donec et mollis dolor. Praesent et diam eget libero egestas mattis sit amet vitae augue. Nam tincidunt congue enim, ut porta lorem lacinia consectetur. Donec ut libero sed arcu vehicula ultricies a non tortor."
droid.fullSetProperty(tv, prop, val)

prop = "lineSpacingExtra"
val = "8dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "8dp"
droid.fullSetProperty(tv, prop, val)

# -----------------------------------------------------------------------------
# lineSpacingMultiplier

prop = "lineSpacingMultiplier"
val = "1.5"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "1"
droid.fullSetProperty(tv, prop, val)

prop = "text"
val = "Just another TextView"
droid.fullSetProperty(tv, prop, val)

# -----------------------------------------------------------------------------
# maxLength

prop = "maxLength"
val = "10"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(et, prop, val)
print et + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# scrollHorizontally

prop = "text"
val = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam viverra nec consectetur ante hendrerit. Donec et mollis dolor. Praesent et diam eget libero egestas mattis sit amet vitae augue. Nam tincidunt congue enim, ut porta lorem lacinia consectetur. Donec ut libero sed arcu vehicula ultricies a non tortor."
droid.fullSetProperty(tv, prop, val)

prop = "scrollHorizontally"
val = "true"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "false"
droid.fullSetProperty(tv, prop, val)

prop = "text"
val = "Just another TextView"
droid.fullSetProperty(tv, prop, val)

# -----------------------------------------------------------------------------
# shadowColor

prop = "shadowColor"
val = "@android:color/holo_red_dark"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# shadownDx

prop = "shadowDx"
val = "45"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# shadowDy

prop = "shadowDy"
val = "45"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# shadowRadius

prop = "shadowRadius"
val = "5"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# textAllCaps

prop = "textAllCaps"
val = "true"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "false"
droid.fullSetProperty(tv, prop, val)

# -----------------------------------------------------------------------------
# textColorLink

prop = "text"
val = "A text with a link, i.e., https://www.google.com"
droid.fullSetProperty(tv, prop, val)
time.sleep(2)

prop = "textColorLink"
val = "#0F0"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

prop = "text"
val = "A TextView"
droid.fullSetProperty(tv, prop, val)

droid.fullDismiss()
