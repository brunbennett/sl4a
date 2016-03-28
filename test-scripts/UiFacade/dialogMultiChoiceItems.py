import android

droid = android.Android()

title = "Multi Choice Dialog"

droid.dialogCreateAlert(title, "")

droid.dialogSetNegativeButtonText("cancel")
droid.dialogSetPositiveButtonText("ok")

items = ["Choice 1", "Choice 2", "Choice 3", "Choice 4"]
selected = [0, 2]

droid.dialogSetMultiChoiceItems(items, selected)

droid.dialogShow()

selection = droid.dialogGetSelectedItems()
print selection
