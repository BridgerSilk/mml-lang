# Creating Components

Components in MML (Modern Markup Language) allow you to reuse blocks of code across multiple parts of your project. This not only makes your code more modular and maintainable, but it also speeds up development and ensures consistency across your website.

---

## Defining a Component

To create a component in MML, use the `!export` and `!/export` syntax. Components encapsulate MML elements, allowing them to be reused anywhere within the same file or across multiple files.

### Basic Syntax:

```mml
!export.component_name
    !// Component code here //!
!/export
```

### Example:

```mml
!export.header
    (&ct cl.[header]) {
        (&text){Welcome to My Site}.&text
    }.&ct
!/export
```

In this example, the `header` component is defined and can be used anywhere in the same file or in other files when included.

---

## Using a Component

To use (or call) a component, simply use the `(@component_name)` syntax:

```mml
(@header)
```

This will insert the `header` component wherever it’s called, rendering the `&ct` element and its content.

---

## Reusing Components Across Multiple Files

You can also use components defined in one file in other MML files by importing them using the `!include` syntax. This is useful for sharing components across pages.

### Example:

```mml
!include [./header.mml]

(@header)
```

In this case, the `header.mml` file is imported, and the `header` component can be used anywhere in the file after the `!include` statement.

---

## Using Variables Inside Components

Variables defined within the same file where a component is called can be used inside components. You can define a variable and reference it within a component to make it dynamic.

### Example:

```mml
var.greeting = "Hello, World!"

!export.greeting_component
    (&text cl.[greeting]){:greeting:}.&text
!/export

(@greeting_component)
```

This allows you to pass dynamic content into your components. For more information on variables, [check the Variables page](./doc_vars.md).

---

## Case Sensitivity

Component names are **case-sensitive** in MML. This means that `!export.Header` and `!export.header` would be treated as different components.

### Example:

```mml
!export.Header
    (&text cl.[header]){Uppercase Header}.&text
!/export

!export.header
    (&text cl.[header]){Lowercase Header}.&text
!/export

(@Header)  !// Calls the uppercase header //!
(@header)  !// Calls the lowercase header //!
```

---

## Why Use Components?

Using components in every MML project offers several benefits:

- **Reusability**: Components allow you to avoid repeating the same code across multiple sections of a website. Instead of copying and pasting elements, you can simply define a component once and call it wherever needed.
  
- **Maintainability**: When you need to update a component, you only need to update it in one place, and the changes will reflect across all the places it's used.

- **Modularity**: Components make your code more organized by breaking down your project into smaller, manageable pieces. This is especially useful for larger websites or when working in teams.

- **Consistency**: Components ensure that the same design and structure are applied consistently throughout your website.

### Example of a Typical Use Case:

```mml
!export.footer
    (&ct cl.[footer]) {
        (&text){© 2024 My Website}.&text
    }.&ct
!/export

!export.header
    (&ct cl.[header]) {
        (&text){Welcome to My Website}.&text
    }.&ct
!/export

(&mml lang.[en]) {
    (&body) {
        (@header)
        (&text){This is the main content}.&text
        (@footer)
    }.&body
}.&mml
```

In this example, both the `header` and `footer` components are defined and used in the body of the document. These components could easily be reused across multiple pages by importing them.

---

[<- Back to Doc Navigation](./doc_nav.md)
<br>
[Next Page ->](./doc_using_components.md)