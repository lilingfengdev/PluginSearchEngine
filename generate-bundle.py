import os
import shutil
import urllib.request
import zipfile
import platform

os.system("python3 -m pip install cn_bing_translator requests lxml pyinstaller")
if platform.system() == 'Windows':
    urllib.request.urlretrieve("https://github.com/upx/upx/releases/download/v4.2.4/upx-4.2.4-win64.zip",
                               "upx.zip")
    zip = zipfile.ZipFile("upx.zip")
    zip.extract("upx-4.2.4-win64/upx.exe", path=os.getcwd())
    shutil.move("upx-4.2.4-win64/upx.exe", os.path.join(os.getcwd(), "upx.exe"))

import PyInstaller.__main__


PyInstaller.__main__.run(["main.spec"])

