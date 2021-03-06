# import jax.numpy as jnp

# from ..abstract import *
# from ..dtype import *
# from ..sized import *
# from ..typed import *


# class TestAbstractArray:
#     def test_init(self):
#         arr = AbstractArray(i32, (1, 2))

#         assert arr.dtype == i32
#         assert arr.dim == (1, 2)

#         assert isinstance(arr, AbstractArray)
#         assert isinstance(arr, AbstractSizedArray)
#         assert isinstance(arr, AbstractTypedArray)

#     def test_mro(self):
#         inheritance_order = tuple(
#             m for m in AbstractArray.__mro__ if not (m.__name__.endswith("_"))
#         )

#         assert inheritance_order == (
#             AbstractArray,
#             AbstractTypedArray,
#             AbstractSizedArray,
#             object,
#         ), inheritance_order

#     def test_repr(self):
#         arr = AbstractArray(i32, (1, 2))
#         assert repr(arr) == "AbstractArray[i32][1, 2]"


# class Test_From_:
#     def test_from_abstract_typed(self):
#         arr = AbstractTypedArray(i32)
#         assert AbstractArray.from_abstract_typed(arr, (5, 5)) == AbstractArray(
#             i32, (5, 5)
#         )


# class Test_Hooks:
#     def test_typed_build_hook(self):
#         arr = AbstractTypedArray(i32)

#         assert arr[5, 5] == AbstractArray(i32, (5, 5))
