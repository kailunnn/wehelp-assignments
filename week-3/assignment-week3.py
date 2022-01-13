import urllib.request as request
import json
import csv
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)

sites = data["result"]["results"]
# print(sites)
# 將資料整理好放進列表
infos = []
section = ["中正區","萬華區","中山區","大同區","大安區","松山區","信義區","士林區","文山區","北投區","內湖區","南港區"]
for site in sites:
    address = site["address"][5:8]
    if address in section:
        title = site["stitle"]
        longitude = site["longitude"]
        latitude = site["latitude"]
        # 圖片
        urlIndex = site["file"].lower().find('jpg')
        siteUrl = site["file"][0:urlIndex+3]
        info = [title,address,longitude,latitude,siteUrl]
        infos.append(info)
# print(infos)

# 寫入 csv
with open("data.csv","w",encoding="utf-8",newline='') as file:
    w = csv.writer(file)
    for item in infos:
        w.writerow(item)
