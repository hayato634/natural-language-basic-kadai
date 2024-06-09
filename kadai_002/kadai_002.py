# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 15:21:25 2024

@author: z574z
"""

#%%

## 　Beautiful Soup4
pip install bs4

# Step1. 文章のスクレイピング
from bs4 import BeautifulSoup
from urllib import request

url = 'https://www.aozora.gr.jp/cards/000148/files/2371_13943.html'
response = request.urlopen(url)
soup = BeautifulSoup(response)
response.close()

print(soup)



# Step2. HTMLタグや不要な文字列の削除(クリーニング)
# タグの削除:タグ（class属性が"main_text"）となっている部分だけを取り出す
main_text = soup.find('div', class_='main_text')
print(main_text)

# 特定のタグとその内容を削除

# get_textメソッドで人が読めるような形式でテキストを抜き出す
main_text = main_text.get_text()
print(main_text)


# 最後に正規表現を用いて、改行や全角空白をテキストクリーニング
import re
main_text = re.sub(r"[\u30000 \n \r]", "", main_text)
print(main_text)

# ストップワードを除去
from bs4 import BeautifulSoup
from urllib import request

# Beautiful Soup4とurllibを使用して,SlothLibのテキストページからストップワードの辞書を取得
url = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
response = request.urlopen(url)
soup = BeautifulSoup(response)
response.close()

print(soup)

# このままの状態では使用できないので、HTMLタグなどを削除
stopwords_text = soup.text
print(stopwords_text)

# 改行コードなどが入っているため、テキストクリーニングを行う
stopwords_list = stopwords_text.split("\r\n")
stopwords_list = [word for word in stopwords_list if word]
print(stopwords_list)

# ストップワードによる除去
delete_stop_words = [word for word in main_text if word not in stopwords_list]
print(delete_stop_words)




