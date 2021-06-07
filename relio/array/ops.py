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


class Cast:
    """
    Type promotion and demotion.

    """

    promote_types = jnp.promote_types
    can_cast = jnp.can_cast  # [TODO] clarify


# ----

# [TODO] typing can get much tighter
class Construct:
    zeros = jnp.zeros
    ones = jnp.ones

    empty = jnp.empty
    full = jnp.full

    arange = jnp.arange

    # TODO: IDEALLY want Fn[N, Array[Dtype][N]]
    # arange: Callable[[N],


class ConstructRelative(Construct):
    zeros_like = jnp.zeros_like
    ones_like = jnp.ones_like

    empty_like = jnp.empty_like
    full_like = jnp.full_like


class UnaOp(Enum):
    abs = jnp.abs
    absolute = jnp.absolute


class BitwiseBinOp(Enum):
    bitwise_and = jnp.bitwise_and
    # bitwise_not = jnp.bitwise_not
    bitwise_or = jnp.bitwise_or
    bitwise_xor = jnp.bitwise_xor


# class BinOp(Enum):
#     ...


class ForwardTrig(Trig):
    sin = jnp.sin
    sinh = jnp.sinh

    cos = jnp.cos
    cosh = jnp.cosh

    tan = jnp.tan
    tanh = jnp.tanh


class BackwardTrig(Trig):
    arcsin = jnp.arcsin
    arcsinh = jnp.arcsinh

    arccos = jnp.arccos
    arccosh = jnp.arccosh

    arctan = jnp.arctan
    arctan2 = jnp.arctan2
    arctanh = jnp.arctanh


class Rotate:

    rot90 = jnp.rot90


class Reflect:
    flip = jnp.flip  # flip along axis
    flipud = jnp.flipud  # flips up/down
    fliplr = jnp.fliplr  # flip left/right


class LogCmp(Enum):
    logical_and = jnp.logical_and
    # logical_not = jnp.logical_not
    logical_or = jnp.logical_or
    logical_xor = jnp.logical_xor


class Join:
    append = jnp.append  # Appends values to end of array
    hstack = jnp.hstack
    vstack = jnp.vstack


class Vertical(Join):
    pass


class Horizontal(Join):
    pass


class BoolOp:
    all = jnp.all
    alltrue = jnp.alltrue

    any = jnp.any


class Stat(Enum):
    mean = jnp.mean
    median = jnp.median

    histogram = jnp.histogram
    histogram_bin_edges = jnp.histogram_bin_edges
    histogram2d = jnp.histogram2d
    histogramdd = jnp.histogramdd


class Exp:
    exp = jnp.exp
    exp2 = jnp.exp2  # [TODO] clarify what this is


class Log(Enum):
    log = jnp.log
    log10 = jnp.log10
    log1p = jnp.log1p
    log2 = jnp.log2


class DiscreteOp:
    floor = jnp.floor
    ceil = jnp.ceil


class BitwiseOp:
    lshift = jnp.lshift
    rshift = jnp.rshift


class Translate:
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


# [TODO] think about the typing interfaces!
class ModularOp(BinOp):
    """
    Modular arithmetic operations.

    """

    mod = jnp.mod
    gcd = jnp.gcd
    divmod = jnp.divmod


class ComplexOp:
    real = jnp.real
    imag = jnp.imag
    angle = jnp.angle  # angle of complex argument


class ComparisonOp:
    """
    Element-wise comparison operators.

    """

    equal = jnp.equal
    isclose = jnp.isclose

    greater = jnp.greater
    greater_equal = jnp.greater_equal

    lesser = jnp.less
    lesser_equal = jnp.less_equal

    where = jnp.where  # predicate evaluation

    allclose = jnp.allclose  # element-wise equality within tolerance


class MatrixOp:
    dot = jnp.dot  # dot product
    cross = jnp.cross  # inner product
    outer = jnp.outer  # outer product


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


class Variance:
    # average = jnp.average  # mean
    var = jnp.var  # variance
    cov = jnp.cov  # covariance
    std = jnp.std  # standard deviation


class Percentile:
    max = jnp.max
    min = jnp.min
    median = jnp.median
    quantile = jnp.quantile
    percentile = jnp.percentile


class NanPercentile:
    nanmax = jnp.nanmax
    nanmin = jnp.nanmin
    nanmedian = jnp.nanmedian
    nanquantile = jnp.nanquantile
    nanpercentile = jnp.nanpercentile


class Slice:
    # [TODO] confirm these are all views
    diag = jnp.diag  # diagonal on axis

    tri = jnp.tri  # triangle copy

    tril = jnp.tril  # lower-triangle copy
    triu = jnp.triu  # upper-triangle copy


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
    sort = jnp.sort


class Index:
    argsort = jnp.argsort  # sorted array indices
    argwhere = jnp.argwhere  # non-zero indices, grouped by element


class ModArithmetic(Enum):
    remainder = jnp.remainder


class Optimization(Enum):
    argmax = jnp.argmax
    argmin = jnp.argmin


class BitwiseOp:
    signbit = jnp.signbit


class Window:
    """
    Window functions.

    """

    bartlett = jnp.bartlett
    blackman = jnp.blackman
    hanning = jnp.hanning


class Analytic:
    """
    Polynomial operations.

    """

    # [TODO] clarify
    polyadd = jnp.polyadd
    polysub = jnp.polysub
    polymul = jnp.polymul

    polyder = jnp.polyder
    polyint = jnp.polyint
    polyval = jnp.polyval


class Shape:
    pass


class Transform:
    """
    Functional transforms.

    """

    positive = jnp.positive  # y = +x
    negative = jnp.negative  # y = -x
    sign = jnp.sign
    heaviside = jnp.heaviside  # [TODO] does ths really go here??


# # TODO: organize numpy api
numpy_api = [
    around,
    array,
    array_equal,
    array_equiv,
    array_repr,
    array_split,
    array_str,
    asarray,
    atleast_1d,
    atleast_2d,
    atleast_3d,
    bfloat16,
    bincount,
    bool_,
    broadcast_arrays,
    broadcast_shapes,
    broadcast_to,
    c_,
    cbrt,
    character,
    choose,
    clip,
    column_stack,
    complexfloating,
    compress,
    concatenate,
    conj,
    conjugate,
    convolve,
    copysign,
    corrcoef,
    correlate,
    count_nonzero,
    csingle,
    delete,
    diagflat,
    diag_indices,
    diag_indices_from,
    diff,
    digitize,
    divide,
    dsplit,
    dstack,
    ediff1d,
    einsum,
    einsum_path,
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
    hamming,
    hsplit,
    hypot,
    i0,
    identity,
    iinfo,
    indices,
    inexact,
    in1d,
    inf,
    inner,
    int_,
    integer,
    interp,
    intersect1d,
    invert,
    isclose,
    iscomplex,
    iscomplexobj,
    isfinite,
    isin,
    isinf,
    isnan,
    isneginf,
    isposinf,
    isreal,
    isrealobj,
    isscalar,
    issubdtype,
    issubsctype,
    iterable,
    ix_,
    kaiser,
    kron,
    lcm,
    ldexp,
    left_shift,
    lexsort,
    linspace,
    load,
    logaddexp,
    logaddexp2,
    logspace,
    mask_indices,
    matmul,
    meshgrid,
    mgrid,
    modf,
    moveaxis,
    msort,
    multiply,
    nan,
    nan_to_num,
    nanargmax,
    nanargmin,
    nancumprod,
    nancumsum,
    nanprod,
    nanstd,
    nansum,
    nanvar,
    ndarray,
    ndim,
    newaxis,
    nextafter,
    nonzero,
    not_equal,
    number,
    object_,
    ogrid,
    operator_name,
    packbits,
    pad,
    piecewise,
    ptp,
    r_,
    ravel,
    ravel_multi_index,
    reciprocal,
    repeat,
    reshape,
    result_type,
    right_shift,
    rint,
    roll,
    rollaxis,
    round,
    row_stack,
    save,
    savez,
    searchsorted,
    set_printoptions,
    setdiff1d,
    setxor1d,
    shape,
    sign,
    signedinteger,
    single,
    size,
    sometrue,
    sort_complex,
    split,
    square,
    squeeze,
    stack,
    std,
    swapaxes,
    tensordot,
    tile,
    trace,
    trapz,
    transpose,
    tri,
    tril_indices,
    tril_indices_from,
    trim_zeros,
    triu_indices,
    triu_indices_from,
    true_divide,
    trunc,
    unique,
    union1d,
    unpackbits,
    unravel_index,
    unsignedinteger,
    unwrap,
    vander,
    vdot,
    vsplit,
]
