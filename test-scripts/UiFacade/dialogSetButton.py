import android

droid = android.Android()

message = "This is a test of alert dialog"

positive = "OK"
negative = "Cancel"
neutral = "Whatever"

droid.dialogCreateAlert("", message) 

droid.dialogSetNegativeButtonText(negative)
droid.dialogSetPositiveButtonText(positive)
droid.dialogSetNeutralButtonText(neutral)

droid.dialogShow()

print droid.dialogGetResponse().result
