from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import music_database_scrape

app = Flask(__name__)

@app.route('/')
def index():
    paragraph_todisplay=main_p()
    g_dic,s_dic=music_database_scrape.main_db_load()
    return render_template('index.html',p_text=paragraph_todisplay+'ALFREDO IS HERE',g_dic=g_dic,s_dic=s_dic)


def main_p ():

    url2 ='https://www.billboard.com/articles/news/list/8545893/best-songs-of-2019-top-100'

    res2 = requests.get(url2)
    soup2 = BeautifulSoup(res2.text, 'html.parser')
    main_p = soup2.find('div',class_='longform__body-primary').find('p').get_text()
    main_p


    return main_p


if __name__ == '__main__':
    app.run(debug=True)