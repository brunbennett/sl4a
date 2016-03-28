import android

droid = android.Android()

title = "Get Input Dialog"
message = "Just a test"

print droid.dialogGetInput(title, message).result
