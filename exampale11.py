#csv file: comma separated value:

import csv

with open("myfile.csv","w") as f:
    writer_row=csv.writer(f)

    #setheder
    writer_row.writerow(["id","name","subject","score"])

    #store record

    writer_row.writerow([1,'Raja','Mony','100'])
    writer_row.writerow([2,'jig','bdg','10000'])