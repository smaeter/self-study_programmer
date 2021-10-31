list = ["トップガン","リスキー　ビジネス","マイノリティ　レポート"],["タイタニック","ザ・リベレント","インセプション"],["トレーニング・デイ","炎の男","フライト"]

import csv

with open("1-9_4.csv","w",encoding="utf=8",newline = "") as f:
    w = csv.writer(f,delimiter=",")
    w.writerows(list)
    
