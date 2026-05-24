---
title: AsciiDoc
author: Justin Bealer
date_created: 2023-11-16, 04-00-30
date_modified: 2024-09-17, 11-01-02
reference: 
description: 
aliases: 
tags: 
---
# AsciiDoc
= AsciiDoc

* Ascii is a markup language similar to Markdown.
* Created in 2002 by Stuart Rackham
== Document Header

* Headers are optional and can't contain blank lines. It must be offset from
  content by at least one blank line.
* Title Only
** = Document Title

** First sentence of document.
* Title and Author
** = Document Title
** First Last <first.last@learnxinyminutes.com>

** Start of this document.
* Multiple Authors
** = Document Title
** John Doe <john@go.com>;k Jane Doe<jane@yo.com>;
** Black Beard <beardy@pirate.com>

** Start of a doc with multiple authors.
* Revision Line (requires an  author line)
** = Doc Title V1
** Potato Man <chip@crunchy.com>
** v1.0, 2016-01-13

** This article about chips is  going to be fun.
* Paragraphs
*
== Attributes

== Headers

* = Level 1
* == Level 2
* === Level 3
* ==== Level 4
* ===== Level 5
* ====== Level 6

== Paragraphs

.Optional Title
Usual
paragraph.

.Optional Title

Literal paragraph.
  Must be indented.

You don't need anything special for paragraphs.

Add a blank line between paragraphs to separate them.

To create a line blank add a +
and you will receive a line break!

== Blocks

.Optional Title
----
*Listing* Block

Use: code or file listings
----

== Text

forced +
line break

normal, _italic_, *bold*, +mono+.
*_bold and italic_*
`mono`
== Macros: links, images & include
== Lists

.Bulleted
* bullet
** sub-bullet
*** sub-sub-bullet

.Ordered
. number
.. sub-number
... sub-sub-number

== Tables
