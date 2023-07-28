
import xlwings as xw

wb=xw.Book('Macro.xlsm')


login=wb.macro('Escrever')
login()

wb.save()


if len(wb.app.books)==1:
    wb.app.quit()
else:
    wb.close()


