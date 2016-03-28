import android

droid = android.Android()

title = "Items Dialog"
message = "Testing the item list dialog"

droid.dialogCreateAlert(title, message)

droid.dialogSetNegativeButtonText("cancel")
droid.dialogSetPositiveButtonText("ok")

items = ["item 1", "item 2", "item 3", "item 4"]

droid.dialogSetItems(items)

droid.dialogShow()

response = droid.dialogGetResponse().result
print response
