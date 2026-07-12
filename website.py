import webbrowser

#Website list
websites={
    "instagram" : "https://www.instagram.com",
    "github" : "https://github.com",
    "google" : "https://google.com",
    "youtube" : "https://www.youtube.com"
}

def open_site(site_name):
    if site_name in websites:
        try:
            webbrowser.open(websites[site_name])
            return True
        except Exception as e:
            print(e)
    return False