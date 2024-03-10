#Usando a datatime#

import datetime as dt


#Isso aqui é para formatar as datas#
formatted_date = dt.datetime.strptime(transaction_date[:-6], '%d/%m/%Y:%H:%M:%S')
print(formatted_date)


# Colocando em data de terras tupiniquins #
import pytz
formatted_date_tz = formatted_date.replace(tzinfo=pytz.UTC)
my_timezone = pytz.timezone('America/Sao_Paulo')
local_date = formatted_date_tz.astimezone(my_timezone)
print(local_date.strftime('%d/%m/%Y %H:%M:%S %Z'))



#Arrendodando para horas#
rounded_date = local_date.replace(minute=0, second=0, microsecond=0)
print(rounded_date)



#Compara as datas#
hoje = dt.datetime.now()
print(hoje)


semana_passada = dt.datetime.now() - dt.timedelta(days=7)
print(semana_passada)


#usando pandas#
import pandas as pd
import warnings
warnings.simplefilter(action='ignore')


df = pd.read_csv('transactions.csv')
df.columns = ['transaction_date', 'transaction_operation']


df.head()
df.dtypes


#coloca no formato que seres humanos entendem #
df['transaction_date'] = pd.to_datetime(df['transaction_date'], 
                                        format='%d/%m/%Y:%H:%M:%S +0000',
                                        utc=True)



df.dtypes
df.set_index('transaction_date', inplace=True)

#Formata para data de terras brazucas heuheuheu#
df.index = df.index.tz_convert('America/Sao_Paulo')

df.head()

#Arredonda a data lá#
df.index = df.index.floor('1H')
df.head()


#Compara a data#
df['inicio_semana'] = df.index.to_period('W').start_time
df.head()

df['inicio_prox_semana'] = df['inicio_semana'] + pd.DateOffset(weeks=1)
df.head()


#Teste#

pd.date_range(dt.datetime.now(), periods=10, freq='D')


#isso daqui é pra colocar (input) a data e hora no teste ficou assim
# (['2020-05-24 02:49:03.762162', '2020-05-31 02:49:03.762162]')
# 
# 
# # 
pd.date_range(dt.datetime.now(), dt.datetime(2020, 6, 30), freq='W')