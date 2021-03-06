# -*- coding:utf-8 -*-
import re
import os
import requests


class CMovieHelper(object):
    def __init__(self, url, page_index=0, dir_path=None, session=None):
        self.url = url
        self.page_index = "page=%d" % page_index
        self.dir_path = dir_path
        if not session:
            self.session = requests.session()
        else:
            self.session = session
        pass

    def set_page_index(self, index):
        self.page_index = "page=%d" % index

    def set_dir_path(self, dir_path):
        self.dir_path = dir_path

    def get_page_content(self):
        response = self.session.get(self.url, params=self.page_index)
        return response.text

    def get_download_links(self, content):
        pat = "\"(show.php\?hash=[a-z0-9]*)?\" target=\"_blank\"\>\r\n        ([\s\S]*?)\<\/a\>"
        match_object = re.findall(pat, content)

        links = []
        if match_object:
            sub_pat = "<a id=\"download\" href=\"([\s\S]*?)\">"
            for link in match_object:
                print self.url+link[0]
                sub_content = self.session.get(self.url + link[0]).text
                try:
                    download_link = re.findall(sub_pat, sub_content)[0]
                    links.append((self.url + download_link, link[1]))
                except IndexError:
                    raise

        return links

    def get_magnet_links(self, content):
        pat = "\"(show.php\?hash=[a-z0-9]*)?\" target=\"_blank\"\>\r\n        [\s\S]*?\<\/a\>"
        match_object = re.findall(pat, content)
        links = []
        if match_object:
            sub_pat = "<a id=\"magnet\" href=\"([\s\S]*?)\">"
            for link in match_object:
                sub_content = self.session.get(self.url+link).text
                try:
                    magnet_link = re.findall(sub_pat, sub_content)[0]
                    links.append(magnet_link)
                except IndexError:
                    raise
        return links

    def download_torrents(self, link, file_name=None):
        if not self.dir_path:
            self.dir_path = os.path.join(os.getcwd(), "torrents")

        if not os.path.isdir(self.dir_path):
            os.makedirs(self.dir_path)

        with DownloadRequest(session=self.session, url=link, path=self.dir_path, file_name=file_name, ext="torrent") as downloadHelper:
            path = downloadHelper.download()
            return True, path

    def run(self):
        content = self.get_page_content()
        # print content
        links = self.get_download_links(content)
        print links
        for link in links:
            self.download_torrents(link[0], file_name=link[1])
        pass

class DownloadRequest(object):
    def __init__(self, session=requests, url="", path="\\", file_name=None, ext=None):
        self.session = session
        self.url = url
        self.path = path
        self.ext = ext
        self.file_name = file_name
        self.response = None

    def download(self):
        print "downloading: %s" % self.url

        if self.file_name:
            local_filename = self.file_name
        else:
            local_filename = self.url.split('/')[-1]

        if self.ext:
            local_filename += ".%s" % self.ext

        local_file_path = os.path.join(self.path, local_filename)
        r = self.session.get(self.url)
        with open(local_file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=512 * 1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
        return os.path.abspath(local_file_path)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.response:
            del self.response
