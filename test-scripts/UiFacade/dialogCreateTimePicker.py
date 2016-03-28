import android

droid = android.Android()

hour = 12
minute = 0
is_24_hour = False

droid.dialogCreateTimePicker(hour, minute)

droid.dialogShow()

response = droid.dialogGetResponse().result

print response
