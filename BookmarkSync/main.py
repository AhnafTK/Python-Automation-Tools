import json

#search for chrome edge and firefox
# C:\Users\ahnaf\AppData\Local\Microsoft\Edge\User Data\Default
# C:\Users\ahnaf\AppData\Local\Google\Chrome\User Data

edge_browser_folder = "C:\\Users\\ahnaf\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default" 
chrome_browser_folder = "C:\\Users\\ahnaf\\AppData\\Local\\Google\\Chrome\\User Data" # chrome has profiles

edge_browser_file = edge_browser_folder + "\\bookmarks"

def evaluateFolder(JSON):
    
    for item in JSON['children']:
        print(item['name'])
        if 'children' in item:
            evaluateFolder(JSON)

with open(edge_browser_file, encoding="utf-8") as f:
    chrome_data_raw = f.read()
    print(chrome_data_raw)
    chrome_data_json = json.loads(chrome_data_raw)
    #print(chrome_data_json["roots"]["bookmark_bar"])
    
    for item in chrome_data_json["roots"]["bookmark_bar"]["children"]:
        print(item['name'])
        if 'children' in item:
            evaluateFolder(item)

