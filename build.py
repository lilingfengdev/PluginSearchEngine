import os
import shutil
import subprocess
import sys
import urllib.request
import zipfile
import platform

if platform.system() == 'Windows':
    urllib.request.urlretrieve("https://github.com/upx/upx/releases/download/v4.2.4/upx-4.2.4-win64.zip",
                               "upx.zip")
    zip = zipfile.ZipFile("upx.zip")
    zip.extract("upx-4.2.4-win64/upx.exe", path=os.getcwd())
    shutil.move("upx-4.2.4-win64/upx.exe", os.path.join(os.getcwd(), "upx.exe"))

os.mkdir("build")
os.mkdir("dist")


def build(filepath):
    args = ["python", "-m", "nuitka", "--onefile", filepath, "--assume-yes-for-downloads", "--output-dir=build"]
    if platform.system() == 'Windows':
        args.append("--windows-icon-from-ico=favicon.png")
        args.append("--enable-plugins=upx")
        args.append("--upx-binary=upx.exe")
    if platform.system() == 'MacOS':
        args.append("--macos-app-icon=favicon.png")
    if platform.system() == 'Linux':
        args.append("--linux-icon=favicon.png")
    args.append("--windows-console-mode=disable")
    args.append("--enable-plugin=pyside6")
    subprocess.call(args)
    filename = os.path.splitext(os.path.basename(filepath))[0]
    for f in os.listdir(os.path.join(os.getcwd(), "build")):
        if f.startswith(filename) and not os.path.isdir(os.path.join(os.getcwd(), "build", f)):
            shutil.move(os.path.join(os.getcwd(), "build", f), os.path.join(os.getcwd(), "dist", f))


build("main/main.py")

# 傻逼
# 狗屎代碼
