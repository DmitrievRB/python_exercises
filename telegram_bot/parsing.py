from bs4 import BeautifulSoup
import requests



def main():
    base = "https://ru.stackoverflow.com/"
    html = requests.get(base).content
    soup = BeautifulSoup(html, "lxml")
    div = soup.find("div", id="question-mini-list")
    a = div.findAll("a", class_ = "s-link")
    for _ in a:
        print(_.getText(), base + _.get("href"))
  




if __name__ == "__main__":
    main()
