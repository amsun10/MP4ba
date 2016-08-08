from MovieHelper import CMovieHelper
from MyRequests import MyRequest
from Constants import *

if __name__ == '__main__':
    session = MyRequest()
    myMovieHelper = CMovieHelper(URL, dir_path="D:\\mp4ba_torrents", session=session)
    # set which page you want to download
    for i in range(1, 7):
        myMovieHelper.set_page_index(i)
        myMovieHelper.run()
    pass