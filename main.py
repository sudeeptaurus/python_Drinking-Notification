import time

from plyer import notification


if __name__ == "__main__":

    # while True: # run pythonw main.py to run in background.
        notification.notify(
            title = "**Please Drink Water!!",
            message = "The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon = "C:\\Users\\DD\\Desktop\\Taurus\\Python Programming\\Drinking Notification\\icon.ico",
            timeout=10
        )
        # time.sleep(60*60)

    