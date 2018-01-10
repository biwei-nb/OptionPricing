# encoding: utf-8

from sqlalchemy import create_engine, MetaData, Table, Column, TIMESTAMP
import datetime
import pandas as pd
from WindPy import w
import os
from data_access.db_data_collection import DataCollection

w.start()
# tradetype = 0  # 0:期货，1：期权
beg_date = datetime.date(2017, 6, 1)
end_date = datetime.date(2017, 12, 15)

engine = create_engine('mysql+pymysql://root:liz1128@101.132.148.152/mktdata_intraday',
                       echo=False)
conn = engine.connect()
metadata = MetaData(engine)
equity_index_intraday = Table('equity_index_mktdata_intraday', metadata, autoload=True)
option_mktdata_intraday = Table('option_mktdata_intraday', metadata, autoload=True)
dc =  DataCollection()

date_range = w.tdays(beg_date, end_date, "").Data[0]

for dt in date_range:
    dt_date = dt.date().strftime("%Y-%m-%d")
    dt_datetime = dt_date+' 09:30:00'
    res = option_mktdata_intraday.select(option_mktdata_intraday.c.dt_datetime == dt_datetime).execute()
    if res.rowcount > 0: continue
    print(dt_date)
    db_data = dc.table_option_intraday().wind_data_50etf_option_intraday(dt_date)
    if len(db_data) == 0: continue
    try:
        conn.execute(option_mktdata_intraday.insert(), db_data)
        print('inserted into data base succefully')
    except Exception as e:
        print(dt)
        print(e)
        continue

for dt in date_range:
    dt_date = dt.date().strftime("%Y-%m-%d")
    dt_datetime = dt_date + ' 09:30:00'
    id_instrument = 'index_50etf'
    res = equity_index_intraday.select((equity_index_intraday.c.dt_datetime == dt_datetime) &
                                       (equity_index_intraday.c.id_instrument == id_instrument)).execute()
    if res.rowcount > 0: continue
    windcode = "510050.SH"
    db_data = dc.table_index_intraday().wind_data_equity_index(windcode, dt_date,id_instrument)
    if len(db_data) == 0: continue
    try:
        conn.execute(equity_index_intraday.insert(), db_data)
        print('inserted into data base succefully')
    except Exception as e:
        print(dt)
        print(e)
        continue

for dt in date_range:
    dt_date = dt.date().strftime("%Y-%m-%d")
    dt_datetime = dt_date + ' 09:30:00'
    id_instrument = 'index_50sh'
    res = equity_index_intraday.select((equity_index_intraday.c.dt_datetime == dt_datetime) &
                                       (equity_index_intraday.c.id_instrument == id_instrument)).execute()
    if res.rowcount > 0: continue
    windcode = "000016.SH"
    db_data = dc.table_index_intraday().wind_data_equity_index(windcode, dt_date,id_instrument)
    if len(db_data) == 0: continue
    try:
        conn.execute(equity_index_intraday.insert(), db_data)
        print('inserted into data base succefully')
    except Exception as e:
        print(dt)
        print(e)
        continue

for dt in date_range:
    dt_date = dt.date().strftime("%Y-%m-%d")
    dt_datetime = dt_date + ' 09:30:00'
    id_instrument = 'index_300sh'
    res = equity_index_intraday.select((equity_index_intraday.c.dt_datetime == dt_datetime) &
                                       (equity_index_intraday.c.id_instrument == id_instrument)).execute()
    if res.rowcount > 0: continue
    windcode = "000300.SH"

    db_data = dc.table_index_intraday().wind_data_equity_index(windcode, dt_date,id_instrument)
    if len(db_data) == 0: continue
    try:
        conn.execute(equity_index_intraday.insert(), db_data)
        print('inserted into data base succefully')
    except Exception as e:
        print(dt)
        print(e)
        continue