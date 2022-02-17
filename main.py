import zipfile

zf = zipfile.ZipFile('english.apkg')
file = zf.open('collection.anki21')

# print(file.read)
print("funciono")