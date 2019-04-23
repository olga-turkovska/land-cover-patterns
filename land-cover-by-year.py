import os
import pandas as pd
import numpy as np
import rasterio


def extract_data(land_class):
    data.append(np.count_nonzero(wp_raster.read(comm_band) * (wp_raster.read(comm_band) == land_class)))


parks = pd.read_csv('./data/ceara_wind_parks.csv')

column_names = ['wp_id', 'comm_year', 'area', 'pixels',
           '3', '4', '5', '12', '15', '19', '21', '23', '24', '25', '31', '32', '33']

dataset = pd.DataFrame(columns=column_names)

land_classes = [3, 4, 5, 12, 15, 19, 21, 23, 24, 25, 31, 32, 33]

for dirs, subdirs, files in os.walk('./data/ceara/'):
    for file in files:
        wp_raster = rasterio.open('./data/ceara/' + file)
        data = []

        file_name = file.replace('id_', '')
        wp_id = int(file_name.replace('.tif', ''))
        data.append(wp_id)

        comm_year = parks['comm_year'].loc[parks['wp_id'] == wp_id]
        data.append(comm_year.iloc[0])

        area = parks['AREA_M2'].loc[parks['wp_id'] == wp_id]
        data.append(area.iloc[0])

        # comm_band = year_band.get(comm_year.iloc[0])
        comm_band = 33
        if comm_band is None:
            data.append([None] * 28)
        else:
            data.append(np.count_nonzero(wp_raster.read(comm_band)))
            result = list(map(extract_data, land_classes))

        add = dict(zip(column_names, data))
        dataset = dataset.append(add, ignore_index=True)

dataset.to_csv('./data/ceara_wp_area_2017.csv')
