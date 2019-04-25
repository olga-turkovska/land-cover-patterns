### Land cover patterns of wind generation infrastructure in Brazil

This repository contains supporting scripts and data for EGU-2019 poster presentation
__*Land cover patterns of wind generation infrastructure in Brazil*__

by *Olga Turkovska*, *Johannes Schmidt*, *Katharina Gruber*, *Felix Nitsch*

Poster presentation is available via Research Gate:
https://www.researchgate.net/publication/332571308_Land_cover_patterns_of_wind_generation_infrastructure_in_Brazil

Input files necessary for running the script can be easily downloaded via links provided below.

1. Caatinga land cover map for the period from 1985 to 2017 - MapBiomas Collection 3:
http://mapbiomas.org/pages/database/mapbiomas_collection_download

2. Wind parks polygons -Polígono_do_Parque_Eolioelétrico_EOL- ANEEL:
https://sigel.aneel.gov.br/Down/

3. Data set of federal states of Brazil - BRUFE250GC_SIR - IBGE:
https://www.ibge.gov.br/en/geosciences/territorial-organization/territorial-structure/18890-meshes.html?=&t=sobre

Downloaded files need to be placed in 'input-dataset' folder.

`0-extract-land-cover.py` extracts the a raster map of land cover for selected wind parks.

`1-explore-land-cover.py` generates a CSV file with technical characteristics of the wind parks, and description of their land cover.

`2-aggregate-land-cover.py` aggregates forest-related land cover subclasses to *forest* land cover class, and agriculture-related landcover subclasses to *mosaic of agriculture and pasture* land cover class.

`3-land-cover-by-year.py` generates a CSV file with land cover overview of the specific year for selected wind parks.

`4-find-conversions.py` generates a CSV file with parameters necessary for initial land cover conversion analysis.

`5-figures.py` generates the figures for the poster.

`MapBiomas_dictionaries.py` contains auxiliary dictionaries for working with MapBiomas dataset.
