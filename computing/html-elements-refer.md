---
title: HTML Element Reference
author: Justin Bealer
date_created: 2024-04-04, 05-24-29
date_modified: 2024-09-17, 09-30-01
reference: 
description: 
aliases: 
tags: 
---
# HTML Element Reference

## Links

https://www.w3schools.com/tags/ref_byfunc.asp

Tag   Description

## Basic HTML

```html
<!DOCTYPE html> Defines the document type
- What at the beginning of all HTML documents
<html>...</html> Defines the root of an HTML document
<head>...</head> Contains metadata/information for the document
  metadata is data about the HTML document
    metadata is not displayed
  metadate typically define the document title, character set, styles, scripts, and other meta information
    <title></title>
    <style></style>
    <base>
    <link>
    <meta>
    <script>
    <noscript>
<title>...</title> Defines a title for the document
<body> Defines the document's body
<h1> to <h6> Defines HTML headings
<p> Defines a paragraph
<br> Defines a single line line-break
<hr> Defines a thematic change in the content
<!--...--> Defines a comment
  used to insert comments in the source code
  are not displayed in the browsers
  explan your code
```

## Formatting

```html
<acronym> Defines an acronym Not supported in HTML5. Use <abbr> instead.
<abbr> Defines an abbreviation or an acronym
<address> Defines contact information for the author/owner of a document
<b> Defines bold text
<bdi> Isolates a part of text that might be formatted in a different direction from other text outside it
<bdo> Overrides the current text direction
<big> Defines big text Not supported in HTML5. Use CSS instead.
<blockquote> Defines a section that is quoted from another source
<center> Defines centered text Not supported in HTML5. Use CSS instead.
<cite> Defines the title of a work
<code> Defines a piece of computer code
<del> Defines text that has been deleted from a document
<dfn> Specifies a term that is going to be defined within the content
<em> Defines emphasized text 
<font> Defines font, color, and size for text Not supported in HTML5. Use CSS instead.
<i> Defines a part of text in an alternate voice or mood
<ins> Defines a text that has been inserted into a document
<kbd> Defines keyboard input
<mark> Defines marked/highlighted text
<meter> Defines a scalar measurement within a known range (a gauge)
<pre> Defines preformatted text
<progress> Represents the progress of a task
<q> Defines a short quotation
<rp> Defines what to show in browsers that do not support ruby annotations
<rt> Defines an explanation/pronunciation of characters (for East Asian typography)
<ruby> Defines a ruby annotation (for East Asian typography)
<s> Defines text that is no longer correct
<samp> Defines sample output from a computer program
<small> Defines smaller text
<strike> Defines strikethrough text Not supported in HTML5. Use <del> or <s> instead.
<strong> Defines important text
<sub> Defines subscripted text
<sup> Defines superscripted text
<template> Defines a container for content that should be hidden when the page loads
<time> Defines a specific time (or datetime)
<tt> Defines teletype text Not supported in HTML5. Use CSS instead.
<u> Defines some text that is unarticulated and styled differently from normal text
<var> Defines a variable
<wbr> Defines a possible line-break
```

## Forms and Input - I'm HERE

```html
<form> Defines an HTML form for user input
<input> Defines an input control
<textarea> Defines a multiline input control (text area)
<button> Defines a clickable button
<select> Defines a drop-down list
<optgroup> Defines a group of related options in a drop-down list
<option> Defines an option in a drop-down list
<label> Defines a label for an <input> element
<fieldset> Groups related elements in a form
<legend> Defines a caption for a <fieldset> element
<datalist> Specifies a list of pre-defined options for input controls
<output> Defines the result of a calculation
```

## Frames

```html
<frame> Defines a window (a frame) in a frameset Not supported in HTML5.
<frameset> Defines a set of frames Not supported in HTML5.
<noframes> Defines an alternate content for users that do not support frames Not supported in HTML5.
<iframe> Defines an inline frame
```

## Images

```html
<img> Defines an image
<map> Defines an image map
<area> Defines an area inside an image map
<canvas> Used to draw graphics, on the fly, via scripting (usually JavaScript)
<figcaption> Defines a caption for a <figure> element
<figure> Specifies self-contained content
<picture> Defines a container for multiple image resources
<svg> Defines a container for SVG graphics
```

## Audio / Video

```html
<audio> Defines embedded sound content
<source> Defines multiple media resources for media elements (<video> and <audio>)
<track> Defines text tracks for media elements (<video> and <audio>)
<video> Defines embedded video content
```

## Links

```html
<a> Defines a hyperlink
<link> Defines the relationship between a document and an external resource (most used to link to style sheets)
<nav> Defines navigation links
```

## Lists

```html
<menu> Defines an unordered list
<ul> Defines an unordered list
<ol> Defines an ordered list
<li> Defines a list item
<dir> Defines a directory list Not supported in HTML5. Use <ul> instead.
<dl> Defines a description list
<dt> Defines a term/name in a description list
<dd> Defines a description/value of a term in a description list
```

## Tables

```html
<table> Defines a table
<caption> Defines a table caption
<th> Defines a header cell in a table
<tr> Defines a row in a table
<td> Defines a cell in a table
<thead> Groups the header content in a table
<tbody> Groups the body content in a table
<tfoot> Groups the footer content in a table
<col> Specifies column properties for each column within a <colgroup> element 
<colgroup> Specifies a group of one or more columns in a table for formatting
```

## Styles and Semantics

```html
<style> Defines style information for a document
<div> Defines a section in a document
<span> Defines a section in a document
<header> Defines a header for a document or section
<hgroup> Defines a header and related content
<footer> Defines a footer for a document or section
<main> Specifies the main content of a document
<section> Defines a section in a document
<search> Defines a search section
<article> Defines an article
<aside> Defines content aside from the page content
<details> Defines additional details that the user can view or hide
<dialog> Defines a dialog box or window
<summary> Defines a visible heading for a <details> element
<data> Adds a machine-readable translation of a given content
```

## Meta Info

```html
<meta> Defines metadata about an HTML document
<base> Specifies the base URL/target for all relative URLs in a document
<basefont> Specifies a default color, size, and font for all text in a document Not supported in HTML5. Use CSS instead.
```

## Programming

```html
<script> Defines a client-side script
<noscript> Defines an alternate content for users that do not support client-side scripts
<applet> Defines an embedded applet Not supported in HTML5. Use <embed> or <object> instead.
<embed> Defines a container for an external application
<object> Defines a container for an external application
<param> Defines a parameter for an object
```
