import android

droid = android.Android()

droid.dialogCreateDatePicker(2016, 10, 1)
droid.dialogShow()

response = droid.dialogGetResponse().result

print response
