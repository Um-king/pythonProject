import requests
from bs4 import BeautifulSoup

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
# 특정 URL이 접속하는 요청(Request) 객체 생성
request = requests.get("https://n.news.naver.com/mnews/article/comment/025/0003273028?sid=105", headers=headers)

# 접속한 이후 웹 사이트 소스코드 추출
html = request.text
#print(html)

# HTML 소스코드를 파이썬 객체로 변환(파이썬 객체로 파싱)
soup = BeautifulSoup(html, 'html.parser')

# 해당 태크 순에 속하는 요소를 추출
links = soup.select('span')
print(links)

# 모든 링크에 하나씩 접근
for link in links:
#     # 링크의 속성 추출
      if link.has_attr('style data-lang'):
#         # data-lang 속성값으로 ko 라는 문자열이 포함되어 있다면
          if link.get('style data-lang').find('ko') != -1:
             print(link.text)


# all = soup.find("span", {'class' : "u_cbox_contents"})
# print(all)

#span = all.find_all("span")

# for item in span:
#     link2 = item.find"(span")

#print(link2)
