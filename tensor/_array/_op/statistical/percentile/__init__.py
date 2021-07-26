import jax.numpy as jnp

from .base import StatisticalOperator


class PercentileOperator(StatisticalOperator):
    max = jnp.max
    min = jnp.min
    median = jnp.median
    quantile = jnp.quantile
    percentile = jnp.percentile


class NanPercentile(StatisticalOperator):
    nanmax = jnp.nanmax
    nanmin = jnp.nanmin
    nanmedian = jnp.nanmedian
    nanquantile = jnp.nanquantile
    nanpercentile = jnp.nanpercentile


class Histogram(StatisticalOperator):
    histogram = jnp.histogram
    histogram_bin_edges = jnp.histogram_bin_edges
    histogram2d = jnp.histogram2d
    histogramdd = jnp.histogramdd
