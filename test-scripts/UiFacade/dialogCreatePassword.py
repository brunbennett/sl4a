import android

droid = android.Android()

title = "Password Dialog"
message = "Enter a new password"

droid.dialogCreatePassword(title, message)

droid.dialogShow()

response = droid.dialogGetResponse().result

print response
