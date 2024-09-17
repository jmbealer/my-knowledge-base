---
title: Data Structures
author: Justin Bealer
date_created: 2023-11-16, 04-00-30
date_modified: 2024-09-17, 09-29-53
reference: 
description: 
aliases: 
tags: 
---
# Data Structures

Data structures are a way of organizing and storing data so that they can be accessed and worked with efficiently. They define the relationship between the data, and the operations that can be performed on the data. There are many various kinds of data structures defined that make it easier for the data scientists and the computer engineers, alike to concentrate on the main picture of solving larger problems rather than getting lost in the details of data description and access.


from algorithms-JeffE
Prerequisites
The algorithms classes I teach at Illinois have two significant prerequisites:
a course on discrete mathematics and a course on fundamental data structures.
Consequently, this textbook is probably not suitable for most students as a first
i

PREFACE

course in data structures and algorithms. In particular, I assume at least passing
familiarity with the following specific topics:
• Discrete mathematics: High-school algebra, logarithm identities, naive
set theory, Boolean algebra, first-order predicate logic, sets, functions,
equivalences, partial orders, modular arithmetic, recursive definitions, trees
(as abstract objects, not data structures), graphs (vertices and edges, not
function plots).
• Proof techniques: direct, indirect, contradiction, exhaustive case analysis,
and induction (especially “strong” and “structural” induction). Chapter 0
uses induction, and whenever Chapter n−1 uses induction, so does Chapter n.
• Iterative programming concepts: variables, conditionals, loops, records,
indirection (addresses/pointers/references), subroutines, recursion. I do not
assume fluency in any particular programming language, but I do assume
experience with at least one language that supports both indirection and
recursion.
• Fundamental abstract data types: scalars, sequences, vectors, sets, stacks,
queues, maps/dictionaries, ordered maps/dictionaries, priority queues.
• Fundamental data structures: arrays, linked lists (single and double,
linear and circular), binary search trees, at least one form of balanced binary
search tree (such as AVL trees, red-black trees, treaps, skip lists, or splay
trees), hash tables, binary heaps, and most importantly, the difference
between this list and the previous list.
• Fundamental computational problems: elementary arithmetic, sorting,

searching, enumeration, tree traversal (preorder, inorder, postorder, level-
order, and so on).

• Fundamental algorithms: elementary algorism, sequential search, binary
search, sorting (selection, insertion, merge, heap, quick, radix, and so
on), breadth- and depth-first search in (at least binary) trees, and most
importantly, the difference between this list and the previous list.
• Elementary algorithm analysis: Asymptotic notation (o, O, Θ, Ω, ω),
translating loops into sums and recursive calls into recurrences, evaluating
simple sums and recurrences.

• Mathematical maturity: facility with abstraction, formal (especially recur-
sive) definitions, and (especially inductive) proofs; writing and following

mathematical arguments; recognizing and avoiding syntactic, semantic,
and/or logical nonsense.
The book briefly covers some of this prerequisite material when it arises in
context, but more as a reminder than a good introduction. For a more thorough
overview, I strongly recommend the following freely available references:
ii

Additional References

• Margaret M. Fleck. Building Blocks for Theoretical Computer Science. Version
1.3 (January 2013) or later available from http://mfleck.cs.illinois.edu/
building-blocks/.
• Eric Lehman, F. Thomson Leighton, and Albert R. Meyer. Mathematics for
Computer Science. June 2018 revision available from https://courses.csail.
mit.edu/6.042/spring18/. (I strongly recommend searching for the most
recent revision.)
• Pat Morin. Open Data Structures. Edition 0.1Gβ (January 2016) or later
available from http://opendatastructures.org/.

• Don Sheehy. A Course in Data Structures and Object-Oriented Design. Feb-
ruary 2019 or later revision available from https://donsheehy.github.io/

datastructures/.

Additional References
Please do not restrict yourself to this or any other single reference. Authors and
readers bring their own perspectives to any intellectual material; no instructor
“clicks” with every student, or even with every very strong student. Finding the
author that most effectively gets their intuition into your head takes some effort,
but that effort pays off handsomely in the long run.
The following references have been particularly valuable sources of intuition,
examples, exercises, and inspiration; this is not meant to be a complete list.
• Alfred V. Aho, John E. Hopcroft, and Jeffrey D. Ullman. The Design and
Analysis of Computer Algorithms. Addison-Wesley, 1974. (I used this textbook
as an undergraduate at Rice and again as a masters student at UC Irvine.)
• Boaz Barak. Introduction to Theoretical Computer Science. Textbook draft,
most recently revised June 2019. (Not your grandfather’s theoretical CS
textbook, and so much the better for it; the fact that it’s free is a delightful
bonus.)
• Thomas Cormen, Charles Leiserson, Ron Rivest, and Cliff Stein. Introduction
to Algorithms, third edition. MIT Press/McGraw-Hill, 2009. (I used the first
edition as a teaching assistant at Berkeley.)

• Sanjoy Dasgupta, Christos H. Papadimitriou, and Umesh V. Vazirani. Algo-
rithms. McGraw-Hill, 2006. (Probably the closest in content to this book,

but considerably less verbose.)
• Jeff Edmonds. How to Think about Algorithms. Cambridge University Press,
2008.
• Michael R. Garey and David S. Johnson. Computers and Intractability:
A Guide to the Theory of NP-Completeness. W. H. Freeman, 1979.

iii

PREFACE

• Michael T. Goodrich and Roberto Tamassia. Algorithm Design: Foundations,
Analysis, and Internet Examples. John Wiley & Sons, 2002.
• Jon Kleinberg and Éva Tardos. Algorithm Design. Addison-Wesley, 2005.
Borrow it from the library if you can.

• Donald Knuth. The Art of Computer Programming, volumes 1–4A. Addison-
Wesley, 1997 and 2011. (My parents gave me the first three volumes for

Christmas when I was 14. Alas, I didn’t actually read them until much later.)

• Udi Manber. Introduction to Algorithms: A Creative Approach. Addison-
Wesley, 1989. (I used this textbook as a teaching assistant at Berkeley.)

• Ian Parberry. Problems on Algorithms. Prentice-Hall, 1995 (out of print).
Downloadable from https://larc.unt.edu/ian/books/free/license.html after
you agree to make a small charitable donation. Please honor your agreement.
• Robert Sedgewick and Kevin Wayne. Algorithms. Addison-Wesley, 2011.
• Robert Endre Tarjan. Data Structures and Network Algorithms. SIAM, 1983.
• Class notes from my own algorithms classes at Berkeley, especially those
taught by Dick Karp and Raimund Seidel.
• Lecture notes, slides, homeworks, exams, video lectures, research papers,
blog posts, StackExchange questions and answers, podcasts, and full-fledged
MOOCs made freely available on the web by innumerable colleagues around
the world.
