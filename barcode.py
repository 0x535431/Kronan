BARCODE="569054100002";

sum1 = 3 *( int(BARCODE[1]) + int(BARCODE[3]) + int(BARCODE[5]) + int(BARCODE[7]) + int(BARCODE[9]) + int(BARCODE[11]))
print(sum1)
sum2 = (int(BARCODE[0]) + int(BARCODE[2]) + int(BARCODE[4]) + int(BARCODE[6]) + int(BARCODE[8]) + int(BARCODE[10]))
print(sum2)
checksum_value = int(sum1) + int(sum2)
print(checksum_value)

checksum_digit = 10 - (checksum_value % 10)
if (checksum_digit == 10):
    checksum_digit = 0

print(checksum_digit)