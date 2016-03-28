import android

droid = android.Android()

title = "SeekBar Dialog"
message = "Move seekbar and press OK"

droid.dialogCreateSeekBar(50, 100, title, message)

droid.dialogSetNegativeButtonText("cancel")
droid.dialogSetPositiveButtonText("ok")

droid.dialogShow()

response = droid.dialogGetResponse().result

print response
