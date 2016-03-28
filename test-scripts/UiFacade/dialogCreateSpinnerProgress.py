import android

droid = android.Android()

title = "Spinner Dialog"
message = "Testing spinner progress dialog"
max_prog = 75

droid.dialogCreateSpinnerProgress(title, message)

droid.dialogShow()

response = droid.dialogGetResponse().result

print response
