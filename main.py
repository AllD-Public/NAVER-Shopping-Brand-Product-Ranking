import requests
from bs4 import BeautifulSoup
import time

brand = input("브랜드 명을 정확히 입력해주세요 : ")

html = requests.get("https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000000&listType=B10002")
soup = BeautifulSoup(html.content, "html.parser")

productList = soup.select(".cont > a")
cnt = 1

print(brand + " 브랜드에서 판매하고 있는 제품이 네이버 쇼핑몰 의류 순위 100위 안에 있는지 체크합니다. (기준시간 : " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ")")
for product in productList:
    print("진행률 : " + str(cnt) + "/100")
    detail_html = requests.get(product.attrs['href'])
    detail_soup = BeautifulSoup(detail_html.content, "html.parser")

    info_list = detail_soup.select(".info_inner > span")

    for info in info_list :
        infoStr = info.get_text()
        try :
            brandNameStartIdx = infoStr.index("브랜드 ")
            brandName = infoStr[brandNameStartIdx + 4:].strip()

            if brandName == brand :
                productName = detail_soup.select(".h_area > h2")[0].get_text().strip()
                print("[발견!] " + str(cnt)+'위. ' + productName)
        except :
            print(end="")

    cnt = cnt + 1
