import requests
from bs4 import BeautifulSoup

ep_link = None
tiwi_link = None
hash = None
video_link = None

def main(start, end):
    border = start + (end-start)
    file = open('video-link-list.txt', 'w')
    while start <= border:
        url = 'http://animehaven.to/episodes/subbed/fairy-tail/page' + str(start)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('h2', {'data-mark': 'for_single'}):
            global ep_link
            ep_link = link.a.get('href')
            #print('episode link: ' + ep_link)
            browse_episode(ep_link)
            #print('tiwi link: ' + tiwi_link)
            get_hash(tiwi_link)
            #print('hash: ' + hash)
            get_video_link(hash)
            #print('video link: ' + video_link)
            file.write(video_link + '\n')
        start += 1
    file.close()

def browse_episode(source):
    source_code = requests.get(source)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for pre_download in soup.findAll('a', {'class': 'btn btn-1 btn-1e'}):
        global tiwi_link
        tiwi_link = pre_download.get('href')
        #print(tiwi_link)

def get_hash(source):
    source_code = requests.get(source)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for download in soup.findAll(href='#', string='Normal quality'):
        videolink = download.get('onclick')
        global hash
        hash = 'http://tiwi.kiwi/dl?op=download_orig&id=' + videolink.split("'")[1] + '&mode=' + videolink.split("'")[3] + '&hash=' + videolink.split("'")[5]
        #print('hash: ' + hash)

def get_video_link(source):
    source_code = requests.get(source)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for last in soup.findAll('a',{'class': 'btn green'}):
        global video_link
        video_link = last.get('href')
        #print(video_link)

main(22, 22)