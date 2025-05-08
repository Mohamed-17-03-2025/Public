#!C:\Users\asafa\OneDrive\Desktop\Public\Ezhil\ezhil_env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ezhil==0.99','console_scripts','ezhili'
__requires__ = 'ezhil==0.99'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('ezhil==0.99', 'console_scripts', 'ezhili')()
    )
