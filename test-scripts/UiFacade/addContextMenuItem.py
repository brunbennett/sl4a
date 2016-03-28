import android
import time

droid = android.Android()

droid.addContextMenuItem("Entry 1", "entry1", None)
droid.addContextMenuItem("Entry 2", "entry", "Tapped 2.")
droid.addContextMenuItem("Off", "off", None)

print "Hit menu to see extra options."
print "Will timeout in 10 seconds if you hit nothing."

while True:  # Wait for events from the menu.
    response = droid.eventWait(10000).result
    if response is None:
        break
    print response
    if response["name"] == "off":
        print "You tapped \"Off\""
        break

droid.clearContextMenu()
print "Context menu cleared"

time.sleep(5)
print "And done."
