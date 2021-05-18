"""
Wrapper on JAX JIT.
"""

import jax
import jax.numpy as jnp

lst = []


def log2(x):
    lst.append(x)
    ln_x = jnp.log(x)
    ln_2 = jnp.log(2.0)
    return ln_x / ln_2


print(jax.make_jaxpr(log2)(3.0))
