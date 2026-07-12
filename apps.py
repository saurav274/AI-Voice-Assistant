import os

# App list
apps={"spotify" :r"C:\Users\Saurav\Desktop\Spotify.lnk",
      "chrome" : "chrome.exe",
      "notepad" : "notepad.exe",
      "calculator" : "calc.exe",
      "browser": r"C:\Users\Saurav\Desktop\Microsoft Edge.lnk"
}

def open_app(app_name):
    if app_name in apps:
        try:
            os.startfile(apps[app_name])
            return True
        except Exception as e:
            print(e)
            print("Wrong path added")
    return False