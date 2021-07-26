from enum import Enum

import jax.numpy as jnp


class Constant:
    E = jnp.e
    PI = jnp.pi
    INFINITY = jnp.inf


class ToCategorize:
    can_cast = jnp.can_cast  # theses are casting rules
    take_along_axis = jnp.take_along_axis


# ----


# class BinOp(Enum):
#     ...


class Piece:
    """
    Seemingly more complex composing ops.

    """

    block = jnp.block


# [TODO] clarify axis vs elementwise


class ElementWiseOp:
    add = jnp.add  # adds element-wise
    subtract = jnp.subtract

    # [TODO] clarify this


class NanStat:
    """
    NaN-inclusive axis summary operations.

    """

    nanmean = jnp.nanmean
    nanmax = jnp.nanmax
    nanmin = jnp.nanmin


class ValidationOperator:

    IsClose = jnp.isclose
    IsComplex = (jnp.iscomplex,)
    IsComplexObj = jnp.iscomplexobj
    IsFinite = (jnp.isfinite,)
    IsNan = jnp.isnan
    IsIn = (jnp.isin,)

    IsInfinity = (jnp.isinf,)
    IsPositiveInfinity = jnp.isposinf
    IsNegativeInfinity = jnp.isneginf

    IsReal = jnp.isreal
    IsRealObj = jnp.isrealobj

    IsScalar = jnp.isscalar

    IsSubtype = jnp.issubdtype
    IsSubclass = jnp.issubsctype


class Slicing:
    # [TODO] confirm these are all views
    Diagonal = jnp.diag  # diagonal on axis

    Compress = jnp.compress

    Square = jnp.square  # [TODO] not sure if belongs


class IndexSlicing:
    DiagonalIndices = jnp.diag_indices

    LowerTriangularIndices = jnp.tril_indices
    UpperTriangularIndices = jnp.triu_indices
    # diag_indices_from,
    # tril_indices_from,
    # triu_indices_from,


class Clone:
    # [TODO] IMPORTANT - check that this is the right cat

    Triangle = jnp.tri


class Apply:
    apply_along_axis = jnp.apply_along_axis
    apply_over_axes = jnp.apply_over_axes


class Algo:
    # [TODO] better kind for this?
    Sort = jnp.sort
    SortComplex = jnp.sort_complex

    SearchSorted = jnp.searchsorted

    Unique = jnp.unique

    LexSort = jnp.lexsort


# [TODO] hmm how different from remainder
class ModArithmetic(Enum):
    remainder = jnp.remainder


# [TODO} hmm where is this


class Array:
    Array = jnp.array
    ArrayEqual = jnp.array_equal
    ArrayEquiv = jnp.array_equiv
    ArrayRepr = jnp.array_repr
    ArraySplit = jnp.array_split
    ArrayStr = jnp.array_str


class EinsteinSummation:

    EinsteinSummation = jnp.einsum
    EinsteinSummationPath = jnp.einsum_path


class Grid:

    MeshGrid = jnp.meshgrid
    MGrid = jnp.mgrid
    OGrid = jnp.ogrid


class Save:

    Save = jnp.save
    Savez = jnp.savez


class Load:

    Load = jnp.load


class Pythagorean:
    Hypotenuse = jnp.hypot


class Nan:

    pass
    # nan,
    # nan_to_num,

    # nanargmin,
    # nanargmax,

    # nansum,
    # nanprod,

    # nancumsum,
    # nancumprod,

    # nanvar,
    # nanstd,


class Numerical:
    # [TODO] better name
    Interpolate = jnp.interp


class Float:
    Float_ = jnp.float_
    FloatPower = jnp.float_power
    FloatInfo = jnp.finfo

    Floating = jnp.floating


# # TODO: organize numpy api


class Set:
    SetPrintOptions = jnp.set_printoptions


class Integer:
    IntegerInfo = jnp.iinfo

    Int_ = jnp.int_
    RInt = jnp.rint

    Integer = jnp.integer
    SignedInteger = jnp.signedinteger
    UnsignedInteger = jnp.unsignedinteger


class Differential:
    # [TODO] check name is appropriate
    Gradient = jnp.gradient


class Types:
    # [TODO] move to appropriate
    Character = jnp.character

    Inexact = jnp.inexact

    Number = jnp.number

    BooleanByte = jnp.bool_

    ComplexSingle = jnp.csingle

    ComplexFloating = jnp.complexfloating

    Variadic = jnp.flexible  # [TODO] clarify

    FloatC = jnp.single  # single-precision C float  # [TODO] clarify


class Iteration:
    IsIterable = jnp.iterable  # [TODO] clarify


class Reciprocal(
    ElementWiseOperator,
    UnaryOperator,
    Functional,
):
    func = jnp.reciprocal


class CopySign(BinaryOperator):
    func = jnp.copysign


numpy_api = [
    asarray,
    bfloat16,
    choose,
    delete,
    diagflat,
    diff,
    expand_dims,
    indices,
    ix_,
    mask_indices,
    nextafter,
    object_,
    operator_name,
    piecewise,
    r_,
    c_,
    result_type,
    trapz,
    floor_divide,
    true_divide,
    trunc,
    unwrap,
    vander,
]
