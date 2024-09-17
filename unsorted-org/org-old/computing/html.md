---
title: HTML
author: Justin Bealer
date_created: 2023-11-16, 04-00-38
date_modified: 2024-09-17, 11-01-04
reference: 
description: 
aliases: 
tags: 
---
# HTML

## What is HTML?

HTML stands of Hyper Text Markup Language.
HTML is the standard markup language for creating Web pages.
HTML describes the structure of a Web page.
HTML consists of a series of elements.
HTML elements tell the browser how to display the content.
HTML elements label pieces of content; such as "this is a heading",


Hypertext defines the link between the web pages.
A markup language is used to define the text document within tag which
defines the structure of web pages.


is a markup language that structure web pages.


HTML is the skeleton of all web pages.
HTML provides structure to the content appearing on a website, such as images, text, or videos.
A markup language is a computer language that defines the structure and presentation of raw text.


HTML Anatomy

html element
opening tag + content + closing tag = element
HTML is composed of elements. These elements structure the webpage and define its content. Let’s take a look at how they’re written.
A tag and the content between it is called an HTML element.


    HTML element (or simply, element) — a unit of content in an HTML document formed by HTML tags and the text or media it contains.

    HTML Tag — the element name, surrounded by an opening (<) and closing (>) angle bracket.

    Opening Tag — the first HTML tag used to start an HTML element. The tag type is surrounded by opening and closing angle brackets.

    Content — The information (text or other elements) contained between the opening and closing tags of an HTML element.

    Closing tag — the second HTML tag used to end an HTML element. Closing tags have a forward slash (/) inside of them, directly after the left angle bracket.



element = <element_name>..content..</element_name>
opening tag <element_name>
closing tag </element_name>
void elements dont have a closing tag or any contents:
  <img>,<meta>,<link> and <input>

 what is an html element?
An HTML element is defined by a start tag, some content, and an end tag:
<tagname>Content goes here...</tagname>
The HTML element is everything from the start tag to the end tag.




\<html> element is the root element of an HTML page.
\<head> element contains meta information about the HTML page.
\<title> element specifies a title for the HTML page.
  which is shown in the browser's title bar or in the page's tab.
\<body> element defines the document's body;
  and is container for all the visible contents, such as heading,
  paragraphs, images, hyperlinks, tables, lists, etc.
\<h1> element defines a large heading.
\<p> element defines a paragraph.




    HTML stands for HyperText Markup Language and is used to create the structure and content of a webpage.
    Most HTML elements contain opening and closing tags with raw text or other HTML tags between them.
    HTML elements can be nested inside other elements. The enclosed element is the child of the enclosing parent element.
    Any visible content should be placed within the opening and closing <body> tags.
    Headings and sub-headings, <h1> to <h6> tags, are used to provide titles for sections of content.
    <p>, <span> and <div> tags specify text or blocks.
    The <em> and <strong> tags are used to emphasize text.
    Line breaks are created with the <br> tag.
    Ordered lists (<ol>) are numbered and unordered lists (<ul>) are bulleted.
    Images (<img>) and videos (<video>) can be added by linking to an existing source.



    <!DOCTYPE html>, the declaration specifying the version of HTML for the browser
    The <html> tags that enclose all of your HTML code
    The <head> tag that contains the metadata of a webpage, such as its <title>



    The <!DOCTYPE html> declaration should always be the first line of code in your HTML files. This lets the browser know what version of HTML to expect.
    The <html> element will contain all of your HTML code.
    Information about the web page, like the title, belongs within the <head> of the page.
    You can add a title to your web page by using the <title> element, inside of the head.
    A webpage’s title appears in a browser’s tab.
    Anchor tags (<a>) are used to link to internal pages, external pages or content on the same page.
    You can create sections on a webpage and jump to them using <a> tags and adding ids to the elements you wish to jump to.
    Whitespace between HTML elements helps make code easier to read while not changing how elements appear in the browser.
    Indentation also helps make code easier to read. It makes parent-child relationships visible.
    Comments are written in HTML using the following syntax: <!-- comment -->.

## HTML Documents


All HTML documents must start with a document type declaration:
  <!DOCTYPE html>
The HTML document itself begins with <html> and ends with </html>.
The visible part of the HTML document is between <body> and </body>.


The <!DOCTYPE> Declaration

The <!DOCTYPE> declaration represent the document type, and helps
browser to display web pages correctly.

It must only appear once, at the top of the page (before any HTML tags).
The <!DOCTYPE> declaration is not case sensitive.
declartion of HTML = <!DOCTYPE html>

\<!DOCTYPE html> declaration defines that this document is an HTML
document.

HTML headings

HTML heading are define by <h1> to <h6> tags.
<h1> defines the most important heading.
<h6> defines the least important heading.

HTML paragraphs
HTML paragraphs are define by the <p> tag

HTML links
HTML links are define by the <a> tag
href attribute defines the link destination.

HTML images
HTML images are define by the <img> tag
the source file (src), alternative text (alt), width, and height are
attributes.
 

 html page structure
A simple HTML document

  ```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>heading</h1>
<p>paragraph.</p>

</body>
</html>
```
