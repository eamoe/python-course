from email.mime import base
from bs4 import BeautifulSoup
from importlib.resources import path
from pickle import TRUE
from turtle import clear
from typing import List
import requests
import hashlib

base_url = "https://www.mountaingoatsoftware.com"
blog_add = "/blog"# + '/P24'
blog_html_path = "html_parser/blog.html"
output_file = "html_parser/blog.csv"


def get_html(base_url, blog_add):
    resp = requests.get(base_url + blog_add)
    html_content = resp.text
    return html_content


def write_data_to_file(path, data, action):
    file = open(path, action)
    file.write(data)
    file.close()


def get_page_articles(path):
    articles_dict = {}
    with open(path) as obj:
        data = BeautifulSoup(obj, "html.parser")
        for article_body in data.find_all('article'):
            link = article_body.div.a['href']
            #if str(link).find('/blog') == -1 \
            #    and str(link).find('/presentations') == -1 \
            #    and str(link).find('/articles') == -1 \
            #    and str(link).find('/reviews') == -1:
            #    print(link)
            if str(link).find('/blog') != -1 \
                or str(link).find('/presentations') != -1 \
                or str(link).find('/articles') != -1 \
                or str(link).find('/reviews') != -1:
                article_title = article_body.h3.text
                description = "Description is not found!"
                publication_date = "Date is not found!"
                try:
                    description = article_body.p.text
                    publication_date = article_body.time.text
                except:
                    pass
                article_address = base_url + article_body.div.a['href']
                articles_dict[article_address] = [article_title, description, publication_date]
    return articles_dict


def dict_to_str(dict, output_str = ""):
    for key, value in dict.items():
        title = str(value[0]).replace(";", " ").replace("\n", "")
        description = str(value[1]).replace(";", " ").replace("\n", "")
        date = value[2]
        if date == "Dec 11, 2018":
            description = "Description is not found!"
        article_hash = hashlib.md5((date + title + description + key).encode('utf-8')).hexdigest()
        output_str += f"{article_hash};{date};{title};{description};{key}\n"
    return output_str


exit_app = False
add_url = blog_add
increment = 0
write_data_to_file(output_file, f"Hash;Publication Date;Title;Description;Link\n", 'a')
while not exit_app:
    blog_html_data = get_html(base_url, add_url)
    write_data_to_file(blog_html_path, blog_html_data, 'w')
    articles_dict = get_page_articles(blog_html_path)
    data_str = dict_to_str(articles_dict)
    if data_str == "":
        exit_app = True
    write_data_to_file(output_file, data_str, 'a')
    print(f"Processed articles: {increment + 12}")
    increment += 12
    add_url = blog_add + '/P' + str(increment)

print("Success!")