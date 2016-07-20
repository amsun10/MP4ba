from MovieHelper import CMovieHelper
from Constants import *

if __name__ == '__main__':

    myMovieHelper = CMovieHelper(URL)
    # set which page you want to download
    myMovieHelper.set_page_index(1)
    myMovieHelper.run()
    pass