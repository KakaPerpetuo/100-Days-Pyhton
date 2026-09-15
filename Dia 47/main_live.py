import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Sony-Playstation-Version-Ultra-High-Bluetooth/dp/B09W14BJF1?dib=eyJ2IjoiMSJ9.HxfLMiZcbu3cR1bjRckuzHWluyE_vqBn5ZwonQhgx8n5U6DYQb28qKKVtmYVVOTmq9fBCdaMcFOmEYUnV__7HOTk8iyPMynZGeSgnuP1klGrgigZT4qigYZQIJeWW3fcWyg2Kmnj0T6HBrdLlQy2SOV9MbqDjDcMPzP1XhUDKz221BPdQiE-BUeQkahvNsnc0tqEt93tF0L0NtlJSpjAH_XoTf-DjUuSQ9Y3x6nIZXc.JOOWfQ8P_RhjvGoIaLe29BDnenQqZfEMa49qq-A8i-0&dib_tag=se&keywords=playstation+5&qid=1789508054&sr=8-2"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
#print(soup.prettify())

price = soup.find("span", id="apex-pricetopay-accessibility-label").getText()

print(price)