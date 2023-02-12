import pytube as pt
import openpyxl
import xlrd


pathToExcel = "C:/Users/r/Desktop/dev/python-test/0.xls"
#the excel file must be xls not other extension
wb = xlrd.open_workbook(pathToExcel)
sheet = wb.sheet_by_index(0)
max_col = sheet.nrows
i = 0

for i in range(0,max_col,1):
    ytt = sheet.cell_value(i, 0)
    print(ytt)
    yt = pt.YouTube(ytt)
    t = yt.streams.filter(only_audio=True)
    t[0].download()
    #it will save audio file as mp4 into the same folder. 
