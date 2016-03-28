# This script checks the operation of the new supported attributes for the View class.
# See http://developer.android.com/reference/android/view/View.html#lattrs

import android
import time
from xml_loader import getXML

droid = android.Android()

# xml = getXML("layouts/layout.xml")
xml = getXML("layouts/layout_scrollable.xml")

droid.fullShow(xml)

ll = "linearLayout"
btn = "button"
img_btn = "imageButton"
et = "editText"
tv = "textView"

droid.makeToast("Testing New Supported View Attributes")
time.sleep(2)

# -----------------------------------------------------------------------------
# accessibilityLiveRegion

prop = "accessibilityLiveRegion"
val = "polite"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(btn, prop, val)
print btn + " " + prop + " set to " + val + " = " + call.result

val = "none"
droid.fullSetProperty(btn, prop, val)

# -----------------------------------------------------------------------------
# accessibilityTraversalAfter

prop = "accessibilityTraversalAfter"
val = tv
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(btn, prop, val)
print btn + " " + prop + " set to " + val + " = " + call.result

# -----------------------------------------------------------------------------
# accessibilityTraversalBefore

prop = "accessibilityTraversalBefore"
val = img_btn
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(btn, prop, val)
print btn + " " + prop + " set to " + val + " = " + call.result

# -----------------------------------------------------------------------------
# backgroundTint

prop = "backgroundTint"
val = "#6F00"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(ll, prop, val)
print ll + " " + prop + " set to " + val + " = " + call.result

# -----------------------------------------------------------------------------
# drawingCacheQuality

prop = "drawingCacheQuality"
val = "low"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(img_btn, prop, val)
print img_btn + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "auto"
droid.fullSetProperty(img_btn, prop, val)

# -----------------------------------------------------------------------------
# elevation

prop = "elevation"
val = "8dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(img_btn, prop, val)
print img_btn + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "0dp"
droid.fullSetProperty(img_btn, prop, val)

# -----------------------------------------------------------------------------
# fadingEdgeLength

prop = "fadingEdgeLength"
val = "100dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(ll, prop, val)
print ll + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

# -----------------------------------------------------------------------------
# importantForAccessibility

prop = "importantForAccessibility"
val = "noHideDescendants"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(img_btn, prop, val)
print img_btn + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "auto"
droid.fullSetProperty(img_btn, prop, val)

# -----------------------------------------------------------------------------
# isScrollContainer

prop = "isScrollContainer"
val = "true"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(ll, prop, val)
print ll + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "false"
droid.fullSetProperty(ll, prop, val)

# -----------------------------------------------------------------------------
# layoutDirection

prop = "layoutDirection"
val = "rtl"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(et, prop, val)
print et + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

val = "inherit"
droid.fullSetProperty(et, prop, val)

# -----------------------------------------------------------------------------
# minHeight

prop = "minHeight"
val = "28dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print ll + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "8dp"
droid.fullSetProperty(ll, prop, val)

# -----------------------------------------------------------------------------
# minWidth

prop = "minWidth"
val = "100dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print ll + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "20dp"
droid.fullSetProperty(ll, prop, val)

# -----------------------------------------------------------------------------
# paddingBottom

prop = "paddingBottom"
val = "32dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(btn, prop, val)
print btn + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

val = "16dp"
droid.fullSetProperty(btn, prop, val)

# -----------------------------------------------------------------------------
# paddingEnd 

prop = "paddingEnd"
val = "32dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(btn, prop, val)
print btn + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

val = "16dp"
droid.fullSetProperty(btn, prop, val)

# -----------------------------------------------------------------------------
# paddingLeft 

prop = "paddingLeft"
val = "32dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(btn, prop, val)
print btn + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

val = "16dp"
droid.fullSetProperty(btn, prop, val)

# -----------------------------------------------------------------------------
# paddingRight 

prop = "paddingRight"
val = "32dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(btn, prop, val)
print btn + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

val = "16dp"
droid.fullSetProperty(btn, prop, val)

# -----------------------------------------------------------------------------
# paddingStart 

prop = "paddingStart"
val = "32dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(btn, prop, val)
print btn + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

val = "16dp"
droid.fullSetProperty(btn, prop, val)

# -----------------------------------------------------------------------------
# paddingTop 

prop = "paddingTop"
val = "32dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(btn, prop, val)
print btn + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

val = "16dp"
droid.fullSetProperty(btn, prop, val)

# -----------------------------------------------------------------------------
# requiresFadingEdge

prop = "requiresFadingEdge"
val = "horizontal|vertical"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(btn, prop, val)
print btn + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

val = "none"
droid.fullSetProperty(btn, prop, val)

# -----------------------------------------------------------------------------
# scrollIndicators

prop = "scrollIndicators"
val = "left"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(ll, prop, val)
print ll + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

val = "right"
droid.fullSetProperty(ll, prop, val)

# -----------------------------------------------------------------------------
# scrollbarDefaultDelayBeforeFade

prop = "scrollbarDefaultDelayBeforeFade"
val = "100"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(ll, prop, val)
print ll + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

val = "500"
droid.fullSetProperty(ll, prop, val)

# -----------------------------------------------------------------------------
# scrollbarFadeDuration

# Solved with the mAttrMethods hash map helper.

prop = "scrollbarFadeDuration"
val = "800"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(ll, prop, val)
print ll + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

val = "500"
droid.fullSetProperty(ll, prop, val)

# -----------------------------------------------------------------------------
# scrollbarSize

# Solved with the mAttrMethods hash map helper.

prop = "scrollbarSize"
val = "16dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(ll, prop, val)
print ll + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

val = "6dp"
droid.fullSetProperty(ll, prop, val)

# -----------------------------------------------------------------------------
# scrollbarStyle

# Solved with the mAttrMethods hash map helper.

prop = "scrollbarStyle"
val = "outsideOverlay"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(ll, prop, val)
print ll + " " + prop + " set to " + val + " = " + call.result
time.sleep(3)

val = "insideOverlay"
droid.fullSetProperty(ll, prop, val)

# -----------------------------------------------------------------------------
# textAlignment (warning: API >= 17)

# Solved with the ViewInflater.toUnderscore() tweak.

prop = "textAlignment"
val = "viewStart"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "inherit"
droid.fullSetProperty(tv, prop, val)

# -----------------------------------------------------------------------------
# textDirection (warning: API >= 17)

# Solved with the ViewInflater.toUnderscore() tweak.

prop = "textDirection"
val = "anyRtl"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "inherit"
droid.fullSetProperty(tv, prop, val)

# -----------------------------------------------------------------------------
# transformPivotX

# Solved with the mAttrMethods hash map helper.

prop = "transformPivotX"
val = "3dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "0dp"
droid.fullSetProperty(tv, prop, val)

# -----------------------------------------------------------------------------
# transformPivotY

# Solved with the mAttrMethods hash map helper.

prop = "transformPivotY"
val = "3dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "0dp"
droid.fullSetProperty(tv, prop, val)

# -----------------------------------------------------------------------------
# transitionName

# Not related method.

# -----------------------------------------------------------------------------
# translationX

# Solved with the mAttrMethods hash map helper.

prop = "translationX"
val = "12dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "0dp"
droid.fullSetProperty(tv, prop, val)

# -----------------------------------------------------------------------------
# translationY

# Solved with the mAttrMethods hash map helper.

prop = "translationY"
val = "12dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "0dp"
droid.fullSetProperty(tv, prop, val)

# -----------------------------------------------------------------------------
# translationZ

# Solved with the mAttrMethods hash map helper.

prop = "translationZ"
val = "12dp"
droid.makeToast(prop)
time.sleep(2)

call = droid.fullSetProperty(tv, prop, val)
print tv + " " + prop + " set to " + val + " = " + call.result
time.sleep(2)

val = "0dp"
droid.fullSetProperty(tv, prop, val)

# -----------------------------------------------------------------------------

droid.fullDismiss()
