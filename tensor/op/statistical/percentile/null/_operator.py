class NanPercentile(StatisticalOperator):
    nanmax = jnp.nanmax
    nanmin = jnp.nanmin
    nanmedian = jnp.nanmedian
    nanquantile = jnp.nanquantile
    nanpercentile = jnp.nanpercentile
