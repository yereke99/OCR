from xlsxwriter.workbook import Workbook
from data_base import cursor, db

def sql_2_excell(name):
    workbook = Workbook('{}.xlsx'.format(name))
    worksheet = workbook.add_worksheet()

    cursor.execute("SELECT * FROM CLIENT")
    my_sel = cursor.execute("SELECT * FROM CLIENT")

    for i, row in enumerate(my_sel):
        for j, value in enumerate(row):
            worksheet.write(i, j, value)

    cursor.execute("UPDATE CLIENT SET c = %s ", ("true"))
    db.commit()

    workbook.close()


