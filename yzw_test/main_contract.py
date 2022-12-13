import akshare as ak
import datetime
import os
import pandas as pd
from tqdm import tqdm
def f1():
    futures_spot_price_previous_df = ak.futures_spot_price_previous('20190318')
    df = futures_spot_price_previous_df[['商品','主力合约代码']]
    print(df[df['商品']=="铜"])
def f2():
    futures_spot_price_df = ak.futures_spot_price("20190318")
    df = futures_spot_price_df[['symbol','dominant_contract']]
    print(df[df['symbol']=="CU"])
def next_day(string):
    the_day = datetime.datetime.strptime(string, '%Y%m%d')
    next_day = the_day+datetime.timedelta(days=1)
    next_day_str = str(next_day.strftime("%Y%m%d"))
    return next_day_str
def f3(symbles):
    futures_spot_price_daily_df = ak.futures_spot_price_daily(start_day="20220319", end_day="20221108", vars_list=symbles)
    df = futures_spot_price_daily_df[['symbol','dominant_contract','date']]
    return df 
def get_all_main_contract():
    data_root = '/root/data/zbf/cn_futures_daily_JQuant/main_contract'
    all_symble_file =os.listdir(data_root)
    all_symble_file.sort()
    print("how many symble: ",len(all_symble_file))
    # all_symble = []
    # for i,symble_file in enumerate(all_symble_file):
    #     symble = symble_file[:-4]
    #     all_symble.append(symble)
    # df = f3(all_symble)
    # df.to_csv ("/root/akshare/test.csv", mode="a" ,index = False, header=False,encoding='gb18030')
def main():
    data_root = '/root/data/zbf/cn_futures_daily_JQuant/main_contract_new/'
    df = pd.read_csv('/root/akshare/test.csv', header=None)
    for idx, row in tqdm(df.iterrows()):
        file_name = data_root + row[0] +'.csv'
        line = str(row[2]) + ','+row[1]+ '\n'
        f = open(file_name,'a+')
        f.write(line)
        f.close()






get_all_main_contract()
main()

