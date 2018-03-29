#!/usr/bin/env python3

import os, json, csv, time
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True, style="darkgrid")

directory = dir_path = os.path.dirname(os.path.realpath(__file__))


def check_and_create_csv():
    my_file = Path(directory + '/cleansed_json.csv')
    if my_file.is_file():
        print('CSV already exists - moving data to pandas dataframe')
    else:
        with open('cleansed_json.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(['description', 'flight_id', 'price', 'city', 'unix'])
            for filename in os.listdir(directory):
                tmp = []
                if filename.endswith(".txt"):
                    try:
                        data = json.load(open(filename))
                        for key, value in data.items():
                                payload = [value['description'], value['flight_id'], value['price'][1:], value['city'], value['unix']]
                                writer.writerow(payload)
                    except Exception:
                        print(filename + ' data is corrupt')
                        # removing json files where scraping returned "Failure" messages
                        os.remove(filename)


def csv_to_dataframe_to_seaborn():
    # create DataFrame
    df = pd.read_csv('cleansed_json.csv', encoding='utf-8')
    df = df.sort_values(['flight_id', 'unix'])
    df.price = pd.to_numeric(df.price, errors='coerce')
    df.unix = pd.to_numeric(df.unix, errors='coerce')

    df['wday'] = df['unix'].apply(time.ctime).str[:3]

    # list comp for each flight_id
    # df1, df2, df3, df4, df5, df6, df7, df8 = [df.loc[df['flight_id'] == 'f{}'.format(x)] for x in range(1, 9)]
    dflist = [df.loc[df['flight_id'] == 'f{}'.format(x)] for x in range(1, 9)]
    for _ in dflist:
        sns.lmplot(x="unix", y="price", ci=None, hue="city", data=_)
        plt.savefig('graphs/{}.png'.format(_.flight_id.iloc[0]), bbox_inches='tight')

if __name__ == '__main__':
    check_and_create_csv()
    csv_to_dataframe_to_seaborn()

