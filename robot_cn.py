import pandas as pd
import os
import pandas_datareader.data as web
import datetime
import fix_yahoo_finance as yf
'''
deleted stock:
600145: 停牌王，已经不能被雅虎财经识别为股票了。。。
600485: 停牌太久
'''


def get_data(stocks_data_frame, start=datetime.datetime(2009, 1, 1), end=datetime.datetime(2018, 12, 31)):
    total = len(stocks_data_frame['A股代码'])
    finished = 1
    for code in stocks_data_frame['A股代码']:
        temp = code
        if os.path.exists(code + '.csv'):
            finished += 1
            print('\r%d/%d  We are downloading %s' % (finished, total, code), end='', flush=True)
            continue    # this line is try to continue the work finished
        print('\r%d/%d  We are downloading %s' % (finished, total, code), end='', flush=True)
        try:
            data = web.get_data_yahoo(code+'.SZ', start, end)  # when downloading SS, change this line into 'SS'
        except:
            pass
            error_log = open('error_log.txt', 'a+')  # create an error log
            error_log.write(temp+'\n')
            error_log.close()
            finished += 1
            continue
        data.reset_index(inplace=True)
        data.to_csv(code+'.csv', index=False)
        finished += 1


def get_all_data(market_name):
    os.chdir(root_dir)
    df = pd.read_csv(market_name+'.csv', dtype=str)    # When opening SS.csv, please use 'GBK' for encoding
    os.chdir('./'+market_name)
    print('Now we are downloading %s' % market_name)
    get_data(df)


# yf.pdr_override()   # core process of yf, giving internet support to visit yahoo finance

# start = datetime.datetime(2009, 1, 1)
# end = datetime.datetime(2018, 12, 31)
# market_list = {'SS'}
market_list = {'SZ'}
# save root dir of the project
root_dir = os.getcwd()
# mkdir for data
for name in market_list:
    flag = os.path.exists('./'+name)
    if flag:
        print("%s path is existing!\n" % name)
    else:
        os.mkdir('./' + name)

# main
for x in market_list:
    get_all_data(x)






