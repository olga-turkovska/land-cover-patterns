import rasterio
import geopandas
from geopandas.tools import overlay
import rasterio.mask


def mask_land_cover(polygon):
    out_meta = biome.meta

    out_raster, out_transform = rasterio.mask.mask(biome, [polygon['geometry']], crop=True)
    out_meta.update({"driver": "GTiff",
                     "height": out_raster.shape[1],
                     "width": out_raster.shape[2],
                     "transform": out_transform})

    park_land_cover = rasterio.open(polygon['raster_path'], 'w', **out_meta)
    park_land_cover.write(out_raster)


biome = rasterio.open('../input-data/CAATINGA.tif')
wind_parks = geopandas.read_file('../input-data/Polígono_do_Parque_Eolioelétrico_EOL.shp')
brazil = geopandas.read_file('../input-data/BRUFE250GC_SIR.shp')

state = brazil[brazil['NM_ESTADO'] == "CEARÃ\x81"]

state_wind_parks = overlay(wind_parks, state, how='intersection')
state_wind_parks['comm_year'] = state_wind_parks['INIC_OPER'].str[0:4]

state_wind_parks = state_wind_parks.to_crs({'init': 'epsg:4326'})
ids = list(range(1, 79))
state_wind_parks['wp_id'] = ids

state_wind_parks.to_csv('../output/ceara_wind_parks.csv')

state_wind_parks['raster_path'] = state_wind_parks['wp_id'].apply(lambda x: "../output/ceara/" + "id_" + str(x) + ".tif")

state_wind_parks.apply(mask_land_cover, axis=1)
