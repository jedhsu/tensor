# from typing import Generic, GenericAlias, TypeVar, Union, Callable

# import jax.numpy as jnp

# # Num = Union[int, float]

# # def sum_of_squares(x):
# # return jnp.sum(


# def sum_of_squares(x):
#     return jnp.sum(x ** 2)


# X = TypeVar("X")
# Y = TypeVar("Y")


# class Fn(Callable[[X], Y]):
#     __class_getitem__ = classmethod(GenericAlias)

#     def __init__(self):
#         ...

# #     def __getitem__(self, params):
# #         args, result = params
# #         return self.__getitem_inner__(params)

# #     def __getitem_inner__(self, params):
# #     args, result = params
# #     resul


#     @abstractmethod
#     def __call__(self):
#         ...


# # class Pr[A,S][T,D]

# #     def grad(self) -> Gradient:
# #         ...


# Fn[int, str]
