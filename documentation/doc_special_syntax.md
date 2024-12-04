# Special Syntax

MML (Modern Markup Language) introduces a few shorthand elements and attributes that differ from traditional HTML. This guide covers these special cases to help you understand how to use them effectively.

---

## Special Elements

In MML, some common HTML elements are represented by different syntax:

1. **Paragraph Element (`<p>`)**

   In MML, the paragraph element `<p>` is represented as `&text`.

   ```mml
   (&text cl.[paragraph]){This is a paragraph}.&text
   ```

2. **Container Element (`<div>`)**

   The HTML `<div>` element is represented as `&ct` in MML. This stands for "container".

   ```mml
   (&ct cl.[container]){This is a container}.&ct
   ```

3. **Root Element (`<html>`)**

   The HTML `<html>` element is represented by `&mml` in MML.

   ```mml
   (&mml lang.[en]) {
       (&head) { ... }.&head
       (&body) { ... }.&body
   }.&mml
   ```

4. **Script Element (`<script>`)**

   The HTML `<script>` element is represented as `&js` in MML. This stands for "javascript".

   ```mml
   (&js src.[myscript.js]) { } .&js
   ```

5. **Button Element (`<button>`)**

   The HTML `<button>` element is represented as `&btn` in MML.

   ```mml
   (&btn) { Test } .&btn
   ```

6. **Horizontal Line Element (`<hr>`)**

   The HTML `<hr>` element is represented as `&line` in MML.

   ```mml
   (&line)      
   ```

7. **Span Element (`<span>`)**

   The HTML `<span>` element is represented as `&ctin` in MML. This stands for "inline container" or "container inline".

   ```mml
   (&ctin) { Test } .&ctin
   ```

8. **Span Element (`<input>`)**

   The HTML `<input>` element is represented as `&in` in MML.

   ```mml
   (&in)
   ```

---

## Special Attributes

MML also introduces shorthand attribute names to simplify writing code:

1. **Class Attribute (`class`)**

   In MML, the `class` attribute is shortened to `cl`.

   ```mml
   (&ct cl.[main-container]){Content here}.&ct
   ```

2. **Link Attribute (`href`)**

   The `href` attribute in HTML, used primarily for links, is represented as `link` in MML.

   ```mml
   (&a link.[./about.html]){About}.&a
   ```

---

## Special Syntax for Document Type Declaration

MML uses a shorthand for the HTML doctype declaration:

- **HTML Doctype Declaration (`<!DOCTYPE html>`)**

   In MML, this is simplified to:

   ```mml
   doc!.mml
   ```

---

## Example Combining Special Syntax

Here’s an example that combines all the special cases:

```mml
doc!.mml
(&mml lang.[en]) {
    (&head) {
        (&title){MML Special Syntax Example}.&title
        (&link rel.[stylesheet] link.[style.css])
    }.&head
    (&body) {
        (&ct cl.[container]) {
            (&text cl.[intro-text]){Welcome to MML!}.&text
            (&a link.[./about.html]){Learn More}.&a
        }.&ct
    }.&body
}.&mml
```

In this example:
- `doc!.mml` replaces `<!DOCTYPE html>`.
- `&mml` is used instead of `<html>`.
- `&ct` replaces `<div>`, and `&text` replaces `<p>`.
- `cl` is used instead of `class`, and `link` replaces `href`.

---

Understanding these special cases will help streamline your development with MML, making your code more concise while retaining the full power of HTML.

---

[<- Back to Doc Navigation](./doc_nav.md)
<br>
[Next Page ->](./doc_vars.md)