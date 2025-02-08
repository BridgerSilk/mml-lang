# Using Components

Once you've defined a component in MML, using it is straightforward. Components are reusable blocks of code that can be called anywhere in the same file or even across multiple files when imported.

---

## How to Call a Component

To call a component, use the `(@component_name)` syntax. This will inject the component wherever it's called.

### Basic Example:

```mml
(@header)
```

In this example, the `header` component is called and inserted at this location in the document.

---

## Calling a Component Multiple Times

You can call the same component multiple times within a file. Each time the component is called, it renders the defined structure wherever it's placed.

### Example:

```mml
(@header)
(&text){This is the body content}.&text
(@header)
```

This would render the `header` component at two separate locations in the document.

---

## Using Components Across Files

If you want to reuse a component from one file in another file, you need to include the file or folder of multiple files containing the component definition using the `!include` syntax. You can also include external files or folders from the web using valid http/https links. Once included, you can call the component as if it were defined in the current file.

### Example:

```mml
!// including single mml files //!
!include [./components.mml]
!include [https://github.com/user/repo/tree/main/folder/file.mml]

!// including folders containing multiple mml files //!
!include [./folder/folder2]
!include [https://github.com/user/repo/tree/main/folder/folder2]

(@header)
(@footer)
```

In this case, `components.mml` contains the `header` and `footer` components, which can now be used in the current file.

---

## Using Variables Inside Components

You can pass dynamic content to components using variables. Make sure that the variables are defined in the same file where the component is called.

### Example:

```mml
var.message = "Welcome to My Website"

(@header)
(&text){:message:}.&text
(@footer)
```

In this example, the variable `message` is used to insert dynamic content into the component. You can learn more about variables [here](./doc_vars.md).

---

## Case Sensitivity in Component Calls

It's important to note that component names are **case-sensitive**. This means that calling `(@Header)` is different from calling `(@header)`. Make sure to match the case exactly as it was defined.

### Example:

```mml
(@Header)  !// Calls the Header component //!
(@header)  !// Calls the header component //!
```

---

## Why Use Components Across Files?

By splitting components across files and including them where needed, you create a more modular and maintainable project structure. You can define common components like headers and footers once, and reuse them across multiple pages of your website.

---

[<- Back to Doc Navigation](./doc_nav.md)
<br>
[Next Page ->](./doc_import_mml_files.md)