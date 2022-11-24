import xlwt

#创建workbook对象
workbook = xlwt.Workbook(encoding="utf-8")
#创建工作表
worksheet = workbook.add_sheet('sheet2')
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i, j,"%d * %d = %d"%(i+1,j+1,(i+1)*(j+1)))

workbook.save('student.xls')
