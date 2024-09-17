---
title: What is Markdown?
author: Justin Bealer
date_created: 2023-11-16, 04-00-30
date_modified: 2024-09-17, 11-01-01
reference: 
description: 
aliases: 
tags: 
---
# What is Markdown?


[//]:# (This may be the most platform independent comment)
  - Can be converted into HTML/XHTML and other formats
  - It's main purpose is readability and ease of use

## What Is It Used For ?

  - Readme Files (Githup, etc)
  - Forum & Blog Posts
  - Used In Many Static Site Generators

## Syntax

### Headings

**Headings** to create a heading, add number signs (#)in front of a word or phrase.
**Heading Best Practices** separate paragraph and heading with one or more blank lines.
- # Heading 1
- ## Heading 2
- ### Heading 3
- #### Heading 4
- ##### Heading 5
- ###### Heading 6

### Paragraphs

**Paragraphs** to create a paragraphs, use a blank line to separate one or more
lines of text.
**Paragraphs Best Practices** don't indent paragraphs with spaces or tabs.

### Emphasis

 **Emphasis** add emphasis by making text bold or italic.
- **Bold (Strong)** to bold text, add two asterisks (**) or underscores (__)
- **Bold Best Practices** use asterisks
  - **Bold**
  - **Bo**ld
- ***Italic*** to italicize text, add one asterisks (*) or underscores (_)
- ***Italic Best Practices*** use asterisks
  - *Italic*
  - *Ita*lic
- ***Bold and Italic*** add three asterisks (***) or underscores (___)
- ***Bold and Italic Best Practices*** use asterisks
  - ***Bold and Italic***
  - ***Bold and Ita***lic
- **Strike-through** use two (~~)
  - ~~Text~~
  - ~~Te~~xt
- **Highlight** use two (==)
  - ==Highlights==
  - ==High==lights

### Block-quotes

- **Blockquotes** To create a blockquote, add a > in front of a paragraph.
  > This is a Blockquote
- **Blockquotes with Multiple Paragraphs** Add a > on the blank lines between
the paragraphs.
  > This is a Blockquote
  >
  > This is a Blockquote with Multiple Paragraphs
- **Nested Blockquotes** Add a >> in front of the paragraph you want to nest.
  > This is a Blockquote
  >
  >> This is a Nested Blockquote
- **Blockquotes with Other Elements** can contain other Markdown formatted
elements. Not all elements can be used.
  > #### Heading 4
  >
  > - Item 1
  > - Item 2
  >
  > *Italic* to *Bold*.

### Lists

**Lists** You can organize items into ordered and unordered lists.
- **Ordered Lists** To create an ordered list, add line items with numbers
followed by periods.
The numbers don't have to be in numerical order, but the list start with the
number one.
1. First item
1. Second item
1. Third item
    1. Indented item
    1. Indented item
1. Fourth item
**Unordered Lists** To create unordered list, add dashes (-), asterisks (),
or plus signs (+) in front of line items. Indent one or more items to create a
nested list.

- First
- Second
- Third
  - Nested
  - Nested
- Fourth

- **Adding Elements in Lists** To add another elements in a list while
preserving the continuity of the list, indent the elements four spaces or one
tab, as shown in the following examples.
- **Paragraphs**
  - First
  - Second

Paragraph

        - Third
      - **Blockquotes**
        - First
        - Second

          > Blockquote

        - Third
      - **Code Blocks** are normally indented four spaces or one tab. When
          they're in a list, indent them eight spaces or two tabs.
        1. First
        1. Second

                <html>
                <head>
                    <title>Test</title>
                </head>

        1. Third
      - **Images**
        1. First
        1. Second

          ![Tux, the Linux mascot](/assets/images/tux.png)

        1. Third
  - **Code** To denote a word or phrase as code, enclose it in backticks (\`).
    - At the command prompt, type `vim`.
    - **Escaping Backticks** If the word or phrase you want to denote as code
        includes one or more backticks, you can escape it by enclosing the word
        or phrase in double backticks (\`\`).
      - ``Use `code` in your Markdown file.``
    - **Code Blocks** To create code blocks, indent every line of the block by
        at least four spaces or one tab.

          <html>
              <head>
              </head>
            </html>

      to create code block without indenting lines, use fenced code blocks.
  - **Horizontal Rules** To create a horizontal rule, use three or more
      asterisks (***), dashes (---), or underscores (___) on a line by
      themselves.
    
    ***

    ---

    ___

    - **Horizontal Rule Best Practices** For compatibility, put blank lines
        before and after horizontal rules.

      Try to put a blank line before...

      ---

      ...and after a horizontal rule.
  - **Links** To create a link, enclose the link text in brackets (e.g.. [Duck
      Duck Go]) and the follow it immediately with the URL in parentheses (e.g..
      (https://duckduckgo.com)).

    My favorite search engine is [Duck Duck Go](https://duckduckgo.com).

    - **Adding Titles** To add a title, enclose it in parentheses after the URL.

      My favorite search engine is [Duck Duck Go](https://duckduckgo.com"The
      best search engine for privacy").

    - **URLs and Email Addresses** To quickly turn URL or email address into a
        link, enclose it in angle brackets (<>).

      <https://www.markdownguide.org>

      <fake@example.com>

    - **Formatting Links** To emphasize links, add asterisks before and after
        the brackets and parentheses. To denote links as code, add backticks in
        the brackets.

      I love supporting the **[EFF](https://eff.org>)**.

      This is the *[Markdown Guide](https://www.markdownguide.org)*.

      See the section on [`code`](markdown.md#code).

    - **Reference-style Links** are a special kind of link that make URLs easier
        to display and read in Markdown. Reference-style links are constructed
        in two parts: the part you keep inline with your text and the part you
        store somewhere else in the file to keep the text easy to read.
      - **Formatting the First Part of the Links** is formatted with two sets of
          brackets. The first set of brackets surrounds the text that should
          appear linked. The second set of brackets display a label used to
          point to the link you're storing elsewhere in your document.

        Although not require, you can include a space between the first and
        seconsecond set of brackets. The label in the secomnd set of brackets is
        not case sensitive and can include letter, numbers, sapce, or
        punctuation.

        This means the following example formats are roughly equivalent for the
        first part of the link:

          - [hobbit-hole][1]
          - [hobbit-hole] [1]

      - **Formatting the Second Part of the Links** is formatted with the
          following attributes:
        1. The label, in brackets, followed immediately by a colon and at least
           one space (e.g. [label]: ).
        1. The URL for the link, which you can optionally enclose in angle
           brackets.
        1. The optional title for the link, which you can enclose in double
           quotes, single quotes, or parentheses.

        This means the following example formats are all roughly equivalent for
        the secomnd part of the link:

          [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle
          [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"
          [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'
          [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit Lifestyle)
          [1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> "Hobbit
          lifestyles"
          [1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> 'Hobbit
          lifestyles'
          [1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> (Hobbit
          lifestyles)

        You Can place this secomnd part of the link anywhere in your Markdown
        document. Some people place them immediately after the paragraph in
        which they appear while other people place at the end of the document
        (like endnotes or footnotes).

    - **An Example Putting the Parts Together** Say you add a URL as a standard
        URL link to a paragraph and it looks like this in Markdown:

      In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet
      hole, filled with the ends of worms and an oozy smell, nor yet a dry,
      bare, sandy hole with nothing in it to sit down on or to eat: it was a
      [hobbit-hole](https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit
      lifestyles"), and that mean
        

    Though it may point to interesting additional information, the URL as
    displayed really doesn’t add much to the existing raw text other than making
    it harder to read. To fix that, you could format the URL like this instead:

      In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet
      hole, filled with the ends of worms and an oozy smell, nor yet a dry,
      bare, sandy hole with nothing in it to sit down on or to eat: it was a
      [hobbit-hole][1], and that means comfort.

      [1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> "Hobbit lifestyles"

  - **Links Best Practices** Markdown applications don't agree on how to handle
      spaces in middle of a URL. For compatibility, try to URL encode any spaces
      with %20.

    [link](https://wwww.example.com/my%20great%20page)
  - **Images** To add an image, add an exclamation mark (!), followed by alt
      text in brackets, and the path or URL to the image asset in parentheses.
      You can optionally add a title after the URL in the parentheses.

    ![Philadelphia's Magic Gardens. This place was so
    cool!](/assets/images/philly-magic-gardens.jpg "Philadelphia's Magic
    Gardens")
    - **Linking Images** To add a link to an image, enclose the Markdown for the
        image in brackets, and then add the link in parentheses.
      
      [![An old rock in the desert](/assets/images/shiprock.jpg "Shiprock, New
      Mexico by Beau
      Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)
        
  - **Escaping Characters**To display a literal character that would otherwise
      be used to format text in a Markdown document, add a backslash (\) in
      front of the character
    \* Without the backslash, this would be a bullet in an unordered list.

    - **Characters You Can Escape** You can use a backslash to escape the
        following characters.
        | Character | Name |
        | --- | --- |
        | \ | backslash |
        | \` | backtick |
        | * | asterisk |
        | _ | underscore |
        | {} | curly braces |
        | [] | brackets |
        | () | parentheses |
        | # | pound sign |
        | + | plus sign |
        | - | minus sign (hyphen) |
        | . | dot |
        | ! | exclamation mark |
        | \| | pipe |

  - **HTML** Many Markdown applications allow you to use HTML tags in
      Markdown-formatted text. This is helpful if you prefer certain HTML tags
      to Markdown syntax. For example, some people find it easier to use HTML
      tags for images. Using HTML is also helpful when you need to change the
      attributes of an elements, like specifying the color of text or changing
      the width of an image.

    - To use HTML, place the tags in the text of your Markdown-formatted file.
      
      This **word** is bold. This <em>word</em> is italic.
      
    - **HTML Best Practices** For security reasons, not all Markdown
        applications support HTML in Markdown documents. When in doubt, check
        your Markdown application’s documentation. Some applications support
        only a subset of HTML tags.

        Use blank lines to separate block-level HTML elements like \<div>,
        \<table>, \<pre>, and \<p> from the surrounding content. Try not to
        indent the tags with tabs or spaces — that can interfere with the
        formatting.

        You can’t use Markdown syntax inside block-level HTML tags. For example,
        \<p>italic and **bold**\</p> won’t work.


---
horizontal rule
___

> This is a quote

[This is a link](https://www.google.com)

[This is a link](https://www.google.com "This is a link with Tile")

unorder lists
- item
- item
  - nested item

1. item
1. item
  2. nested
  1. nested

Inline Code Block

`<p>This is a paragraph</p>`

Images

![Markdown Logo](https://markdown-here.com/img/icon256.png)

Github Markdown
  - Code Blocks ```[lanuage] the code```


Tables
| Name | Email |
| --- | --- |
| John Doe | john@gmail.com |
| Jane Doe | jane@gmail.com |

Task list
- [x] Task 1
- [x] Task 2
- [ ] Task 3

  #markdown
