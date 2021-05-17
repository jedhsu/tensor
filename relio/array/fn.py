from typing import GenericAlias, Union

import jax.numpy as jnp

# Num = Union[int, float]

# def sum_of_squares(x):
# return jnp.sum(


def sum_of_squares(x):
    return jnp.sum(x ** 2)


class Fn:
    __class_getitem__ = classmethod(GenericAlias)

    def __init__(self):
        ...


#     def grad(self) -> Gradient:
#         ...


Fn[int, str]
