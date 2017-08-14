import pprint

import os
import psycopg2
import openpyxl
from DBConnection import DBConnection
from dotenv import load_dotenv, find_dotenv

from models.Transaction import Transaction
conn = DBConnection().get_connection()


pp = pprint.PrettyPrinter(indent=4)
wb = openpyxl.load_workbook('golden_one_example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
obs = []
for row in range(2, sheet.max_row + 1):
    transaction_date = sheet['A' + str(row)].value
    amount = sheet['B' + str(row)].value
    description = sheet['C' + str(row)].value
    running_total = sheet['D' + str(row)].value
    tran = Transaction(transaction_date, amount, description, running_total)
    obs.append(Transaction(transaction_date, amount, description, running_total))
    tran.save(conn)

conn.close()
