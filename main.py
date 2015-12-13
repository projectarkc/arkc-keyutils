#! /usr/bin/env python3

# By ArkC developers
# Released under GNU General Public License 2

import argparse

from common import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="ArkC Key Utilities")
    # Load arguments
    #parser.add_argument("-v", dest="v", action="store_true", help="show detailed logs")
    parser.add_argument('-gs', '--get-SHA1', dest="gs", help="Get sha1 of a public or private key file")
    options = parser.parse_args()
    if options.gs:
        try:
            key_data = open(options.gs, "r").read()
            key = certloader(key_data).importKey()
            key_sha1 = certloader(key_data).getSHA1()
            print(key_sha1)
        except Exception as err:
            print ("Fatal error while loading local certificate.")
            print (err)
            quit()
                