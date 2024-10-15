# Comments

In MML (Modern Markup Language), comments are converted to HTML comments during compilation. This means that comments written in MML will appear as standard HTML comments (`<!-- comment -->`) in the final output.

---

## Syntax for Comments

MML comments use the following syntax:

```mml
!// This is a comment //!
```

### Example:

```mml
(&ct cl.[container]) {
    !// This is a container for content //!
    (&text){Hello, World!}.&text
}.&ct
```

This will be converted to the following HTML:

```html
<div class="container">
    <!-- This is a container for content -->
    <p>Hello, World!</p>
</div>
```

---

## Best Practices for Comments

- **Clarity**: Use comments to explain sections of your code for future reference or for other developers.
  
- **Document Key Sections**: Focus comments on major sections, components, or variables.

---

## Comment Example

```mml
!// Define the title variable //!
var.title = "Welcome to My Site"

!// Header component //!
!export.header
(&text cl.[header]){:title:}.&text
!/export

(&mml lang.[en]) {
    (&body) {
        !// Call the header component //!
        (@header)

        (&text cl.[content]){This is the main content of the page}.&text
    }.&body
}.&mml
```

In the compiled HTML, the comments will be converted like this:

```html
<!-- Define the title variable -->
<!-- Header component -->
<!DOCTYPE html>
<html lang="en">
    <body>
        <!-- Call the header component -->
        <p class="header">Welcome to My Site</p>
        <p class="content">This is the main content of the page</p>
    </body>
</html>
```

---

MML comments behave just like HTML comments, ensuring that you can document your code without affecting its functionality.

---

[<- Back to Doc Navigation](./doc_nav.md)
<br>
[Next Page ->](./doc_creating_components.md)