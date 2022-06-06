import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/History_of_Mexico"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")
parser_output = soup.find("div", class_="mw-parser-output")
paragraphs = parser_output.find_all("p")


def get_citations_needed_count():
    counter = 0

    for p in paragraphs:
        ankers = p.find_all("a", title="Wikipedia:Citation needed")

        for _ in ankers:
            counter += 1

    return counter


def get_citations_needed_report():
    output = "The following paragraphs need citation \n \n"

    for p in paragraphs:
        text = p.text
        count = text.count("[citation needed]")
        check = "[citation needed]" in text
        if check:
            if count == 1:
                index = text.index("[citation needed]")
                output += text[0 : index - 1]
                output += "\n \n"
            if count > 1:
                multi = text.split("[citation needed]")
                i = 0
                for _ in range(len(multi) - 1):
                    output += multi[i]
                    output += "\n \n"
                    i += 1

    return output


if __name__ == "__main__":
    pass
