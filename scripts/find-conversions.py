import os
import pandas as pd
import numpy as np
import rasterio

from mapBiomas_dictionaries import year_band


def reclassified_pixels(year):
    band = year_band.get(year)
    open_band = wp_raster.read(band)
    pixels = np.count_nonzero(open_band)
    converted = open_band * (open_band != wp_raster.read(band - 1))
    data.append(round(np.count_nonzero(converted) / pixels * 100, 2))


parks = pd.read_csv('./data/ceara_wind_parks.csv')

column_names = ['wp_id', 'comm_year', 'share', 'no_classes', 'max_class',
                '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
dataset = pd.DataFrame(columns=column_names)

years = column_names[5:]
years = list(map(int, years))

for dirs, subdirs, files in os.walk('./data/ceara_agg_v2/'):
    for file in files:
        wp_raster = rasterio.open('./data/ceara_agg_v2/' + file)
        data = []
        file_name = file.replace('agg_v2_id_', '')
        wp_id = int(file_name.replace('.tif', ''))
        data.append(wp_id)
        comm_year = parks['comm_year'].loc[parks['wp_id'] == wp_id]
        data.append(comm_year.iloc[0])
        comm_band = year_band.get(comm_year.iloc[0])

        if comm_band is None:
            data.append(None)
            data.append(None)
            data.append(None)
        else:
            comm_pixels = np.count_nonzero(wp_raster.read(comm_band))
            comm_converted = wp_raster.read(comm_band) * (wp_raster.read(comm_band) != wp_raster.read(comm_band - 1))
            data.append(round(np.count_nonzero(comm_converted) / comm_pixels * 100, 2))

            unique, counts = np.unique(comm_converted, return_counts=True)
            data.append(len(unique) - 1)
            land_cover = dict(zip(counts, unique))

            if land_cover.get(max(land_cover)) == 0:
                del land_cover[max(land_cover)]

            max_class = land_cover.get(max(land_cover))
            data.append(max_class)
            # """

        list(map(reclassified_pixels, years))

        add = dict(zip(column_names, data))
        dataset = dataset.append(add, ignore_index=True)


dataset.to_csv('./data/ceara_agg_v2_lc_conversion.csv')
