import os
from requests import get
try:
    bs4_test = True
    from bs4 import BeautifulSoup
except:
    try:
        import pip
        print("if you want the full features, use this command in console: pip install beautifulsoup4")
        bs4_test = False
    except:
        print("if you want the full features, intall pip via this link\nhttps://phoenixnap.com/kb/install-pip-windows#:~:text=PIP%20On%20Windows-,Step%201%3A%20Download%20PIP%20get%2Dpip.py,you%20can%20use%20it%20later.")
        print("\nand then use this command in console: pip install beautifulsoup4")
        bs4_test = False

def vimeo_downloader(url):
    try:
        if bs4_test == True:
            print("[vimeo_downloader] finding name of video")
            info = get(url)
            soup = BeautifulSoup(info.text, 'lxml')
            name = str(soup.find_all('h1')).replace("<",",").replace(">",',').split(",")[7] 
        else:
            while True:
                name = input("what is the name of the video: ")
                if path.exists(name + ".mp4") == True:
                    print("file already exists")
                    continue
                else:
                    break     
        print("[vimeo_downloader] name of video is " +name)
        print("[vimeo_downloader] Sending request to player.vimeo.com")
        r = get("https://player.vimeo.com/video/" + url.split("/")[3], allow_redirects=True)
        print("[vimeo_downloader] The request has been successfully")
        magic_link = r.content.decode().split('"')
        count = 0
        for i in range(len(magic_link)):
            item = magic_link[i]
            item_save = magic_link[i]
            try:
                item = item.replace(".","†").replace("%","†").split("†")
                if "mp4" in item:
                    if count == 0:
                        count += 1
                    else:
                        break
            except:
                continue
                    
        print("[vimeo_downloader] magic link has been made.")
        print("[vimeo_downloader] sending request to magic link")
        r = get(item_save, allow_redirects=True)
        print("[vimeo_downloader] The request has been successfully")
        print("[vimeo_downloader] downloading")
        
        open(name + ".mp4", 'wb').write(r.content)
        print("[vimeo_downloader] downloading is done and file save to " + os.getcwd())        
    except Exception as e:
        print("Error: " +str(e))
    


vimeo_downloader("https://vimeo.com/312478768")

