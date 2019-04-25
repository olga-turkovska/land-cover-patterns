import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

from mapBiomas_dictionaries import code_color, code_label

sns.set(context='poster', font='Trebuchet MS')

# Figure 1 | Distribution of wind park territories amongst land cover classes in Ceara
dataset_1 = pd.read_csv('../output/ceara_wp_area_2017.csv')
figure_1 = dataset_1.loc[:, '3':'33']
figure_1 = figure_1.apply(lambda x: x * 994.4037219 / 1000000)

labels_1 = []
colors_1 = []

for code in figure_1.columns.values:
    labels_1.append(code_label.get(code))
    colors_1.append(code_color.get(int(code)))

fig_1, ax_1 = plt.subplots()
ax_1.barh(np.arange(len(labels_1)), figure_1.sum(axis=0), color=colors_1)
ax_1.set_xlabel('\n Area, km$^2$')
ax_1.set_yticks(np.arange(len(labels_1)))
ax_1.set_yticklabels(list(labels_1), wrap=True, fontsize='small', verticalalignment='center')

plt.show()

# Figure 2 | Diversity of land cover amongst wind parks in Ceara
dataset_2 = pd.read_csv('../output/ceara_lc_overview.csv')

labels_2 = []
colors_2 = []

codes = list(dataset_2['lc_class_max_cy'].unique())
codes.sort()

for code in codes:
    labels_2.append(code_label.get(str(code)))
    colors_2.append(code_color.get(code))

legend_labels_2 = dict(zip(colors_2, labels_2))
patches_2 = [Patch(color=color, label=label) for color, label in legend_labels_2.items()]

fig_2, ax_2 = plt.subplots()
ax_2 = sns.scatterplot(x='classes_number_cy', y='lc_share_max_cy', hue='lc_class_max_cy',
                       s=500, data=dataset_2, palette=colors_2)
ax_2.set_xlabel('Quantity of land cover classes per wind park', labelpad=10)
ax_2.set_ylabel('Share of the largest land cover class, % ', labelpad=10)
ax_2.legend(handles=patches_2, title='The largest land cover class')
plt.show()

# Figure 3 | Was the highest estimated conversion of each wind park in commissioning year?

dataset_3 = pd.read_csv('../output/ceara_agg_v2_lc_conversion.csv')
figure_3 = dataset_3[dataset_3['share'] > 0]

colors_3 = []
labels_3 = ['forest', 'mosaic of agriculture and pasture', 'beaches and dunes',
            'other non-vegetated area', 'aquaculture', 'water']

codes = list(figure_3['max_class'].unique())
codes.sort()

for code in codes:
    colors_3.append(code_color.get(code))

legend_labels_3 = dict(zip(colors_3, labels_3))
patches_3 = [Patch(color=color, label=label) for color, label in legend_labels_3.items()]

fig_3, ax_3 = plt. subplots()
ax_3 = sns.scatterplot(x=figure_3.loc[:, '2005':'2017'].max(axis=1), y=figure_3['share'],
                       hue=figure_3['max_class'], s=500, palette=colors_3)
ax_3.set_xlabel('The highest land cover conversion, %', labelpad=10)
ax_3.set_ylabel('Land cover conversion in the commissioning year, %', labelpad=10)
ax_3.legend(handles=patches_3, title='Land cover class after conversion')
plt.show()
