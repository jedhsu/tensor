from enum import Enum

import jax.numpy as jnp


class Constant:
    E = jnp.e
    PI = jnp.pi


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
    abs = jnp.abs
    absolute = jnp.absolute


# class BinOp(Enum):
#     ...


class Stat(Enum):
    mean = jnp.mean
    median = jnp.median


class DiscreteOp:
    floor = jnp.floor
    ceil = jnp.ceil


class BitwiseOperator:
    LeftShift = jnp.left_shift
    RightShift = jnp.right_shift


class Wrangling:
    pad = jnp.pad  # [TODO] does this really belong here?


class BinOp:

    divide = jnp.divide  # true division

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


class FrequencyOp:
    # [TODO] lol improve name
    radians = jnp.radians
    degrees = jnp.degrees
    rad2deg = jnp.rad2deg
    deg2rad = jnp.deg2rad


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


class Slicing:
    # [TODO] confirm these are all views
    diag = jnp.diag  # diagonal on axis

    tri = jnp.tri  # triangle copy

    tril = jnp.tril  # lower-triangle copy
    triu = jnp.triu  # upper-triangle copy


class IndexSlicing:
    DiagonalIndices = jnp.diag_indices

    LowerTriangularIndices = jnp.tril_indices
    UpperTriangularIndices = jnp.triu_indices
    # diag_indices_from,
    # tril_indices_from,
    # triu_indices_from,


class Clone:
    # [TODO] IMPORTANT - check that this is the right cat
    diagonal = jnp.diagonal


class Apply:
    apply_along_axis = jnp.apply_along_axis
    apply_over_axes = jnp.apply_over_axes


class Root:
    sqrt = jnp.sqrt


class Algo:
    # [TODO] better kind for this?
    Sort = jnp.sort
    SortComplex = jnp.sort_complex


class Index:
    argsort = jnp.argsort  # sorted array indices
    argwhere = jnp.argwhere  # non-zero indices, grouped by element


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


class ShapeProperty:
    Shape = jnp.shape
    NumDimensions = jnp.ndim


class Ravel:
    Ravel = jnp.ravel
    RavelMultiIndex = jnp.ravel_multi_index
    UnravelIndex = jnp.unravel_index


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


# # TODO: organize numpy api

numpy_api = [
    around,
    asarray,
    bfloat16,
    bincount,
    bool_,
    cbrt,
    character,
    choose,
    clip,
    complexfloating,
    compress,
    concatenate,
    convolve,
    copysign,
    count_nonzero,
    csingle,
    delete,
    diagflat,
    diff,
    digitize,
    divide,
    ediff1d,
    euler_gamma,
    expand_dims,
    expm1,
    extract,
    eye,
    fabs,
    finfo,
    fix,
    flatnonzero,
    flexible,
    float_,
    float_power,
    floating,
    floor_divide,
    fmod,
    frexp,
    geomspace,
    gradient,
    hypot,
    i0,
    identity,
    iinfo,
    indices,
    ix_,
    inexact,
    in1d,
    inf,
    int_,
    integer,
    rint,
    interp,
    intersect1d,
    invert,
    iterable,
    ldexp,
    lexsort,
    linspace,
    load,
    logaddexp,
    logaddexp2,
    logspace,
    mask_indices,
    matmul,
    moveaxis,
    msort,
    multiply,
    ndarray,
    newaxis,
    nextafter,
    nonzero,
    not_equal,
    number,
    object_,
    operator_name,
    packbits,
    piecewise,
    ptp,
    r_,
    c_,
    reciprocal,
    repeat,
    result_type,
    roll,
    rollaxis,
    round,
    row_stack,
    column_stack,
    searchsorted,
    set_printoptions,
    setdiff1d,
    setxor1d,
    sign,
    signedinteger,
    single,
    size,
    sometrue,
    square,
    squeeze,
    swapaxes,
    vdot,
    tensordot,
    tile,
    trace,
    trapz,
    transpose,
    trim_zeros,
    true_divide,
    trunc,
    unique,
    union1d,
    unpackbits,
    unsignedinteger,
    unwrap,
    vander,
]
