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

    def get_page_links(self, content):
        pat = "\"show.php\?hash=([a-z0-9]*)?\" target=\"_blank\"\>\r\n        ([\s\S]*?)\<\/a\>"
        match_object = re.findall(pat, content)

        if match_object:
            return match_object
        else:
            return []

    def get_download_url(self, hash_code):
        # link address is like:
        # http://www.mp4ba.com/down.php?date=1468040484&hash=02b44c7d83211ad922021bca1b8e0d9d66f25a48

        download_url = u"%sdown.php?date=%s&hash=%s" % (self.url, int(time.time()), hash_code)
        print download_url
        return download_url
        pass

    def download_torrents(self, path):
        pass

    def run(self):
        content = self.get_page_content()
        # print content
        links = self.get_page_links(content)

        for link in links:
            self.get_download_url(link[0])
        # print links
        pass


if __name__ == '__main__':
    myMovieHelper = CMovieHelper(URL)
    myMovieHelper.run()
    pass