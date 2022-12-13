# import akshare as ak

# futures_zh_daily_sina_df = ak.futures_zh_daily_sina(symbol="V2105")
# print(futures_zh_daily_sina_df)
import os
import akshare as ak
import pandas as pd
from tqdm import tqdm
from datetime import datetime

# get_futures_daily_df = ak.get_futures_daily(start_date="20220318", end_date="20221108", market="DCE")
# get_futures_daily_df.to_csv ("/root/akshare/future_raw_data.csv", mode="a" ,index = False, header=True,encoding='gb18030')

def main():
    data_root = '/root/data/zbf/cn_futures_daily_JQuant/future_raw_data_new/'
    df = pd.read_csv('/root/akshare/future_raw_data.csv')
    
    for idx, row in tqdm(df.iterrows()):

        date = datetime.strptime(str(row['date']),'%Y%m%d')
        date = date.strftime('%Y-%m-%d')
        line = str(date)+','+str(row['open'])+','+str(row['close'])+','+str(row['low'])+','+str(row['high'])+\
        ','+str(row['volume'])+',,,,,,,,'+str(row['open_interest'])+'\n'
        symbol = row['symbol'][:-4]

        the_file = os.path.join(data_root,symbol,row['symbol']+'.XDCE.csv')
        if (os.path.exists(the_file)):
            f = open(the_file,'a+')
            f.write(line)
            f.close()

        # file_name = data_root + row[0] +'.csv'
        # line = str(row[2]) + ','+row[1]+ '\n'
        # f = open(file_name,'a+')
        # f.write(line)
        # f.close()

main()