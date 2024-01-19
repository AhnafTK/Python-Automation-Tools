import json

#search for chrome edge and firefox
# C:\Users\ahnaf\AppData\Local\Microsoft\Edge\User Data\Default
# C:\Users\ahnaf\AppData\Local\Google\Chrome\User Data

edge_browser_folder = "C:\\Users\\ahnaf\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default" 
chrome_browser_folder = "C:\\Users\\ahnaf\\AppData\\Local\\Google\\Chrome\\User Data" # chrome has profiles

edge_browser_file = edge_browser_folder + "\\bookmarks"


master_url_table = {}

def evaluateFolder(JSON):
    
    for item in JSON['children']:
        print(item['name'])
        if 'children' in item: # each folder
            evaluateFolder(JSON)

with open(edge_browser_file, encoding="utf-8") as f:
    recurse_fac = 0
    edge_data_raw = f.read()
    print(edge_data_raw)
    edge_data_json = json.loads(edge_data_raw)
    #print(chrome_data_json["roots"]["bookmark_bar"])
    
    for item in edge_data_json["roots"]["bookmark_bar"]["children"]:
        print(item['name'])
        if 'children' in item: # each folder
            evaluateFolder(item)
        else:
            # check if the url has been processed already. if processed, discard. 
            if item['url'] in master_url_table:
                continue
            
            master_url_table[item['url']] = item['name']
        

print("\n\n\n\MASTER URL TABLE")
for key in master_url_table:
    print(key)