import glob
# glob.glob("/test_dir/dir_A/*")

# Windowsでは'\\'でもディレクトリを区切れます
# glob.glob("\\test_dir\\dir_A\\*")

# 相対パスでも指定可能です
import os
os.chdir("/Users/s-han/git/python_panda")
glob.glob("./*")
print(glob.glob("*"))