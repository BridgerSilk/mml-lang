# Syntax

This guide covers the general syntax of MML (Modern Markup Language), which is fully based on HTML but introduces new shorthand syntax and enhancements handled with Python.

## Basic Structure

- **All HTML code is also valid MML code** since MML is built entirely on top of HTML.
- MML files use the `.mml` file extension.
- The MML document type is defined with `doc!.mml`, which is equivalent to `<!DOCTYPE html>` in HTML.

### Example of a simple MML document:

```
doc!.mml
(&mml lang.[en]) {
    (&head) {
        (&meta charset.[UTF-8])
        (&meta name.[viewport] content.[width=device-width, initial-scale=1.0])
        (&title){test}.&title
        (&link rel.[stylesheet] link.[test.css])
    }.&head
    (&body) {
        !// comment example //!
        
        static str test = "hello"

        (&nav) {
            (&a link.[./home.html]){Home}.&a
            (&a link.[./about.html]){About}.&a
        }.&nav

        (&main) {
            (&ct cl.[content] id.[abc] style.[margin:20px; padding:2px;]) {
                (&h2 cl.[heading]){Hello!}.&h2
                (&h1 cl.[heading test]){hi!}.&h1
                (&text cl.[test]){test}.&text
                (&ct id.[test]) {
                    (&img src.[./test.png] alt.[test img])
                }.&ct
            }.&ct
        }.&main
    }.&body
}.&mml
```

---

## MML Comments

- Comments in MML are denoted using the `!//` and `//!` syntax.
  
### Example:

```
!// This is a comment //!
```

---

## MML Tags

- MML uses `&` before any tag name to denote an HTML element.

### Example:

```mml
(&ct)Content here.&ct
```

- MML elements are similar to HTML elements but use `&` to represent the start of an element and `.` to close it.

---

## MML Attributes

- **New Solution (Recommended)**: MML introduces a shorthand for attributes using the `.[ ]` notation.
  
    - Syntax: `attr.[value]`
    
### Example:

```mml
(&img src.[./image.png] alt.[An image])
```

- **Old Solution**: You can still use the traditional MML attribute syntax `!"value"`. _(deprecated since version 0.0.4)_

### Example:

```mml
(&img src!"./image.png" alt!"An image")
```

---

## MML Elements

- In MML, you define an element using the following structure:
  
    ```mml
    (&tag attr.[value])content.&tag
    ```

  or using braces `{}` for the content (both are valid):

    ```mml
    (&tag attr.[value]){content}.&tag
    ```

    ### **Element Structure**:
    - `()` is used to define the element and its' attributes, events, etc.
    - `&element` is used to indicate the element, therefore needs to be written inside of the `()` _(all HTML elements can be used, some elements have a shorthand form, explanation below)_
    - `attr.[]` is used to define the attributes of the element
    - `{}` is usually used to define the content of an element, but is optional as explained below
    - `.&element` is used to indicate the end tag of the element

  **Note:** Braces `{}` for content are optional and only affect the syntax highlighting of the mml vsc extension.

### Example:

```mml
(&text cl.[paragraph])This is a paragraph.&text
```

Or with braces:

```mml
(&text cl.[paragraph]){This is a paragraph}.&text
```

**Note:** MML has some differences to HTML when it comes to element names. As you can see above, MML uses `(&text)` instead of the `<p>` element in HTML. <br>
[Learn more about special cases in MML.](./doc_special_syntax.md)

---

## Defining the Document Type

In MML, the document type is declared using:

```mml
doc!.mml
```

This is equivalent to `<!DOCTYPE html>` in HTML.

---

## MML Skeleton Code

Here is an example of a basic MML skeleton code that represents the structure of a typical MML document:

```mml
doc!.mml
(&mml lang.[en]) {
    (&head) {
        (&meta charset.[UTF-8])
        (&meta name.[viewport] content.[width=device-width, initial-scale=1.0])
        (&title){ example }.&title
        (&link rel.[stylesheet] link.[style.css])
    }.&head
    (&body) {

        !// add page content here //!

    }.&body
}.&mml
```

---

## More Information

For more advanced cases and MML-specific syntax, please refer to the [Special Syntax](./doc_special_syntax.md) documentation page.

---

[<- Back to Doc Navigation](./doc_nav.md)
<br>
[Next Page ->](./doc_special_syntax.md)