from MovieHelper import CMovieHelper
from Constants import *

if __name__ == '__main__':

    myMovieHelper = CMovieHelper(URL, dir_path="D:\\mp4ba_torrents")
    # set which page you want to download
    for i in range(1, 125):
        myMovieHelper.set_page_index(i)
        myMovieHelper.run()
    pass