# Setting up a Project

This guide will walk you through the process of setting up an MML (Modern Markup Language) project. Follow these steps to organize your project structure and create your first `.mml` files.

---

## Folder Structure

It's recommended to use a clean and organized folder structure for your MML project. Here's an example:

```
my-mml-project/
├── components/
├── pages/
├── styles/
└── index.mml
```

- **components/**: This folder stores reusable components you can import across multiple pages.
- **pages/**: This folder is where you store individual page `.mml` files.
- **styles/**: Place your CSS files here.
- **index.mml**: This is your main entry file for the homepage.

---

## Creating Your First `.mml` Files

1. **Create the `index.mml` file:**

   In the root of your project, create a file called `index.mml`. This will serve as your homepage.

   ```mml
   doc!.mml
   (&mml lang.[en]) {
       (&head) {
           (&meta charset.[UTF-8])
           (&title){My First MML Page}.&title
       }.&head
       (&body) {
           (&text cl.[welcome-text]){Hello, MML World!}.&text
       }.&body
   }.&mml
   ```

2. **Create a reusable component:**

   Inside the `components/` folder, create a file called `navbar.mml`:

   ```mml
   !export.navbar
   (&nav) {
       (&a link.[./index.html]){Home}.&a
       (&a link.[./about.html]){About}.&a
   }.&nav
   !/export
   ```

3. **Use the component in `index.mml`:**

   Edit the `index.mml` file to include the reusable component:

   ```mml
   !include [./components/navbar.mml]

   doc!.mml
   (&mml lang.[en]) {
       (&head) {
           (&meta charset.[UTF-8])
           (&title){My First MML Page}.&title
       }.&head
       (&body) {
           !// Include the navbar component //!
           (@navbar)

           (&text cl.[welcome-text]){Hello, MML World!}.&text
       }.&body
   }.&mml
   ```

---

### Tips for a Clean MML Project

- **Folder Structure:** Keep components, pages, and styles in separate folders to maintain organization and readability.
- **Indentation:** Use consistent indentation to make your `.mml` files more readable.
- **Reusability:** Use components and variables to avoid code repetition across different pages.

---

[<- Back to Doc Navigation](./doc_nav.md)
<br>
[Next Page ->](./doc_syntax.md)