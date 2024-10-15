# Example: Empty Page

In this example, we will create a simple empty page using MML. This page contains only the skeleton structure without any content.

### MML Code for the Empty Page:

```mml
doc!.mml
(&mml lang.[en]) {
    (&head) {
        (&title){Empty Page}.&title
    }.&head
    (&body) {
        !// This page is intentionally left blank //! 
    }.&body
}.&mml
```

### Explanation:

- **Document Type:** The document begins with `doc!.mml`, indicating it is an MML document.
  
- **Head Section:** The `(&head)` section contains the title of the page, which will be displayed in the browser tab.

- **Body Section:** 
  - The `(&body)` section is present, but it intentionally contains no content. A comment is included using `!// This page is intentionally left blank //!` to clarify that the body is empty.

This skeleton serves as a foundation for adding content, styles, or components as needed in your project.

---

[<- Back to Doc Navigation](./doc_nav.md)
<br>
[Next Page ->](./ex_gallery_page.md)