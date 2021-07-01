from xlsxwriter.workbook import Workbook
from data_base import cursor, db

def _sql2excell(name):
    query = "SELECT * FROM CLIENT WHERE c = 'false'"
    cursor.execute(query)

    workbook = Workbook('{}.xlsx'.format(name))
    sheet = workbook.add_worksheet()

    for r, row in enumerate(cursor.fetchall()):
        for c, col in enumerate(row[:-1]):
            sheet.write(r, c, col)

    cursor.execute("UPDATE CLIENT SET  c = 'true'")
    db.commit()

    workbook.close()

def sql_2_excell(name):
    query = "SELECT * FROM client_za WHERE c = 'false'"
    cursor.execute(query)

    workbook = Workbook('{}.xlsx'.format(name))
    sheet = workbook.add_worksheet()

    for r, row in enumerate(cursor.fetchall()):
        for c, col in enumerate(row[:-1]):
            sheet.write(r, c, col)

    cursor.execute("UPDATE client_za SET  c = 'true'")
    db.commit()

    workbook.close()



