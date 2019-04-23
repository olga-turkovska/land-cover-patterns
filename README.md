### Land cover patterns of wind generation infrastructure in Brazil

This repository contains supporting scripts and data for EGU-2019 poster presentation
__*Land cover patterns of wind generation infrastructure in Brazil*__

by *Olga Turkovska*, *Johannes Schmidt*, *Katharina Gruber*, *Felix Nitsch*

Poster presentation is available via Research Gate:
https://www.researchgate.net/publication/332571308_Land_cover_patterns_of_wind_generation_infrastructure_in_Brazil

All the data necessary for running the script are provided except *CAATINGA.tif* due to its large size.

However, this file can be easily downloaded from MapBiomas Collection 3:
http://mapbiomas.org/pages/database/mapbiomas_collection_download

`extract-land-cover.py` extracts the a raster map of land cover for selected wind parks.

`explore-land-cover.py` generates a CSV file with technical characteristics of the wind parks, and description of their land cover.

`aggregate-land-cover.py` aggregates forest-related land cover subclasses to *forest* land cover class, and agriculture-related landcover subclasses to *mosaic of agriculture and pasture* land cover class.

`land-cover-by-year.py` generates a CSV file with land cover overview of the specific year for selected wind parks.

`find-conversions.py` generates a CSV file with parameters necessary for initial land cover conversion analysis.

`figures.py` generates the figures for the poster.

`MapBiomas_dictionaries.py` contains auxiliary dictionaries for working with MapBiomas dataset.
