#!/usr/bin/python

import sys
import os

from string import Template

def usage():
    return """
dump blocks into single files named by height

python dump_blocks_into_single_files.py PATH_TO_ZCASH_CLI 
"""

def main():
    if len(sys.argv) < 2:
        print(" Error: insufficient arguments")
        print(usage())
        return 1
    
    zcash_cli_path = sys.argv[1]
    
    for i in range(0, 152):
        template = Template("$cli_path --regtest getblock $blockheight 0 > $height.txt")
        os.system(template.substitute(cli_path=zcash_cli_path, blockheight=i, height=i))

if __name__ == "__main__":
    main()