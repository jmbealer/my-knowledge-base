what is html
  html stands for hypertext markup language
  
 HTML is the skeleton of all web pages.

HTML provides structure to the content appearing on a website, such as images, text, or videos.

HTML stands for HyperText Markup Language:

    A markup language is a computer language that defines the structure and presentation of raw text.
    In HTML, the computer can interpret raw text that is wrapped in HTML elements.
    HyperText is text displayed on a computer or device that provides access to other text through links, also known as hyperlinks. You probably clicked on a couple of hyperlinks on your way to this Codecademy course.


HTML Anatomy

HTML is composed of elements. These elements structure the webpage and define its content. Let’s take a look at how they’re written.

The diagram to the right displays an HTML paragraph element. As we can see, the paragraph element is made up of:

    An opening tag (<p>)
    The content (“Hello World!” text)
    A closing tag (</p>)

A tag and the content between it is called an HTML element. There are many tags that we can use to organize and display text and other types of content, like images.

Let’s quickly review each part of the element pictured:

    HTML element (or simply, element) — a unit of content in an HTML document formed by HTML tags and the text or media it contains.

    HTML Tag — the element name, surrounded by an opening (<) and closing (>) angle bracket.

    Opening Tag — the first HTML tag used to start an HTML element. The tag type is surrounded by opening and closing angle brackets.

    Content — The information (text or other elements) contained between the opening and closing tags of an HTML element.

    Closing tag — the second HTML tag used to end an HTML element. Closing tags have a forward slash (/) inside of them, directly after the left angle bracket.

HTML Structure

HTML is organized as a collection of family tree relationships. As you saw in the last exercise, we placed <p> tags within <body> tags. When an element is contained inside another element, it is considered the child of that element. The child element is said to be nested inside of the parent element.

<body>
  <p>This paragraph is a child of the body</p>
</body>

In the example above, the <p> element is nested inside the <body> element. The <p> element is considered a child of the <body> element, and the <body> element is considered the parent. You can also see that we’ve added two spaces of indentation (using the space bar) for better readability.

Since there can be multiple levels of nesting, this analogy can be extended to grandchildren, great-grandchildren, and beyond. The relationship between elements and their ancestor and descendent elements is known as hierarchy.
