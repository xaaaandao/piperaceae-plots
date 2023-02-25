import matplotlib.pyplot as plt
import numpy as np


def coords_complement(is_region):
    if not is_region:
        return (0, 0.4)
    return (0, 0.9)


def plot_brazil(column, key, series, title, fontsize=6, is_region=False):
    fig, ax = plt.subplots(figsize=(10, 10), dpi=300)

    series.plot(column=column, cmap='Reds', legend=True, ax=ax,
                legend_kwds={'shrink': 0.3, 'orientation': 'horizontal'})
    series.apply(lambda x: ax.annotate(text=x[key] + '\n' + str(np.round(x[column], 2)),
                                       xy=np.subtract(x.geometry.centroid.coords[0], coords_complement(is_region)),
                                       ha='center', fontsize=fontsize), axis=1)

    ax.set_title(title, fontsize=18)
    ax.axis('off')
    fig.savefig(column + '.png')
