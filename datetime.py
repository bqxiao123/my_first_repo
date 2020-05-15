# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:56:13 2020

@author: admin
"""

import numpy as np
import pandas as pd
from datetime import datetime 
from datetime import timedelta
#字符串和时间的转换
stamp = datetime(2018, 7, 25)           #------------------define datetime var
print(str(stamp))                       # -----------------to string
stamp1 = stamp.strftime('%Y-%m-%d')     #------------------datetime var to string by format as ....
print(stamp1)
value = '2018-1-12'
strp_time = datetime.strptime(value, '%Y-%m-%d') #---------string 2 datetime by format
print(strp_time) 
#%% 
#timestamp  
timestamp = 1528797322                          #----------timestamp
date_time = datetime.fromtimestamp(timestamp)   #----------timestamp to datetime
print(date_time)
# more format with datetime
stamp = datetime(2018, 7, 25, 10, 20,15) 
stamp.strftime('%A')
#..................................
#%a 星期几的简写;如 星期三为Web 
#%A 星期几的全称;如 星期三为Wednesday 
#%b 月份的简写; 如4月份为Apr 
#%B 月份的全称; 如4月份为April 
#%c 标准的日期的时间串;（如： 04/07/10 10:43:39） 
#%C 年份的后两位数字 
#%d 十进制表示的每月的第几天 
#%D 月/天/年 
#%e 在两字符域中，十进制表示的每月的第几天 
#%F 年-月-日 
#%g 年份的后两位数字，使用基于周的年 
#%G 年分，使用基于周的年 
#%h 简写的月份名 
#%H 24小时制的小时 
#%I 12小时制的小时 
#%j 十进制表示的每年的第几天 
#%m 十进制表示的月份 
#%M 十时制表示的分钟数 
#%n 新行符 
#%p 本地的AM或PM的等价显示 
#%r 12小时的时间 
#%R 显示小时和分钟：hh:mm 
#%S 十进制的秒数 
#%t 水平制表符 
#%T 显示时分秒：hh:mm:ss 
#%u 每周的第几天，星期一为第一天 （值从0到6，星期一为0） 
#%U 第年的第几周，把星期日做为第一天（值从0到53） 
#%V 每年的第几周，使用基于周的年 
#%w 十进制表示的星期几（值从0到6，星期天为0） 
#%W 每年的第几周，把星期一做为第一天（值从0到53） 
#%x 标准的日期串 
#%X 标准的时间串 
#%y 不带世纪的十进制年份（值从0到99） 
#%Y 带世纪部分的十制年份 
#%z，%Z 时区名称，如果不能得到时区名称则返回空字符。 
#%%
#时间序列基础
import pandas as pd 
import numpy as np
from datetime import datetime
dates = [datetime(2011,1,2), datetime(2011,1,5),
        datetime(2011,1,7), datetime(2011,1,8),
        datetime(2011,1,10), datetime(2011,1,12)
         ]
np.random.seed(666)
ts = pd.Series(np.random.randn(6), index = dates)   #使用时间戳作为索引
print(ts)
print(ts.index) 
print(ts[ts.index[2]])  # 1.1734680120920244 选取第三行的元素
print(ts['20110105'])   # 0.47996600310104814
 
#对于较长的时间序列， 可以传入年， 或者 月来进行索引
longer_date = pd.Series(np.random.randn(1000), index = pd.date_range('2012-01-01', periods=1000))
print(longer_date.shape)    # (1000,)
print(longer_date[:3])  #打印出前3项出来
# 2012-01-01    0.019028
# 2012-01-02   -0.943761
# 2012-01-03    0.640573
# Freq: D, dtype: float64
print(longer_date['2014'][:3])  #依据年份进行索引， 打印出前3 项
# 2014-01-01    1.154235
# 2014-01-02    0.360002
# 2014-01-03   -1.197186
# Freq: D, dtype: float64
print(longer_date['2014-05'][:3])   #依据年 月
# 2014-05-01   -0.036317
# 2014-05-02    0.134003
# 2014-05-03   -0.863556
# Freq: D, dtype: float64
 
#使用时间戳进行切片
print(longer_date['2014-03-03':'2014-03-06'])   #可以看到 3号 和 6 号都包括了
# 2014-03-03   -1.157900
# 2014-03-04    0.690954
# 2014-03-05    2.187638
# 2014-03-06   -0.194585
# Freq: D, dtype: float64
 
print(ts.truncate(after = '1/6/2011'))  #定义最后一项是2011 -1-6 选取之前的日期
# 2011-01-02    0.824188
# 2011-01-05    0.479966
# dtype: float64
#%%
##重复索引的时间序列
dates  = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', 
                          '1/2/2000', '1/3/2000'])
dup_ts = pd.Series(np.random.randn(5), index = dates)
print(dup_ts)
# 2000-01-01    0.721593
# 2000-01-02   -0.024682
# 2000-01-02   -0.813268
# 2000-01-02   -2.478950
# 2000-01-03    0.497203
# dtype: float64
print(dup_ts.index.duplicated())# [False False  True  True False]
print(dup_ts.index.is_unique)   # False 代表不是唯一的 
 
#聚合具有重复时间戳的数据， 一种方法是 groupby  使得 level = 0
grouped = dup_ts.groupby(level=0)
print(grouped.mean())       #计算相同时间的 平均值
# 2000-01-01    0.721593
# 2000-01-02   -1.105633
# 2000-01-03    0.497203
# dtype: float64
print(grouped.count())  #计算出现的次数
# 2000-01-01    1
# 2000-01-02    3
# 2000-01-03    1
# dtype: int64

#%%
##日期的范围，频率以及移动
import pandas as pd 
import numpy as np
from datetime import datetime
dates = [datetime(2011,1,2), datetime(2011,1,5),
        datetime(2011,1,7), datetime(2011,1,8),
        datetime(2011,1,10), datetime(2011,1,12)
         ]
np.random.seed(666)
ts = pd.Series(np.random.randn(6), index = dates)   #使用时间戳作为索引
print(ts)
# # 2011-01-02    0.824188
# # 2011-01-05    0.479966
# # 2011-01-07    1.173468
# # 2011-01-08    0.909048
# # 2011-01-10   -0.571721
# # 2011-01-12   -0.109497
# # dtype: float64
#%%
resampler = ts.resample('D')    #下面会更深入地讲
print(resampler)
#生成日期的范围
index = pd.date_range('2012-04-01','2012-06-01')    #只传入起始和结束时间
print(index[:5])
# DatetimeIndex(['2012-04-01', '2012-04-02', '2012-04-03', '2012-04-04',
#                '2012-04-05'],
#               dtype='datetime64[ns]', freq='D')
pd.date_range(end='2012-06-01', periods=20) # 输入结束时间也可以输入 start， 打印出20 个时间戳
#设定频度 freq
print(pd.date_range('2000-01-01','2000-12-01', freq = 'BM'))    #设置频度为每个月的最后一个工作日
# DatetimeIndex(['2000-01-31', '2000-02-29', '2000-03-31', '2000-04-28',
#                '2000-05-31', '2000-06-30', '2000-07-31', '2000-08-31',
#                '2000-09-29', '2000-10-31', '2000-11-30'],
#               dtype='datetime64[ns]', freq='BM')
 
#将时间戳进行归一化，将秒 进行清零
nor_date = pd.date_range('2015-05-02 12:50:21', periods = 5, normalize=True)
print(nor_date)
# DatetimeIndex(['2015-05-02', '2015-05-03', '2015-05-04', '2015-05-05',
#                '2015-05-06'],
#               dtype='datetime64[ns]', freq='D')
print(nor_date[0])  # 2015-05-02 00:00:00 可以看到分钟，秒都归为0 了

#%%




