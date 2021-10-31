list = ["Top Gun","Risky Buisness","Minority Report"],["Taitanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]

import csv

with open("1-9_3.csv","w",newline = "") as f:
    w = csv.writer(f,delimiter=",")
    w.writerows(list)
