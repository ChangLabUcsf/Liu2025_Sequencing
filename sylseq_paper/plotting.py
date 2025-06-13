# -*- coding: utf-8 -*-
"""
Plotting utils and presets.

:Author: Jessie R. Liu
:Copyright: Copyright (c) 2025, Jessie R. Liu, All rights reserved.
"""

import logging

# Third party libraries
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import ndimage

ucsf_colors = {
    'primary_palette'  : {
        'navy'     : '#052049',
        'turquoise': '#18A3AC',
        'green'    : '#90BD31',
        'blue'     : '#178CCB',
        'orange'   : '#F48024'

    },
    'secondary_palette': {
        'purple' : '#716FB2',
        'magenta': '#EC1848',
        'yellow' : '#FFDD00'
    }
}

all_ucsf_colors = ['#052049', '#18A3AC', '#90BD31', '#178CCB', '#F48024', '#716FB2', '#EC1848', '#FFDD00']
ucsf_sequential_color_palette = ['#178CCB', '#F48024', '#90BD31', '#EC1848', '#716FB2', '#18A3AC', '#FFDD00', '#052049']

area_names = {
    'superiorfrontal'          : 'SFG',
    'caudalmiddlefrontal'      : 'caudal MFG',
    'superiortemporal'         : 'STG',
    'posteriorsuperiortemporal': 'pSTG',
    'posteriormiddletemporal'  : 'pMTG',
    'inferiortemporal'         : 'ITG',
    'ventralprecentral'        : 'ventral PrCG',
    'rostralmiddlefrontal'     : 'rostral MFG',
    'supplementarymotor'       : 'SMA',
    'medialsuperiorfrontal'    : 'medial SFG',
    'dorsalprecentral'         : 'dorsal PrCG',
    'middleprecentral'         : 'middle PrCG',
    'supramarginal'            : 'SMG',
    'parsopercularis'          : 'Pars operc.',
    'middletemporal'           : 'MTG',
    'dorsalpostcentral'        : 'dorsal PoCG',
    'middlepostcentral'        : 'middle PoCG',
    'parstriangularis'         : 'Pars triang.',
    'ventralpostcentral'       : 'ventral PoCG',
    'superiorparietal'         : 'superior Parietal',
    'bankssts'                 : 'STG',
    'nan'                      : 'null',
    'paracentral'              : 'Paracentral',
    'isthmuscingulate'         : 'Cingulate',
    'posteriorcingulate'       : 'Cingulate',
    'rostralanteriorcingulate' : 'Cingulate',
    'caudalanteriorcingulate'  : 'Cingulate',
    'medial'                   : 'Medial',
    'cingulate'                : 'Cingulate',
    'precuneus'                : 'Precuneus'
}

def default_plot_settings(return_colormap=False, colormap='default',
                          linecolor='404040', fontsize=14, font='Helvetica',
                          linewidth=2, ticklength=6):
    """
    Set default plot settings, like color and fontsize for axes. Quiet the
    matplotlib logger warning.
    """

    mpl_logger = logging.getLogger('matplotlib')
    mpl_logger.setLevel(logging.WARNING)

    mpl.rcParams.update({'font.size': fontsize})
    mpl.rcParams['font.sans-serif'] = font
    mpl.rcParams['font.family'] = 'sans-serif'

    mpl.rcParams['axes.spines.top'] = False
    mpl.rcParams['axes.spines.right'] = False

    mpl.rcParams['xtick.major.size'] = ticklength
    mpl.rcParams['xtick.major.width'] = linewidth
    mpl.rcParams['ytick.major.size'] = ticklength
    mpl.rcParams['ytick.major.width'] = linewidth

    mpl.rcParams['xtick.minor.size'] = ticklength // 2
    mpl.rcParams['xtick.minor.width'] = linewidth
    mpl.rcParams['ytick.minor.size'] = ticklength // 2
    mpl.rcParams['ytick.minor.width'] = linewidth

    mpl.rcParams['lines.linewidth'] = linewidth
    mpl.rcParams['axes.linewidth'] = linewidth

    mpl.rcParams['text.color'] = linecolor
    mpl.rcParams['axes.labelcolor'] = linecolor
    mpl.rcParams['axes.edgecolor'] = linecolor
    mpl.rcParams['xtick.color'] = linecolor
    mpl.rcParams['ytick.color'] = linecolor

    if return_colormap:
        if colormap == 'default':
            colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
        elif colormap == 'custom_set2':
            # Custom version of seaborn's Set2 palette
            pal = sns.color_palette('Set2')
            pal = pal.as_hex()
            colors = list(reversed(pal[:3])) + pal[3:]
        else:
            print(f'The colormap {colormap} is not implemented.')
            colors = None

        return colors

fancy_location_colors = {
    'SFG'         : (0.21840821737392985, 0.6647898200401803,
                     0.7553445340026518),
    'SMA'         : (
        0.8233753136307219, 0.5564097629441267, 0.19515040910202758),
    'medial SFG'  : (
        0.8233753136307219, 0.5564097629441267, 0.19515040910202758),
    'middle PrCG' : (
        0.9709475908389634, 0.46403989737619705, 0.23268163300341138),
    'dorsal PoCG' : (
        0.2276041189151808, 0.6492591618617503, 0.8667352328785314),
    'ventral PrCG': (
        0.19381360556293972, 0.7009873870290324, 0.2710533164704233),
    'dorsal PrCG' : (
        0.9609894338512172, 0.3866875852472021, 0.8475770545475213),
    'rostral MFG' : (
        0.9677975592919913, 0.44127456009157356, 0.5358103155058701),
    'middle PoCG' : (
        0.7188721694437208, 0.601448945129206, 0.19432336924941168),
    'ventral PoCG': (
        0.964715581208501, 0.4175934015417711, 0.6999430436310112),
    'Pars operc.' : (
        0.8753266398274079, 0.4280264074507189, 0.9577762021967094),
    'pSTG'        : (
        0.6199256505009382, 0.6340974041174863, 0.19366913066077465),
    'caudal MFG'  : (
        0.690592305012026, 0.5310029892694575, 0.9581797268573365),
    'Pars triang.': (
        0.20260140137245986, 0.6888777365691905, 0.5073931192355193),
    'pMTG'        : (
        0.46464649399867336, 0.6001189477477143, 0.9585131479964976),
    'SMG'         : (
        0.20806612541243952, 0.6808998626985141, 0.6056504754121731),
    'STG'         : (
        0.21283940026780146, 0.6736342952276683, 0.6790583455137678),
    'MTG'         : (
        0.48656894593750394, 0.6663726666050075, 0.19297564161091252),
    'Cingulate'   : (0.9677975592919913, 0.44127456009157356,
                     0.5358103155058701)
}

def smoothed_weighted_histogram(x=None, y=None, weights=None, xlim=None,
                                ylim=None, bins=None, smooth=None,
                                baseline_norm=False):
    """
    Generate a Gaussian smoothed 2D histogram. If baseline norm is set to
    True, then the weights that are 0 determine the rest of the population
    and the resulting density will be normalized by the baseline before
    smoothing.

    Parameters
    ----------
    x
    y
    weights
    xlim
    ylim
    bins
    smooth

    Returns
    -------

    """

    im, xedges, yedges = np.histogram2d(
        x, y, bins=bins, density=False, weights=weights, range=[xlim, ylim]
    )

    if baseline_norm:
        b_im, xedges, yedges = np.histogram2d(
            x, y, bins=bins, density=False, range=[xlim, ylim]
        )
        im /= b_im + 1e-15

    im = ndimage.gaussian_filter(im, sigma=(smooth, smooth), order=0)
    im /= im.max()

    return im, xedges, yedges
