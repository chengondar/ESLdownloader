import ConfigParser
import requests
import os
MAX = 2000

def get_rss(url):
    rss = requests.get(url)
    if rss.status_code == '200':
        print rss.text


def main():
    cf = ConfigParser.ConfigParser()
    cf.read("option.conf")

    rss_enable = cf.get("esl", "rss_enable").strip()
    latest_pod, latest_cafe = 0, 0
    if rss_enable == 'true':
        rss_url = cf.get("esl", "rss_url").strip()
        get_rss(rss_url)
    else:
        latest_pod, latest_cafe = 2000, 500

    if latest_pod <= cf.getint("local", "last_pod") and latest_cfe <= cf.getint("local", "last_cafe"):
        print "Already download"
        exit()

    base_url = cf.get("esl", "download_base_url")
    pod_base_url = base_url + cf.get("esl", "pod_pre")
    cafe_base_url = base_url + cf.get("esl", "cafe_pre")
    suffix = cf.get("esl", "suffix")

    esl = [1079,1089,1106,112,113,118,127,130,294,417,61,62,63,64,65,719,831,87,997]
    for pod in esl:
        url = pod_base_url + str(pod) + suffix
        print "download " + url
        code = os.system("timeout 500 axel -n 10 " + url)
        # if code == '256':
        #     break
    ec = [117,60,66,71,88,96]
    for cafe in ec:
        url = cafe_base_url + str(cafe) + suffix
        code = os.system("timeout 500 axel -n 10 " + url)
        # if code == '256':
        #     break


main()
