import os
import sys
import wget
from datetime import date

if len(sys.argv) != 3:
    print("Please enter a start date and an end date.")
arg_start = sys.argv[1]
arg_end = sys.argv[2]
if len(arg_start) != 8 or len(arg_end) != 8:
    print("Please enter a valid date in the format of yyyyMMdd")
start_date = date(int(arg_start[0:4]), int(arg_start[4:6]), int(arg_start[6:8]))
end_date = date(int(arg_end[0:4]), int(arg_end[4:6]), int(arg_end[6:8]))

if not os.path.exists('./v2'):
    os.makedirs('./v2')
if not os.path.exists('./logs'):
    os.makedirs('./logs')

missinglog = open('./logs/missing.log', 'w')
with open('./masterfilelist.txt', 'r') as filelist:
    data = filelist.readlines()
    for line in data:
        tokens = line.split(' ')
        url = tokens[-1].strip()
        filename = url.split('/')[-1]
        
        if not filename.endswith('export.CSV.zip'):
            continue
        
        cur_date = date(int(filename[0:4]), int(filename[4:6]), int(filename[6:8]))
        if cur_date < start_date:
            continue
        if cur_date >= end_date:
            break
        
        print('Downloading: ' + filename)
        try:
            wget.download(url, './v2/' + filename)
        except Exception as e :
            missinglog.write('Missing:' + filename + '\n')
            print(e)
        print('Finished: ' + filename)
