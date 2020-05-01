import getopt
import sys

from .file_utils import *

argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv, "d:s:f")
except getopt.GetoptError:
    print("Invalid input. TestCoverage -d <Directorypath> -s <searchFilter> -f(ull)")
    sys.exit(2)

full_search = False
for opt, arg in opts:
    if opt == '-d':
        dir_path = arg
    elif opt == '-s':
        search_filter = arg
    elif opt == '-f':
        full_search = True

find_test_files(dir_path, search_filter, full_search)
