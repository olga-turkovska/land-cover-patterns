import os
import math
import pandas as pd
import numpy as np
import rasterio
from mapBiomas_dictionaries import year_band


def find_max(land_cover):
    if land_cover.get(max(land_cover)) == 0:
        del land_cover[max(land_cover)]

    max_class = land_cover.get(max(land_cover))
    max_number = max(land_cover)
    return max_class, max_number, land_cover


dataset = pd.read_csv('./data/wp_landcover_ceara.csv')
parks = pd.read_csv('./data/ceara_wind_parks.csv')

for dirs, subdirs, files in os.walk('./data/ceara/'):
    for file in files:
        wp_raster = rasterio.open('./data/ceara/' + file)

        file_name = file.replace('id_', '')
        wp_id = int(file_name.replace('.tif', ''))

        park = parks[parks['wp_id'] == wp_id]

        wp_land_cover_attrs = []

        to_append = parks['wp_id'].loc[parks['wp_id'] == wp_id]
        wp_land_cover_attrs.append(to_append.iloc[0])

        wp_land_cover_attrs.append('CR')

        to_append = parks['NOME_EOL'].loc[parks['wp_id'] == wp_id]
        wp_land_cover_attrs.append(to_append.iloc[0])

        to_append = parks['geometry'].loc[parks['wp_id'] == wp_id]
        wp_land_cover_attrs.append(to_append.iloc[0])

        to_append = parks['comm_year'].loc[parks['wp_id'] == wp_id]

        if to_append.iloc[0] >= 2018 or math.isnan(float(to_append.iloc[0])) is True:
            continue

        wp_land_cover_attrs.append(to_append.iloc[0])
        band = year_band.get(to_append.iloc[0])
        del to_append

        # Main land cover: class & share for commissioning year
        classes, pixels = np.unique(wp_raster.read(band), return_counts=True)

        d = dict(zip(pixels, classes))
        lc_class_max_cy, lc_number_max_cy, upd_d = find_max(d)
        lc_share_max_cy = round(lc_number_max_cy / np.count_nonzero(wp_raster.read(band)) * 100, 2)
        lc_classes_number = np.count_nonzero(classes)
        wp_land_cover_attrs.append(lc_class_max_cy)
        wp_land_cover_attrs.append(lc_share_max_cy)
        wp_land_cover_attrs.append(lc_classes_number)

        # Extract years for assessing land cover conversion
        year_from = np.where(wp_raster.read(band - 1) == 0, 100, wp_raster.read(band - 1))
        year_to = np.where(wp_raster.read(band) == 0, 100, wp_raster.read(band))

        change_from = year_from * (year_from != year_to)
        change_to = year_to * (year_from != year_to)

        # ----------------------------------------------------------------------------

        # 1st max land cover change: class & share
        classes, pixels = np.unique(change_from, return_counts=True)
        d = dict(zip(pixels, classes))

        lc_class_from_max, lc_number_from_max, upd_d = find_max(d)
        lc_share_from_max = round(lc_number_from_max / np.count_nonzero(change_from) * 100, 2)
        wp_land_cover_attrs.append(lc_class_from_max)
        wp_land_cover_attrs.append(lc_share_from_max)
        del upd_d[max(upd_d)]

        # 2nd max land cover change: class & share
        if len(upd_d) == 0:
            lc_class_from_max2 = 0
            lc_share_from_max2 = 0
        else:
            lc_class_from_max2, lc_number_from_max2, upd_d = find_max(upd_d)
            lc_share_from_max2 = round(lc_number_from_max2 / np.count_nonzero(change_from) * 100, 2)
            del upd_d[max(upd_d)]

        wp_land_cover_attrs.append(lc_class_from_max2)
        wp_land_cover_attrs.append(lc_share_from_max2)

        # 3rd max land cover change: class & share
        if len(upd_d) == 0:
            lc_class_from_max3 = 0
            lc_share_from_max3 = 0
        else:
            lc_class_from_max3, lc_number_from_max3, upd_d = find_max(upd_d)
            lc_share_from_max3 = round(lc_number_from_max3 / np.count_nonzero(change_from) * 100, 2)

        wp_land_cover_attrs.append(lc_class_from_max3)
        wp_land_cover_attrs.append(lc_share_from_max3)
        del upd_d

        # ----------------------------------------------------------------------------

        # 1st max new land cover: class & share
        classes, pixels = np.unique(change_to, return_counts=True)
        d = dict(zip(pixels, classes))

        lc_class_to_max, lc_number_to_max, upd_d = find_max(d)
        lc_share_to_max = round(lc_number_to_max / np.count_nonzero(change_to) * 100, 2)
        wp_land_cover_attrs.append(lc_class_to_max)
        wp_land_cover_attrs.append(lc_share_to_max)
        del upd_d[max(upd_d)]

        # 2nd max new land cover: class & share
        if len(upd_d) == 0:
            lc_class_to_max2 = 0
            lc_share_to_max2 = 0
        else:
            lc_class_to_max2, lc_number_to_max2, upd_d = find_max(upd_d)
            lc_share_to_max2 = round(lc_number_to_max2 / np.count_nonzero(change_to) * 100, 2)
            del upd_d[max(upd_d)]

        wp_land_cover_attrs.append(lc_class_to_max2)
        wp_land_cover_attrs.append(lc_share_to_max2)

        # 3rd max new land cover: class & share
        if len(upd_d) == 0:
            lc_class_to_max3 = 0
            lc_share_to_max3 = 0
        else:
            lc_class_to_max3, lc_number_to_max3, upd_d = find_max(upd_d)
            lc_share_to_max3 = round(lc_number_to_max3 / np.count_nonzero(change_to) * 100, 2)

        wp_land_cover_attrs.append(lc_class_to_max3)
        wp_land_cover_attrs.append(lc_share_to_max3)
        del upd_d

        add = dict(zip(dataset.columns.values, wp_land_cover_attrs))
        dataset = dataset.append(add, ignore_index=True)

dataset.to_csv('./data/ceara_lc_overview.csv')

