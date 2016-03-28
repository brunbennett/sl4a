import android

droid = android.Android()

title = "Test"
message = "Testing the dialog alert"

# Title and message
droid.dialogCreateAlert(title, message)

# Only title
# droid.dialogCreateAlert(title, "")

# Only message 
# droid.dialogCreateAlert("", message) 

droid.dialogShow()
