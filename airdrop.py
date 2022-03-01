import itertools
import csv
import os
import subprocess
from os import listdir
from os.path import isfile, join

mintAdress = "" # your custom token contract address

fileName = "address.csv"

with open(fileName, 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f, delimiter='')
    line_count = 0
    for row in csv_reader:
        print(row[0])
        print(row[1])

        line_count += 1

        print(f'spl-token transfer --allow-unfunded-receipt --fund-receipient {mintAdress} {row[1]} {row[0]}')
        transferInstr = subprocess.run(["spl-token", "transfer", "--allow-unfunded-receipent", "--fund-receipent", mintAdress, row[1], row[0]], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        wf = open("txn-log.txt", "a")
        wf.write(transferInstr.stdout + transferInstr.stderr)
        wf.close()
f.close()