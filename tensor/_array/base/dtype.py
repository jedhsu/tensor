from enum import Enum

import jax.numpy as jnp

__all__ = [
    "Dtype",
    "u8",
    "u16",
    "u32",
    "u64",
    "i8",
    "i16",
    "i32",
    "i64",
    "f16",
    "f32",
    "f64",
]


class _Display_:
    name: str

    def __repr__(self):
        return f"Datatype[{self.name}]"


class Dtype(_Display_, Enum):
    dtype = jnp.dtype

    b8 = jnp.bool_

    u8 = jnp.uint8
    u16 = jnp.uint16
    u32 = jnp.uint32
    u64 = jnp.uint64

    i8 = jnp.int8
    i16 = jnp.int16
    i32 = jnp.int32
    i64 = jnp.int64

    f16 = jnp.float16
    f32 = jnp.float32
    f64 = jnp.float64


u8 = Dtype.u8
u16 = Dtype.u16
u32 = Dtype.u32
u64 = Dtype.u64

i8 = Dtype.i8
i16 = Dtype.i16
i32 = Dtype.i32
i64 = Dtype.i64

f16 = Dtype.f16
f32 = Dtype.f32
f64 = Dtype.f64
