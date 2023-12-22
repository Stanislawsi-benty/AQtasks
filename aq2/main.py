import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def dataframe():
    data = {
        'Dtime': pd.date_range("2023-10-01", periods=200, freq="S"),
        'Degrees1': [random.randint(0, 100) for _ in range(200)],
        'Degrees2': [random.randint(0, 100) for _ in range(200)]
    }

    df = pd.DataFrame(data)
    return df


def chart(df, sensor_1, sensor_2, x_ax, y_ax, header):
    global file_name
    df.to_csv(f"{file_name}.csv", index=False)

    df['Time'] = df['Dtime'].dt.strftime('%M:%S')

    plt.figure(figsize=(20, 10))
    plt.plot(df['Time'], df['Degrees1'], linestyle='-', color='b', label=sensor_1)
    plt.plot(df['Time'], df['Degrees2'], linestyle='--', color='r', label=sensor_2)
    plt.title(header)
    plt.xlabel(x_ax)
    plt.ylabel(y_ax)
    plt.legend(loc='upper right')

    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(base=10))
    ax.yaxis.set_major_locator(MultipleLocator(base=10))
    plt.grid(linewidth=1, which="major")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('saved_chart.png')


if __name__ == '__main__':
    file_name = str(input("Введите название файла(без формата): "))
    sensor_one = str(input("Введите название первого датчика: "))
    sensor_two = str(input("Введите название второго датчика: "))
    title = str(input("Введите название графика: "))
    x_axis = str(input("Введите название оси y: "))
    y_axis = str(input("Введите название оси x: "))

    result = dataframe()
    chart(result, sensor_one, sensor_two, x_axis, y_axis, title)
