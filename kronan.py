import json
from pymongo import MongoClient
import requests

# Egill scraper 569 0541 00101 4
# 569 Iceland 0541 olgerdinn 00101 Product number - 4 checksum

s = requests.session()
#html = s.get(html_page)

# Database Setup
client = MongoClient('localhost', 27017)
db = client['egillkrona']
collection = db['barcode']

# Barcode scan variables
COUNTRY = "569"
COMPANY = "0541"
PRODUCT_START = "01993"
PRODUCT_END = "99999"



for i in range(int(PRODUCT_START),int(PRODUCT_END)):
    BARCODE = COUNTRY + COMPANY + ("%05d" % (i))
    sum1 = 3 *( int(BARCODE[1]) + int(BARCODE[3]) + int(BARCODE[5]) + int(BARCODE[7]) + int(BARCODE[9]) + int(BARCODE[11]))
    sum2 = (int(BARCODE[0]) + int(BARCODE[2]) + int(BARCODE[4]) + int(BARCODE[6]) + int(BARCODE[8]) + int(BARCODE[10]))
    checksum_value = int(sum1) + int(sum2)

    checksum_digit = 10 - (checksum_value % 10)
    if (checksum_digit == 10):
        checksum_digit = 0
    BARCODE = BARCODE + str(checksum_digit)

    html_page = "http://appservice.kronan.is/KrAppVerdPerVoruJSON.ashx?BarcodeOrItem=" + BARCODE

    myjson = s.get(html_page).text
    if (len(myjson) == 2):
        #print("WE HAVE A ZERO AT " + str(i))
        continue
    try:
        item = json.loads(myjson)
        print("WE GOT A LIVE ONE!" + str(i))
        item['_id'] = str(BARCODE)
        collection.insert(item)
    except:
            print("DOCUMENT ALREADY EXITS")


    print(html_page)
