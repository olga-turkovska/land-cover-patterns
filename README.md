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

    2.1 Go to the webpage: https://sigel.aneel.gov.br/Down/
    
    2.2 Click on second button on the left
    
    2.3 From *Layers to Clip* select *Polígono do Parque Eolioelétrico EOL*
    
    2.4 Press *Execute* button at the end of the list. This will generate a link for dowloading the data
    
    2.5 Use the generated link to download your data
    
    2.6. Extract downloded files to *data-input* folder

3. Data set of federal states of Brazil - BRUFE250GC_SIR - IBGE:
ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2017/Brasil/BR/br_unidades_da_federacao.zip

Downloaded files need to be placed in 'input-dataset' folder.

`0-extract-land-cover.py` extracts the a raster map of land cover for selected wind parks.

`1-explore-land-cover.py` generates a CSV file with technical characteristics of the wind parks, and description of their land cover.

`2-aggregate-land-cover.py` aggregates forest-related land cover subclasses to *forest* land cover class, and agriculture-related landcover subclasses to *mosaic of agriculture and pasture* land cover class.

`3-land-cover-by-year.py` generates a CSV file with land cover overview of the specific year for selected wind parks.

`4-find-conversions.py` generates a CSV file with parameters necessary for initial land cover conversion analysis.

`5-figures.py` generates the figures for the poster.

`MapBiomas_dictionaries.py` contains auxiliary dictionaries for working with MapBiomas dataset.
