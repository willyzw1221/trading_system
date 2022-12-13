import akshare as ak

get_futures_daily_df = ak.get_futures_daily(start_date="20200701", end_date="20200716", market="DCE")
print(get_futures_daily_df)

print(get_futures_daily_df.columns)
