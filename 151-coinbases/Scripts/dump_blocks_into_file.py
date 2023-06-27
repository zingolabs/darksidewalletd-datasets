#!/usr/bin/python

import sys
import os

from string import Template

def usage():
    return """
dump blocks into a darksidewalletd blocks URL file.

python dump_blocks_into_file.py PATH_TO_ZCASH_CLI file.txt
"""

def main():
    if len(sys.argv) < 3:
        print(" Error: insufficient arguments")
        print(usage())
        return 1
    
    zcash_cli_path = sys.argv[1]
    file_path = sys.argv[2]
    
    for i in range(0, 152):
        template = Template("$cli_path --regtest getblock $blockheight 0 >> $path")
        os.system(template.substitute(cli_path=zcash_cli_path, blockheight=i, path=file_path))

if __name__ == "__main__":
    main()