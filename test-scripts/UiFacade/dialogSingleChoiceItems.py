import android
# import time

droid = android.Android()

title = "Single Choice Dialog"
message = "Testing the single choice dialog"

# Title and message
droid.dialogCreateAlert(title, message)

droid.dialogSetNegativeButtonText("cancel")
droid.dialogSetPositiveButtonText("ok")

items = ["choice 1", "choice 2", "choice 3", "choice 4"]
selected = [0,3]

droid.dialogSetSingleChoiceItems(items)

# Show an existing dialog.
droid.dialogShow()

# response = droid.dialogGetResponse().result
# print response

selection = droid.dialogGetSelectedItems()
print selection
