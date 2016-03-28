import android

droid = android.Android()

title = "Input Dialog"
message = "Enter a number"
def_text = ""
input_type = "number"  # Only numbers are allowed

droid.dialogCreateInput(title, message, def_text, input_type)

droid.dialogSetNegativeButtonText("cancel")
droid.dialogSetPositiveButtonText("ok")

droid.dialogShow()

response = droid.dialogGetResponse().result

print response
