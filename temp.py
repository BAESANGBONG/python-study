from bs4 import BeautifulSoup

html_doc = """
<html>
<body>

<h1>H1태그</h1>
<div class='a'>클래스찾기 - a</div>
<div class='b'>클래스찾기 - b</div>
<div class='b'>클래스찾기 - b2</div>
<div id='hello'>아이디찾기</div>

<div id='focusPanelCenter'>
    <div class='panel_inner'>
        <img alt='국민일보'></img>
    </div>
</div>

</body>
</html>
"""

# HTML 엘레멘트 = DOM
soup = BeautifulSoup(html_doc, 'html.parser')

target = soup.select_one("#focusPanelCenter .panel_inner img")
# print(target)
title = target["alt"]
# print(title)

target2 = soup.select_one(".b")
print(target2.text)

m_body = soup.body
# print(m_body)
m_h1 = soup.h1
# print(m_h1)

m_a = soup.find(class_="a")
# print(m_a)
m_b = soup.find(class_="b")
# print(m_b)

m_b_all = soup.find_all(class_="b")
# print(m_b_all)

# let temp = document.querySelector("#focusPanelCenter .panel_inner img");
m_hello = soup.find(id="hello")
# print(m_hello)
