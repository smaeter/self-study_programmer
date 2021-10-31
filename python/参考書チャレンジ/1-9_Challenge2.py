print("何か入力してください。入力した文字をCSVに出力します。")
qs = []
qs = input("文字：")

import csv

with open("test.csv","w",encoding="utf-8") as f:
    w = csv.writer(f,delimiter=",")
    w.writerow(qs)
