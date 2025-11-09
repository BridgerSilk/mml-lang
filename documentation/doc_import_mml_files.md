# Importing MML Files

You can include other `.mml` files to reuse components or structure your code modularly.
Now MML also supports **native includes**, allowing you to import official MML components directly.

---

## Standard Includes

```mml
!include [./components/header.mml]
```

Includes a local `.mml` file from your project directory.

All exported components get imported when including an mml file.

---

## Native Includes

```mml
!include native [file.mml]
```

Native includes let you import files directly from the **official MML GitHub repository** under the `components/` directory.

For example:

```mml
!include native [std.mml]
```

This loads the official `std.mml` file and gives access to its components.

### Currently Available Native Components

* **std.mml** → Components: `testxyz`

---

## Notes

* Native includes always fetch from the official repository.
* Use them to access standard, reusable MML libraries.
* Custom includes remain supported via the normal `!include` syntax.

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