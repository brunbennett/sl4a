# Testing the dialogShow() method.

import android

droid = android.Android()

title = "Dialog Show"
message = "Testing the dialog show method"

title2 = "Dialog Show v2"
message2 = "Second dialog alert?"

# Comment out to test when no dialog is present
droid.dialogCreateAlert(title, message)

# Test which dialog is shown.
droid.dialogCreateAlert(title2, message2)

# Show an existing dialog.
droid.dialogShow()
