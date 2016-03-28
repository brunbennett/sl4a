import android
import time

droid = android.Android()

message = "Testing the dialog dismissal"

positive = "OK"
negative = "Cancel"


# Only message 
droid.dialogCreateAlert("", message) 
droid.dialogSetNegativeButtonText(negative)
droid.dialogSetPositiveButtonText(positive)

droid.dialogShow()

time.sleep(3)

# Dismiss dialog automatically
droid.dialogDismiss()
