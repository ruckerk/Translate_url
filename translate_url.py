from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from google_trans_new import google_translator  
import re

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

def translate_page(url_in,lang2= 'es'):
    html = urllib.request.urlopen(url).read()
    txt = text_from_html(html)

    translator = google_translator()  
    output = list()

    for i in re.split('\.|\!|\?',txt):
        output = output+ [translator.translate(i,lang_tgt=lang2)]
    return output

# EXAMPLE
#def main():
#    url = 'https://datacarpentry.org/python-ecology-lesson/00-before-we-start/index.html'#
#    t_text = translate_page(url)
#    with open('translated_page.txt', 'w') as filehandle:
#        for listitem in t_text:
#            filehandle.write('%s\n' % listitem)
