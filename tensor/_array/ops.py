from enum import Enum

import jax.numpy as jnp


class Constant:
    E = jnp.e
    PI = jnp.pi
    INFINITY = jnp.inf

# [TODO] move to types
class AdditionalTypes:
    complex128 = jnp.complex128
    complex64 = jnp.complex64
    complex_ = jnp.complex_

    double = jnp.double
    cdouble = jnp.cdouble

    can_cast = jnp.can_cast  # [TODO] clarify


# ----


class UnaOp(Enum):
    abs = jnp.abs  # [TODO] i think this abbreviation alias
    absolute = jnp.absolute

    FloatAbs = jnp.fabs

    
# class BinOp(Enum):
#     ...


class Multiply(ElementOperator, BinaryOperator, ArrayOperator,):
    """
    Element-wise multiplication.

    """
    func = jnp.multiply
    
class Divide(ElementOperator, BinaryOperator, ArrayOperator,):
    """
    Element-wise division.

    """
    func = jnp.divide

class Stat(Enum):
    mean = jnp.mean
    median = jnp.median


class BitwiseOperator:
    LeftShift = jnp.left_shift
    RightShift = jnp.right_shift


class Wrangling:
    # [TODO] better name
    Pad = jnp.pad  # [TODO] does this really belong here?
    Repeat = jnp.repeat

    TrimZeros = jnp.trim_zeros  # this is also vector op

class BinOp:


    amax = jnp.amax  # maximum along axis
    amin = jnp.amin  # minimum along axis

    power = jnp.power


class Piece:
    """
    Seemingly more complex composing ops.

    """

    block = jnp.block


# [TODO] clarify axis vs elementwise


class AxisOp:
    sum = jnp.sum
    Trace = jnp.trace  # [TODO] clarify  # sum along diagonals

    cumsum = jnp.cumsum

    average = jnp.average  # average along axis
    max = jnp.max  # max along axis
    min = jnp.min

    prod = jnp.prod
    cumprod = jnp.cumprod
    cumproduct = jnp.cumproduct  # [TODO] how different?


class ElementWiseOp:
    add = jnp.add  # adds element-wise
    subtract = jnp.subtract

    # [TODO] clarify this
    fmax = jnp.fmax
    fmin = jnp.fmin



class Functional:
    """
    Functional selection patterns.

    """

    select = jnp.select  # [TODO] clairfy
    take = jnp.take


class FunctionalAxis:
    """
    Functional selection patterns along axis.

    """

    take_along_axis = jnp.take_along_axis


class ElementWisePercentile:
    maximum = jnp.maximum
    minimum = jnp.minimum


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
    IsIn = (jnp.isin,)

    IsNan = jnp.isnan

    IsInfinity = (jnp.isinf,)
    IsPositiveInfinity = jnp.isposinf
    IsNegativeInfinity = jnp.isneginf

    IsReal = jnp.isreal
    IsRealObj = jnp.isrealobj

    IsScalar = jnp.isscalar

    IsSubtype = jnp.issubdtype
    IsSubclass = jnp.issubsctype

class Clone:


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
    Diagonal = jnp.diagonal

    Triangle = jnp.tri

    LowerTriangle = jnp.tril
    UpperTriangle = jnp.triu


class Apply:
    apply_along_axis = jnp.apply_along_axis
    apply_over_axes = jnp.apply_over_axes


class Root:
    sqrt = jnp.sqrt


class Algo:
    # [TODO] better kind for this?
    Sort = jnp.sort
    SortComplex = jnp.sort_complex

    SearchSorted = jnp.searchsorted

    Unique = jnp.unique

    LexSort = jnp.lexsort


class Index:
    ArgSort = jnp.argsort  # sorted array indices
    ArgWhere = jnp.argwhere  # non-zero indices, grouped by element

    Digitize = jnp.digitize  # REturns indices of bins


# [TODO] hmm how different from remainder
class ModArithmetic(Enum):
    remainder = jnp.remainder


class Optimization(Enum):
    argmax = jnp.argmax
    argmin = jnp.argmin


# [TODO} hmm where is this
class BitwiseOp:
    signbit = jnp.signbit


class Shape:
    pass


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


class ShapeProperty:
    Shape = jnp.shape
    NumDimensions = jnp.ndim


class Pythagorean:
    Hypotenuse = jnp.hypot


class Count:
    BinCount = jnp.bincount

    CountNonZero = jnp.count_nonzero
    FlatNonZero = jnp.flatnonzero
    NonZero = jnp.nonzero

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

class Reciprocal(ElementWiseOperator, UnaryOperator, Functional,):
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
