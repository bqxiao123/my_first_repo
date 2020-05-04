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