import zipfile
archive = zipfile.ZipFile('main.zip', 'r')
files=[f[:-3] for f in archive.namelist() if f.endswith(".py")]


with open('info.txt','w') as writer:
    writer.writelines("\n".join(sorted(files)))
