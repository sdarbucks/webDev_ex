# findAll() - 모든 태그 요소를 찾아서 리스트로 반환
from bs4 import BeautifulSoup   # 파싱(구분분석)기

html_str = '''
<html>
    <body>
        <ul class = 'item'>
            <li>인공지능</li>
            <li>빅데이터</li>
            <li>로봇</li>
        </ul>
        <ul class = 'comlang'>
            <li>Python</li>
            <li>C/C#</li>
            <li>Java</li>
        </ul>
    </body>
</html>
'''

html = BeautifulSoup(html_str, "html.parser")
first_ul = html.find('ul', {'class':'item'})    # {키:값}
all_li = first_ul.findAll('li')
print(all_li)
print(all_li[1])
print(all_li[1].text)

for li in all_li[0:3]:
    print(li.text, end=" ")

print()
first_li = html.find('li')
print(first_li)