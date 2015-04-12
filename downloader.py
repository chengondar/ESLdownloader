import ConfigParser
import requests


def get_rss(url):
    rss = requests.get(url)
    if rss.status_code == '200':
        print rss.text


def main():
    cf = ConfigParser.ConfigParser()
    cf.read("option.conf")
    rss_url = cf.get("esl", "rss_url").strip()
    get_rss(rss_url)

main()