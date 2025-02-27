# Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"25717","system":"gprdproduct"},{"code":"46948","system":"gprdproduct"},{"code":"26529","system":"gprdproduct"},{"code":"34374","system":"gprdproduct"},{"code":"6","system":"gprdproduct"},{"code":"55","system":"gprdproduct"},{"code":"32896","system":"gprdproduct"},{"code":"19194","system":"gprdproduct"},{"code":"27696","system":"gprdproduct"},{"code":"47815","system":"gprdproduct"},{"code":"46699","system":"gprdproduct"},{"code":"34557","system":"gprdproduct"},{"code":"27926","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('loop-diuretics-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["loop-diuretics-furosemide---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["loop-diuretics-furosemide---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["loop-diuretics-furosemide---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
