class Wrangling:
    # [TODO] better name
    Pad = jnp.pad  # [TODO] does this really belong here?
    Repeat = jnp.repeat

    select = jnp.select  # [TODO] clairfy
    take = jnp.take
    TrimZeros = jnp.trim_zeros  # this is also vector op
