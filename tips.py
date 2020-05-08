# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:38:18 2019

@author: admin

"""
#################################################################
#github操作步骤：
#git add .             -----------添加所有修改
#git commit -m "xxxxx" -----------提交到临时仓库
#git push              -----------推送至github对应的repositories
#################################################################
#%%
import os
os.getcwd()                         # get current working directory 获取当前工作目录 
os.chdir('D:\\github\\my_first_repo')    # change working directory 加上路径便可更改工作目录
#%%
import pandas as pd
pd.set_option ('display.max_columns', 200)
pd.set_option ('display.max_rows', 200)
pd.set_option ('display.width', 1000)
pd.set_option('mode.chained_assignment', None)
pd.set_option ('display.precision', 2)
pd.set_option ('display.float_format','{:, 6f}'.format)
import warnings
warnings.filterwarnings('ignore')

#%%


##write pd.DataFrame to xlsx file with sheet_name
data.to_excel("output.xlsx",sheet_name='tseq')

#%%
print('ab%s%s' %(5,5))#格式输出
#%%
#列表两种操作方式：
#列表推导式总共有两种形式：
#[x for x in data if condition] 此处if主要起条件判断作用，data数据中只有满足if条件的才会被留下，最后统一生成为一个数据列表
#[exp1 if condition else exp2 for x in data] 此处if…else主要起赋值作用，当data中的数据满足if条件时将其做exp1处理，否则按照exp2处理，最后统一生成为一个
x=[1,2,3,4,5,6]
print([a for a in x if a > 2])

print([a if a < 3 else 3 for a in x])



#%%
import pandas as pd
a=pd.DataFrame([[0,1,2,3,'x'],[2,3,4,5,'t'],[3,4,8,9,'p']],dtype=float,columns=['a','b','c','d','char'])
#a.astype(float)
#a.filter().eq(2.0).any(axis=0)
a.sample(n=2,axis=1)
a.select_dtypes(include=['object'])#['nuumber']
#(a.isnull().sum()/a.shape[0]*100,2).sort_value(ascending=False)#查看每列缺失情况

#%%
#根据分位数计算异常值上下界：
lower=data.quantile(q=(1-0.9)/2)
higher=data.quantile(q=(1+0.9)/2)
#%%
#生成并处理时间数据
import pandas as pd
data_list=pd.date_range(start='2017-01-01',end='2019-05-01',freq='M')
[str(x)[0:7].replace('-','') for x in data_list]
#%%
#按照q=[0.,0.2,.....1.0]切割分组，也可以设定分组数目直接分类，duplicates=‘drop’丢弃重复边界
pandas.qcut(x, q, labels=None, retbins=False, precision=3, duplicates='raise')
#按照bins--list进行分类，bins列出分类边界，也可以设定分组数目直接分类
pandas.cut(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise')
#%%
##打开画布，可以画多福图，每幅图对应不同的axes
#
import matplotlib.pyplot as plt
figure,axes1=plt.subplots()
axes1.plot(range(20))
figure,axes2=plt.subplots()
axes2.plot(range(30))
axes1.plot(range(10))

ax3 = plt.subplot(313, sharex=ax1, sharey=ax1) # share x轴和y轴
ax1.xaxis.tick_top()#x轴刻度置顶
ax1.set_xticks([]) #不显示坐标刻度
ax1 = plt.subplot2grid((3, 1), (0, 0),rowspan=2,sharex=ax2)
plt.subplots_adjust(wspace =0, hspace =0)#调整子图间距

#同一幅图画多福子图
#%%
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(range(50))
plt.subplot(1,2,2)
plt.plot(range(5))

plt.figure()
plt.plot(range(1000))

#%%
plt.xticks(np.arange(10),list(字符),rotation=45)#设定刻度显示值，这个值是个list
ax1.set_xticks([]) #不显示坐标刻度
plt.tick_params(labelsize=20) #设定刻度大小    
plt.xlabel('xx',fontsize=20)
plt.ylabel('yy',fontszie=20)
"""
解决python pyplot作图中文乱码的问题
如果没有中文字符库，将中文字符库SimHei.ttf拷贝到当前路径
"""
ttf_path='SimHei.ttf'
myfont=FontProperties(fname=ttf_path)
plt.title('title',fontproperties=myfont,fontsize=20)

#%%
##np.vstack,
##np.array().flatten,
##np.array().values.astype('')
x1=app_train.iloc[0,0:10].values.astype('float')
x2=app_train.iloc[0,10:20].values.astype('float')
dd=pd.DataFrame({'x1':x1,'x2':x2})
dd1=dd.sort_values(by='x1')
print(dd1)
dd2=dd1.reset_index(drop=True).values.flatten()
dd3=dd2
print(type(dd2),'.........')
np.vstack((dd3,dd2))


#%%
#dataframe去重
import pandas as pd
a=pd.DataFrame({'a':[1,2,2],'b':[2,3,4]})
a[a.duplicated(subset='a',keep='first')]


#%%
#dataframe格式转换
import pandas as pd
s = pd.Series(['1', '2', '4.7', 'pandas', '10'])
s=pd.to_numeric(s, errors='coerce')#只能处理一维数据
a=pd.DataFrame({'a1':['1','2','6','a'],'a2':['2','b','2','9']})
a=a.apply(pd.to_numeric, errors='coerce')

Lcap=Lcap[Lcap['time'].str.contains('08:00')].reset_index(drop=True)#根据字符内容筛选dataframe
#%%
#日期格式转换
import datetime
import time
from dateutil.relativedelta import relativedelta
#时间（字符串）
date='201806'
#字符转时间
x=datetime.datetime.strptime(date,'%Y%m')
#时间加减
x1=x+relativedelta(months=+6)
#时间转字符
str_date=x1.strftime('%Y%m')



print(str_date)


#%%
#对dataframe进行格式化
df['Open'] = df['Open'].map('{:,.2f}'.format)
df['High'] = df['High'].map('{:,.2f}'.format)
df['Low'] = df['Low'].map('{:,.2f}'.format)
df['Close'] = df['Close'].map('{:,.2f}'.format)
df['Adj Close'] = df['Adj Close'].map('{:,.2f}'.format)
a=0.00002
'{0:.2E}'.format(a)

'i am %s,i am %u age old' %('xiao',40)
'i am {0},i am {1} age old'.format('xiao',40)
df.applymap('{:,.2f}'.format) #------applymap 主要是针对df的每个元素
df.apply('{:,.2f}'.format) #---------apply 主要是基于整列操作，所以这儿会报r错。


#--list map 函数操作方法例子
import numpy as np
import pandas as pd
df=pd.DataFrame({'a':[1,2,np.nan,4],'a1':[0.5,0.5,0.5,0.5]})
print('origin df')
print(df)
print()
df.iloc[:,1]=list(map(lambda x,y:0 if np.isnan(x) else y, df.iloc[:,0],df.iloc[:,1]))
print('after map df')
print(df)
#%%
#%% f-string 用法
name = 'Eric'
f'Hello, my name is {name}'

price = 19.99
f'The price of this book is {price}'

#f-string的大括号 {} 可以填入表达式或调用函数，Python会求出其结果并填入返回的字符串内：
f'A total number of {24 * 8 + 4}'

#f-string大括号内所用的引号不能和大括号外的引号定界符冲突，可根据情况灵活切换 ' 和 "：
#若 ' 和 " 不足以满足要求，还可以使用 ''' 和 """
f'I am {"Eric"}'
f"""He said {"I'm Eric"}"""
f'''He said {"I'm Eric"}'''
#%%
#f-string用大括号 {} 表示被替换字段，其中直接填入替换内容：

###### plot twinx()###### 
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    # ax1
    p1 = ax1.bar(ind, binx['good_distr'], width, color=(24/254, 192/254, 196/254))
    p2 = ax1.bar(ind, binx['bad_distr'], width, bottom=binx['good_distr'], color=(246/254, 115/254, 109/254))
    for i in ind:
        ax1.text(i, binx.loc[i,'count_distr']*1.02, str(round(binx.loc[i,'count_distr']*100,1))+'%, '+str(binx.loc[i,'count']), ha='center')
    # ax2
    ax2.plot(ind, binx['badprob'], marker='o', color='blue')
    for i in ind:
        ax2.text(i, binx.loc[i,'badprob']*1.02, str(round(binx.loc[i,'badprob']*100,1))+'%', color='blue', ha='center')
    # settings
    ax1.set_ylabel('Bin count distribution')
    ax2.set_ylabel('Bad probability', color='blue')
    ax1.set_yticks(np.arange(0, y_left_max+0.2, 0.2))
    ax2.set_yticks(np.arange(0, y_right_max+0.2, 0.2))
    ax2.tick_params(axis='y', colors='blue')
    plt.xticks(ind, binx['bin'])
    plt.title(title_string, loc='left')
    plt.legend((p2[0], p1[0]), ('bad', 'good'), loc='upper right')
    # show plot 
    # plt.show()


#%%
import pandas as pd
r = [[0,2],[2,4],[4,6],[6,8]]
i = [pd.Interval(x[0],x[1]) for x in r]
df = pd.DataFrame({"x":["a","b","a","b"],"i":i})



#%%
#时间序列例子https://blog.csdn.net/qq_40587575/article/details/81205873

d = ['xiaoquanbao']

while True:
	name = input('请输入您的用户名：')
	if name in d:
		break
	else:
		print('您输入的用户名不存在，请重新输入')
		continue
    
count = 5
while count:
	password = input('请输入您的密码：')
	if d[name] == password:
		print('进入系统')
		break
	else:
		count -= 1
		print('您输入的密码不正确，还有{}次输入机会'.format(count))
		continue

#%%
import pandas as pd
s = pd.Series(data=[1, None, 4, 1],
              index=['A', 'B', 'C', 'D'])
#s.argmin()
s.idxmin()

s1=pd.DataFrame(s,columns=['test'])
s1.idxmin()

#%%
#-------LabelEncoder -----------------------
from sklearn import preprocessing
encode = preprocessing.LabelEncoder()
encode.fit_transform(['one', 'two', 'three']) # encoding .................
keys = encode.classes_                        # encoding class .............
values = encode.transform(encode.classes_)
dictionary = dict(zip(keys, values))
print(dictionary)

#%%
import pandas as pd
data=pd.read_csv('D:\\github\\my_first_repo\\data\\train_data.csv')
data.info()
xx=data[['x_027','x_028']]
xx.corr(method='kendall') #用于反映分类变量相关性的指标
xx.corr(method='pearson') #默认值，线性相关--判断两个变量是否在一条直线上
xx.corr(method='spearman') #秩相关。
