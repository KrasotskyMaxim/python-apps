import matplotlib.pyplot as plt
import requests
from datetime import datetime


# функция чтения данных из источника
def get_data_plot():
    url = 'https://api.blockchain.info/charts/market-price'
    params = {'timespan':'3years', 'rollingAverage':'8hours', 'format':'json'}
    response = requests.get(url, params=params)
    data = response.json()
    return data 

# обработка полученных json данных
def data_plot():
    data = get_data_plot()
    x_list = []
    y_list = []
    for item in data["values"]:
        x_list.append(datetime.utcfromtimestamp(item['x']))
        y_list.append(item['y'])
    return x_list, y_list

# заголовок графика
plt.title('Bitcoin market value chart', fontsize=14, fontweight='bold', color='blue')
# наименование осей графика
plt.xlabel('Period', fontsize=12, color='black')
plt.ylabel('Market price', fontsize=12, color='black')
# построение графика
plt.plot(*data_plot(), label='Market price')
# легенда графика
plt.legend()
# сетка графика
plt.grid()
# вывод графика
plt.show()