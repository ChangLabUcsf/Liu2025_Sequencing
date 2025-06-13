# -*- coding: utf-8 -*-
"""
Statistics functions.

:Author: Jessie R. Liu
:Copyright: Copyright (c) 2025, Jessie R. Liu, All rights reserved.
"""

# Standard libraries
import os
import random

# Third party libraries
import numpy as np
import pandas as pd
from mne.stats import permutation_cluster_test
from scipy import stats
from scipy.ndimage.filters import gaussian_filter1d
from statsmodels.stats.multitest import fdrcorrection

def fdr_omitnans(pvals, **kwargs):
    """
    Computes FDR correction while ignoring NaN entries.

    Parameters
    ----------
    pvals : 1d array of floats
        The p-values to correct.
    kwargs : dictionary
        The keyword arguments to pass to the statsmodels function.

    Returns
    -------
    corrected_pvals : 1d array of floats
        The corrected p-values with the same shape as the input pvals
        variable. Any NaN p-values remain NaN's in this new array.
    """

    corrected_pvals = np.full(pvals.shape, np.nan)
    idx = np.where(~np.isnan(pvals))[0]

    _, new_pvals = fdrcorrection(pvals[idx], **kwargs)
    corrected_pvals[idx] = new_pvals
    return corrected_pvals


def p_value_calc(data, test_statistic=None, axis=0):
    """
    Calculate the p-value for a specific test statistic value from
    the distribution of re-sampled test statistics.

    Parameters
    ----------
    data : nd-array
        The resampled test statistics.
    test_statistic : int or float
        The test statistic to compare against.
    axis : int
        The axis along which to compute (the axis holding the bootstrap or
        permutation iterations).

    Returns
    -------
    p_value : nd-array
        Array of p-values, same shape as incoming data except reducing the
        given axis.
    """
    # Shift the distribution to be centered around 0.
    dmean = data.mean(axis)
    data = data - dmean
    test_statistic = test_statistic - dmean

    # Calculate the number of test statistics resulting from resampling)
    # that are more extreme than our test-statistic we want to calculate the
    # p-value for.
    p_value = np.sum(np.abs(data) > np.abs(test_statistic), axis=axis) / \
              data.shape[axis]

    return p_value

def correlation_permutation(group1, group2, n_permute=1000,
                            corr=stats.pearsonr, return_dist=False,
                            random_seed=None):
    """
    Perform a permutation test for a correlation function. Performs the
    permutation by permuting only 1 group, to assess the null
    hypothesis that the group structure has a significant correlation.

    Parameters
    ----------
    group1 : 1d array
        The first group of observations.
    group2 : 1d array
        The second group of observations, with equal shape to group1.
    n_permute : int
        The number of permutations to
    corr : function
        A correlation function that accepts 2 args (each a group of
        observations to calculate the correlation between) and returns a
        tuple with the first element being the correlation value and the
        second element being a p-value (which is ignored in favor of the
        permutation calculated p-value). Need not be a scipy.stats function.
    return_dist : bool, default False
        Whether to return the distribution of computed correlation values
        for each permutation.
    random_seed : int
        Random seed for reproducibility.

    Returns
    -------
    test_correlation : float
        The correlation between the un-permuted group1 and group2.
    p_value : float
        The computed p-value associated with the permutation distribution
        and test_correlation.
    (optionally) corr_dist : 1d array
        The distribution of correlation values from each permutation.
    """
    # Set random number generator.
    random.seed(random_seed)

    # Compute the test statistic on the data.
    test_correlation, _ = corr(group1, group2)

    # Initialize array.
    corr_dist = np.zeros(n_permute)

    # Calculate the correlation distribution for n_permute permutations.
    for p in range(n_permute):
        # Permute 1 group.
        perm_idx = random.sample(range(len(group1)), k=len(group1))
        permuted_group1 = np.copy(group1[np.array(perm_idx)])

        # Calculate and append the correlation value.
        corr_value, _ = corr(permuted_group1, group2)
        corr_dist[p] = corr_value

    # Calculate the p-value.
    p_value = p_value_calc(corr_dist, test_statistic=test_correlation)

    if return_dist:
        return test_correlation, p_value, corr_dist
    else:
        return test_correlation, p_value
