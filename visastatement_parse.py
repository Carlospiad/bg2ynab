import csv

with open('data/MovimientoEstTexto.txt', newline='',encoding='latin-1') as csvfile:
  with open('data/bgynab.csv', 'w+') as csvout:
    writer = csv.writer(csvout, lineterminator='\n')
    cs = csv.reader(csvfile, delimiter=';', quotechar='"')
    next(cs, None)  # skip the first row from the reader, the old header
    writer.writerow(['Date','Payee','Category','Memo','Outflow','Inflow']) # write new header
    for line in cs:
        writer.writerow((line[2],'','',line[4].replace(",", ""),line[6].replace(",", ""),line[7].replace(",", "")))
