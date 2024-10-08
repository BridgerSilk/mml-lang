# MML (Modern Markup Language) Syntax Guide

This guide covers the general syntax of MML (Modern Markup Language), which is fully based on HTML but introduces some new shorthand syntax and enhancements.

## Basic Structure

- **All HTML code is also valid MML code** since MML is built entirely on top of HTML.
- MML files use the `.mml` extension.
- The MML document type is defined with `doc!.mml`, which is equivalent to `<!DOCTYPE html>` in HTML.

### Example:

```mml
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

- Comments in MML are denoted using the `!//` syntax.
  
### Example:

```mml
!// This is a comment //!
```

---

## MML Tags

- MML uses `&` before any tag name to denote an HTML element.

### Example:

```mml
(&div)Content here.&div
```

- MML elements are similar to HTML tags but use `&` to represent the start of an element and `.` to close it.

---

## MML Attributes

- **New Way (Recommended)**: MML introduces a shorthand for attributes using the `.[ ]` notation.
  
    - Syntax: `attr.[value]`
    
### Example:

```mml
(&img src.[./image.png] alt.[An image])
```

- **Old Way**: You can still use the traditional HTML attribute syntax `!"value"`.

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

  **Note:** Braces `{}` for content are optional and only needed when content contains complex structures or whitespace.

### Example:

```mml
(&p cl.[paragraph])This is a paragraph.&p
```

Or with braces:

```mml
(&p cl.[paragraph]){This is a paragraph}.&p
```

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
        (&link rel.[stylesheet] link.[test.css])
    }.&head
    (&body) {

        !// add page content here //!

    }.&body
}.&mml
```

---

## More Information

For more advanced cases and MML-specific syntax, please refer to the `special_cases.md` file for additional details.