Title: Introduction to DyND

DyND is C++ library for dynamic, multidimensional arrays, aiming to
target C++, Python, and eventually other languages in a first class
manner. DyND aspires to become multi-language dynamic array infrastructure
upon which array-oriented systems are built, like NumPy has for Python.

## Types

The dynamic type system forms the foundation of DyND, describing how
data is laid out in memory and how functions transform that data.
Some primitive value types are "int32", "float64", and "string".
Array types have their dimensions prepended like "16 * int32" and
"3 * var * float32". These types can be composed into tuples
"(int32, float64, bool)" or structs
"{present: bool, value: int32, name: string}".

Types can also be patterns, which don't represent a particular data layout,
but rather match against sets of types which fit into the pattern.
For example "Dim * T" is an arbitrary one-dimensional array. This is
how parameters of DyND's callables objects are typically specified.

## Arrays

Data in DyND is stored in the `nd::array` object, which combines a
type, some array layout metadata, and a block of memory for the data.
Atomically reference-counted smart pointers are used to manage the
memory blocks, allowing for the view operations on data familiar
to NumPy users.

## Computation

Computations in DyND are represented as `callable` objects, which
encapsulate how data transforms from one data layout to another
in an array-oriented fashion. Callables are composable, for example
a callable operating on scalars can be lifted to a callable which
operates elementwise, using standard broadcasting rules for combining
dimensions.
