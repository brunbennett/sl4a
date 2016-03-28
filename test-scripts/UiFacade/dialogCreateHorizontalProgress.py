import android
import time

droid = android.Android()

title = "Progress"
message = ""

droid.dialogCreateHorizontalProgress(title, message)

droid.dialogShow()

time.sleep(2)

# Set new max progress.
droid.dialogSetMaxProgress(50)
time.sleep(2)

for p in range(1,51):
    droid.dialogSetCurrentProgress(p)
    time.sleep(0.1)


# Dismiss dialog automatically
# droid.dialogDismiss()
