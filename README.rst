.. |Codecov| image:: https://codecov.io/gh/jedhsu/tensor/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/jedhsu/tensor
   :alt: Codecov

tensor
======

`tensor`{.:python} is a tensor manipulation library.

It provides the following features:

1. Patterns on the cell relationships are parametrized by a `Topology`{.:python}.

Consider checkerboard pattern. Note how this is a minimal syntax to describe the crux of a pattern, which is what "sets are open".

Consider a convolutional layer. (Run trhough).

2. References at the cell-level for network graph construction.


Features to add:
Framework for network architecture, framed as a network topology.

type annotation for arrays


[TODO} try and integrate in networkx complex graph structs

modularization of array operators. Every operator is a class. This enables symbolic expression computation at the type-level (what else?)

Tensor strengthens the type system the operator of numpy arrays.
* embeds tensors with a dependent type for their geometry. This can be later extended so a static checker can check that geometry of tensor operators is well-formed.
* provides type classes for all the 

Helpful because the file system structure helps infer the structure of the operators.

Geometry[11111]

Simple example on dualities.
