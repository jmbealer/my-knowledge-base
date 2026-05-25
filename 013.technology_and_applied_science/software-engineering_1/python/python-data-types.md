# what is Data Types WIP

a classification or category of various types of data, that states the possible
values that can be taken, how they are stored, and what range of operations are
allowed on them

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

You can get the data type of any object by using the type() function:

Type represents the kind of value and determines how the value can be used.
All data values in Python are encapsulated in relevant object classes.
Everything in Python is an object and every object has an identity, a type, and a value.
Extension modules which are written in C, Java, or other languages can define additional types.

To determine a variable's type in Python you can use the type() function.
The value of some objects can be changed.
Objects whose value can be changed are called mutable and objects whose value is unchangeable (once they are created) are called immutable.

None
This type has a single value. There is a single object with this value.
This object is accessed through the built-in name None.
It is used to signify the absence of a value in many situations, e.g., it is returned from functions that don't explicitly return anything. Its truth value is false.

Because Python is interpreted programming language and Python interpreter can determine which type of data is storing, so no need to define the data type of memory location.

The data type determines:

- The possible values for that type.
- The operations that can be done with that values.
- Conveys the meaning of data.
- The way values of that type can be stored.

Everything in Python programming is an object, and each object has its own unique identity(a type and a value).
: variable or object determines which operations can be applied to it.

Primitive
: data types which are pre-defined and supported by the programming language.
Non-Primitive
: data types which are derived from the primitive data types and offer
increased functionality.

.Data Structure (Data Types in Python)
**Immutable** Data
: immutable objects
: Immutable objects can be read but not modified (rewritten) after being created. 
: For example, a string is immutable, so you cannot add caracters to a string without reassign the string itself.

**Mutable** Data
: mutable objects
: Mutable Objects can be modified after being created (elements can be changed).


- Text Type: [str](python-strings.md) WIP
- [Numeric](python-numeric.md) Types: [python int](python-int.md), [python float](python-float.md), [python complex](python-complex.md) WIP
- Sequence Types: [python list](python-list.md), [python tuple](python-tuple.md), [python range](python-range.md) WIP
- Mapping Type: [python dict](python-dict.md) WIP
- Set Types: [python set](python-set.md), [frozenset](python-frozenset.md) WIP
- Boolean Type: [python bool](python-bool.md) WIP
- Binary Types: bytes, bytearray, memoryview WIP
[bytes bytearray](python-bytes-bytearray.md)

- Type Conversion ([Casting](python-casting.md)) WIP

  #python #datatypes
