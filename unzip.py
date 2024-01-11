import os
import zipfile

folder = './v2/'
filelist = sorted(os.listdir(folder))

for fzip in filelist:
    if os.path.isfile(os.path.join(folder, fzip)):
        f = zipfile.ZipFile(folder+fzip, 'r')  # 压缩文件位置
        for file in f.namelist():
            f.extract(file, folder)  # 解压位置
        f.close()
    os.remove(folder+fzip)
