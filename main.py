from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import os

now=time
def crawling_img(name):
    search = name  # 이미지 이름
    count = 20  # 크롤링할 이미지 개수
    if not os.path.isdir("C:/Users/jw267/PycharmProjects/imgcrolling/idols/" + str(search)):
        os.mkdir("C:/Users/jw267/PycharmProjects/imgcrolling/idols/" + str(search))
    saveurl = "C:/Users/jw267/PycharmProjects/imgcrolling/idols/" + str(search) + "/" + str(search)  # 이미지들을 저장할 폴더 주소

    ## 셀레니움으로 구글 이미지 접속 후 이미지 검색

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=1920x1080")


    elem = driver.find_element(By.NAME, "q")
    # elem = driver.find_element(By.ID, "nx_query")
    elem.clear()
    elem.send_keys(search)

    elem.send_keys(Keys.RETURN)

    # 페이지 끝까지 스크롤 내리기
    SCROLL_PAUSE_TIME = 1
    # 스크롤 깊이 측정하기
    last_height = driver.execute_script("return document.body.scrollHeight")

    # 스크롤 끝까지 내리기

    while True:

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # 페이지 로딩 기다리기
        time.sleep(SCROLL_PAUSE_TIME)
        # 더 보기 요소 있을 경우 클릭하기

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            try:
                driver.find_element_by_css_selector(".mye4qd").click()

            except:
                break

        last_height = new_height

    # 이미지 찾고 다운받기
    images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")

    for i in range(count):

        try:
            images[i].click()  # 이미지 클릭
            time.sleep(1)
            # imgUrl = driver.find_element(By.CSS_SELECTOR,".n3VNCb").get_attribute("src")
            imgUrl = driver.find_element(By.XPATH,
                                         '//*[@id="Sva75c"]//div[1]//div[1]//div[3]//div[2]//c-wiz//div//div[1]//div[1]//div[2]//div[1]//a//img').get_attribute(
                "src")
            urllib.request.urlretrieve(imgUrl, saveurl + str(now.strftime('%Y%m%d%H%M%S')) + ".jpg")  # 이미지 다운

        except:
            pass

idols = ["아이네 일러스트",
         "징버거 일러스트",
         "릴파 일러스트",
         "주르르 일러스트",
         "고세구 일러스트",
         "비챤 일러스트",
         "우왁굳 일러스트"]

driver = webdriver.Chrome('C://chromedriver.exe')  # options=options
driver.set_window_position(0, 0)
driver.set_window_size(1980, 1080)
driver.minimize_window()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")#크롬
# driver.get('https://search.naver.com/search.naver?where=image&section=image&query=아이네')#네이버
for idol in idols:
    crawling_img(idol)

driver.close()
