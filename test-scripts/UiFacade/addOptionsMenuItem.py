import android
import time

droid = android.Android()

droid.addOptionsMenuItem("Silly", "silly", None)
droid.addOptionsMenuItem("Sensible", "click", "I bet.")
droid.addOptionsMenuItem("Off", "off", None)

print "Hit menu to see extra options."
print "Will timeout in 10 seconds if you hit nothing."

while True: # Wait for events from the menu.
    response=droid.eventWait(10000).result
    if response==None:
        break
    print response
    if response["name"]=="off":
        break

droid.clearOptionsMenu()
print "Context menu cleared"

time.sleep(5)
print "And done."
