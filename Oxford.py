import requests
# import json
app_id = "54489f82"
app_key = "77e3f80cffcf43b1840386e741e741bc"
language = "en-gb"


def getdic(word):
    word_id = word
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res = r.json()
    
    
    if 'error' in res.keys():
        return False
    
    dic = {}
    
    
    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        audio = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
    definitions = []
    
    
    for sense in res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']:
       definitions.append(f"👉{sense['definitions'][0]}")
    

    dic["audio"] = audio
    dic['definitions'] = "\n".join(definitions)
    
    
    return dic



if __name__ == '__main__':
    from pprint import pprint as print
    print(getdic('hello'))
