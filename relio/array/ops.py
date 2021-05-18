from enum import Enum

import jax.numpy as jnp


class Construct(Enum):
    zeros = jnp.zeros
    ones = jnp.ones
    empty = jnp.empty


class UnaOp(Enum):
    abs = jnp.abs
    absolute = jnp.absolute


class BitwiseBinOp(Enum):
    bitwise_and = jnp.bitwise_and
    # bitwise_not = jnp.bitwise_not
    bitwise_or = jnp.bitwise_or
    bitwise_xor = jnp.bitwise_xor


class BinOp(Enum):
    ...


class Trig(Enum):
    cos = jnp.cos
    cosh = jnp.cosh

    arcsin = jnp.arcsin
    arcsinh = jnp.arcsinh
    arccos = jnp.arccos
    arccosh = jnp.arccosh
    arctan = jnp.arctan
    arctan2 = jnp.arctan2
    arctanh = jnp.arctanh


class LogCmp(Enum):
    logical_and = jnp.logical_and
    # logical_not = jnp.logical_not
    logical_or = jnp.logical_or
    logical_xor = jnp.logical_xor


class Join(Enum):
    ...


class Stat(Enum):
    mean = jnp.mean
    median = jnp.median

    histogram = jnp.histogram
    histogram_bin_edges = jnp.histogram_bin_edges
    histogram2d = jnp.histogram2d
    histogramdd = jnp.histogramdd


class Log(Enum):
    log = jnp.log
    log10 = jnp.log10
    log1p = jnp.log1p
    log2 = jnp.log2


class Exp(Enum):
    ...


class ModArithmetic(Enum):
    remainder = jnp.remainder


class Optimization(Enum):
    argmax = jnp.argmax
    argmin = jnp.argmin


# # TODO: organize numpy api
numpy_api = [
    add,
    all,
    allclose,
    alltrue,
    amax,
    amin,
    angle,
    any,
    append,
    apply_along_axis,
    apply_over_axes,
    arange,
    argsort,
    argwhere,
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
    average,
    bartlett,
    bfloat16,
    bincount,
    blackman,
    block,
    bool_,
    broadcast_arrays,
    broadcast_shapes,
    broadcast_to,
    c_,
    can_cast,
    cbrt,
    cdouble,
    ceil,
    character,
    choose,
    clip,
    column_stack,
    complex128,
    complex64,
    complex_,
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
    cov,
    cross,
    csingle,
    cumprod,
    cumproduct,
    cumsum,
    deg2rad,
    degrees,
    delete,
    diag,
    diagflat,
    diag_indices,
    diag_indices_from,
    diagonal,
    diff,
    digitize,
    divide,
    divmod,
    dot,
    double,
    dsplit,
    dstack,
    e,
    ediff1d,
    einsum,
    einsum_path,
    empty_like,
    equal,
    euler_gamma,
    exp,
    exp2,
    expand_dims,
    expm1,
    extract,
    eye,
    fabs,
    finfo,
    fix,
    flatnonzero,
    flexible,
    flip,
    fliplr,
    flipud,
    float_,
    float_power,
    floating,
    floor,
    floor_divide,
    fmax,
    fmin,
    fmod,
    frexp,
    full,
    full_like,
    gcd,
    geomspace,
    gradient,
    greater,
    greater_equal,
    hamming,
    hanning,
    heaviside,
    hsplit,
    hstack,
    hypot,
    i0,
    identity,
    iinfo,
    imag,
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
    less,
    less_equal,
    lexsort,
    linspace,
    load,
    logaddexp,
    logaddexp2,
    logspace,
    mask_indices,
    matmul,
    max,
    maximum,
    meshgrid,
    mgrid,
    min,
    minimum,
    mod,
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
    nanmedian,
    nanpercentile,
    nanquantile,
    nanmax,
    nanmean,
    nanmin,
    nanprod,
    nanstd,
    nansum,
    nanvar,
    ndarray,
    ndim,
    negative,
    newaxis,
    nextafter,
    nonzero,
    not_equal,
    number,
    object_,
    ogrid,
    ones_like,
    operator_name,
    outer,
    packbits,
    pad,
    percentile,
    pi,
    piecewise,
    polyadd,
    polyder,
    polyint,
    polymul,
    polysub,
    polyval,
    positive,
    power,
    prod,
    product,
    promote_types,
    ptp,
    quantile,
    r_,
    rad2deg,
    radians,
    ravel,
    ravel_multi_index,
    real,
    reciprocal,
    repeat,
    reshape,
    result_type,
    right_shift,
    rint,
    roll,
    rollaxis,
    rot90,
    round,
    row_stack,
    save,
    savez,
    searchsorted,
    select,
    set_printoptions,
    setdiff1d,
    setxor1d,
    shape,
    sign,
    signbit,
    signedinteger,
    sin,
    sinc,
    single,
    sinh,
    size,
    sometrue,
    sort,
    sort_complex,
    split,
    sqrt,
    square,
    squeeze,
    stack,
    std,
    subtract,
    sum,
    swapaxes,
    take,
    take_along_axis,
    tan,
    tanh,
    tensordot,
    tile,
    trace,
    trapz,
    transpose,
    tri,
    tril,
    tril_indices,
    tril_indices_from,
    trim_zeros,
    triu,
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
    var,
    vdot,
    vsplit,
    vstack,
    where,
    zeros_like,
]
