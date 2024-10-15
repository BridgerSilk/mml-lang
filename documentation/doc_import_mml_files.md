# Importing MML Files

In MML (Modern Markup Language), you can import other `.mml` files into your current file using the `!include` syntax. This feature allows you to modularize your code by separating components, styles, or any other reusable content into different files. It enhances maintainability and encourages code reuse across multiple pages.

---

## Using the `!include` Syntax

To import an MML file, use the `!include` directive followed by the path to the file you want to include. The path can be relative to the current file.

### Basic Syntax:

```mml
!include [./path/to/file.mml]
```

### Example:

```mml
!include [./components/header.mml]
```

In this example, the `header.mml` file is included, allowing you to use any components defined within it.

**Note:** The `!include` expression can **only** be used for importing other `.mml` files. For including external CSS stylesheets or JavaScript scripts, you still need to use the `(&style)` or `(&script)` syntax.

### Example for Including Styles and Scripts:

```mml
(&style link.[./styles/main.css])
(&script src.[./scripts/main.js])
```

---

## Use Cases for Importing MML Files

Importing MML files is beneficial in several scenarios:

### 1. Reusing Components Across Multiple Files

When you define components (like headers, footers, or navigation bars) in separate MML files, you can easily include them in multiple pages. This ensures a consistent look and feel across your website.

#### Example:

```mml
!include [./components/header.mml]
!include [./components/footer.mml]

(&mml lang.[en]) {
    (&body) {
        (@header)
        (&text){This is the main content of the page}.&text
        (@footer)
    }.&body
}.&mml
```

### 2. Organizing Your Code

By splitting your code into multiple MML files, you can keep your project organized. For example, you could have separate files for layout components, scripts, and styles.

#### Example Folder Structure:

```
project/
│
├── components/
│   ├── header.mml
│   ├── footer.mml
│   └── nav.mml
│
├── styles/
│   └── main.css
│
└── index.mml
```

In your `index.mml` file, you could include the header, footer, and navigation components like this:

```mml
!include [./components/header.mml]
!include [./components/nav.mml]
!include [./components/footer.mml]
```

### 3. Centralizing Common Styles and Scripts

You can create a separate MML file for common styles or scripts that need to be included in multiple pages, reducing duplication and ensuring consistency.

#### Example:

```mml
!include [./styles/global_styles.mml]

(&mml lang.[en]) {
    (&head) {
        (&title){My Site}.&title
    }.&head
    (&body) {
        (&text){Welcome to my website!}.&text
    }.&body
}.&mml
```

### 4. Keeping Your Project Scalable

As your project grows, importing MML files helps you manage complexity by allowing you to break down large components into smaller, manageable parts. This makes it easier to maintain and update your code over time.

---

## Important Notes

- The included MML files must be accessible in the specified path; otherwise, an error will occur.
- You can include the same file multiple times in different locations, but it's a good practice to avoid this unless necessary to prevent redundancy.
- Ensure that the component names in the included files are unique to avoid naming conflicts.

---

[<- Back to Doc Navigation](./doc_nav.md)
<br>
[Next Page ->](./doc_nesting_mml_files.md)