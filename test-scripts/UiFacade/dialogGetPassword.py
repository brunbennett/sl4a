import android

droid = android.Android()

title = "Get Password Dialog"
message = "Just a test"

print droid.dialogGetPassword(title, message).result
