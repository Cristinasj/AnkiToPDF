from anki_export import ApkgReader
import pyexcel_xlsxwx

with ApkgReader('test.apkg') as apkg: 
    pyexcel_xlsxwx.save_data('test.xlsx', apkg.export, config={'format': None})