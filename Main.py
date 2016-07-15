# -*- coding:utf-8 -*-
import requests
import re
import time

from Constants import *


class CMovieHelper(object):
    def __init__(self, url, page_index=0):
        self.url = url
        self.page_index = "page=%d" % page_index
        pass

    def set_page_index(self, index):
        self.page_index = index

    def get_page_content(self):
        response = requests.get(self.url, self.page_index)
        return response.text

    def get_download_links(self, content):
        pat = "\"show.php\?hash=([a-z0-9]*)?\" target=\"_blank\"\>\r\n        ([\s\S]*?)\<\/a\>"
        match_object = re.findall(pat, content)

        links = []
        if match_object:
            for hash_code in match_object:
                download_url = u"%sdown.php?date=%s&hash=%s" % (self.url, int(time.time()), hash_code[0])
                links.append(download_url)

        return links

    def get_magnet_links(self, content):
        pat = "\"(show.php\?hash=[a-z0-9]*)?\" target=\"_blank\"\>\r\n        [\s\S]*?\<\/a\>"
        match_object = re.findall(pat, content)
        print match_object
        links = []
        if match_object:
            sub_pat = "<a id=\"magnet\" href=\"([\s\S]*?)\">"
            for link in match_object:
                sub_content = requests.get(self.url+link).text
                try:
                    magnet_link = re.findall(sub_pat, sub_content)[0]
                    links.append(magnet_link)
                except IndexError:
                    raise
        return links

    def download_torrents(self, path):
        pass

    def run(self):
        content = self.get_page_content()
        # print content
        links = self.get_download_links(content)
        print links

        links = self.get_magnet_links(content)
        print links

        pass


if __name__ == '__main__':
    myMovieHelper = CMovieHelper(URL)
    myMovieHelper.run()
    pass