---
title: Complex
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 11-01-02
reference: 
description: 
aliases: 
tags: 
---
# Complex

immutable
Complex numbers also called Imaginary numbers
Complex number is a number with a real part and an imaginary part.
Complex:`<real part>+<imaginary part>j`
  to create a complex real part , then plus sign , imaginary part with j at the end
Complex numbers have two properties, .real and .imag
.real returns the real part of a complex number
  <variable>.real
.imag returns the imaginary part of a complex number
  <variable>.imag
.real and .imag returns as floats
.conjugate() method returns conjugate of the number
  <variable>.conjugate()
conjugate of a complex number has the same properties but opposite sign.
floor division doesn't work on complex numbers
Can't convert complex numbers into another number type.


.Complex Examples:
x = 3+5j # complex
x.real # 3.0
x.imag # 5.0
x.conjugate() # 3-5j

  #python #datatypes
