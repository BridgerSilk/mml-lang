# Example: Login Form

In this example, we will create a simple login form using MML. The form will include fields for a username and password, as well as a submit button. No additional CSS or JavaScript is used.

### MML Code for the Login Form:

```mml
doc!.mml
(&mml lang.[en]) {
    (&head) {
        (&title){Login Form}.&title
    }.&head
    (&body) {
        (&h1){Login}.&h1
        
        (&ct cl.[form-container]) {
            (&form) {
                (&label for.[username]){Username:}.&label
                (&input type.[text] id.[username] name.[username]).&input
                
                (&label for.[password]){Password:}.&label
                (&input type.[password] id.[password] name.[password]).&input
                
                (&button type.[submit]){Login}.&button
            }.&form
        }.&ct
    }.&body
}.&mml
```

### Explanation:

- **Document Type:** The document begins with `doc!.mml`, indicating it is an MML document.
  
- **Head Section:** The `(&head)` section contains the title of the page, displayed in the browser tab.

- **Body Section:**
  - A main heading is created using `(&h1){Login}`.
  - A container for the form is defined using `(&ct)` to keep the form elements organized.
  - The form itself is created using `(&form)`:
    - Labels are associated with input fields using `(&label)`.
    - Input fields for username and password are defined using `(&input)`, specifying their types and names.
    - A submit button is created using `(&button)`.

This simple login form can be easily expanded or modified as needed.

---

[<- Back to Doc Navigation](./doc_nav.md)
<br>
[Next Page ->](./ex_empty_page.md)