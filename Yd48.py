#-*- coding: UTF-8 -*-
import os
import sys
import argparse

from multiprocessing import Pool
from bs4 import BeautifulSoup
from urllib import parse,request


class Downloader(object):
    def __init__(self, elements):
        self.elements = elements
        
    def download(self, href):
        os.system('you-get "http:{0}"'.format(href))
              
    def go(self):
        soup = BeautifulSoup(open(self.elements, 'r'), 'lxml')
        urls = soup.find_all('a', class_ = 'video')
        for url in urls:
            print(url.get('title'))
        print("===============================================================")

        sign = input("确认下载以上公演? (yes/no):")

        if sign == "yes" or sign == "y" :

            p = Pool(4)
            for url in urls:

                p.apply_async(self.download, args = (url['href'],))

            p.close()
            p.join()
        else: 
            print("已取消下载！")
            sys.exit()
        

        

def getList(searchString,page):  

    youku_get = {'q':searchString,'page':page}
    youku_get = parse.urlencode(youku_get)
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
    url = 'http://i.youku.com/i/UMTM4NTM5Nzc4OA==/videos'
    req = request.Request(url='%s%s%s' % (url,'?',youku_get),headers=header_dict)
    res = request.urlopen(req)
    res = res.read()

    data_list_raw=res.decode(encoding='utf-8')

    data_list=data_list_raw.replace('</\div>','/\n').replace('target','class')
    
    with open("48.list","w") as f:
    
        f.write(data_list)


def usage():
    usage_info = '''
    Usage:
        1. input the team of SNH48G by adding -t
        2. input the page number of youku playlist by adding -p
        3. -h for help
    '''
    print(usage_info)

def logo():
    logo_info = '''
    
        欢迎使用SNH48G公演批量下载程序 Yd48 ！
                      
    '''
    print(logo_info)

def main():

    if len(sys.argv) < 2:
        usage()
        sys.exit()
    logo()
    parser = argparse.ArgumentParser()  
    parser.add_argument('-t','--team',help='input the Team of SNH48G or the date ')  
    parser.add_argument('-p','--page',help='input the page number from youku video web page')
    args = parser.parse_args()
    print("正在更新数据........")
    getList(args.team,args.page)
    print("即将为您下载以下公演:")
    print("===============================================================")

    downloader = Downloader("48.list")  
    downloader.go()

if __name__ == '__main__':
    main()