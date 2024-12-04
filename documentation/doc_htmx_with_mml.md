# Using htmx with MML

This page with explain how you can use [htmx](https://htmx.org/) within MML. Htmx is a lightweight JavaScript library that allows you to add interactive and dynamic behavior to your web application by using HTML attributes instead of writing complex JavaScript. It leverages HTML to define behaviors like making AJAX requests, updating parts of a page, and handling events.

---

## Inlcuding htmx in your Project

This is how you can include htmx in your MML code:

```mml
(&js src.[https://unpkg.com/htmx.org]){}.&js
```
Add this line either in the head or body of your MML code.

[Here](https://htmx.org/docs/#installing) you can find other ways of including htmx in your project.

---

## htmx Attributes

Making a GET request to a URL:

```mml
(&btn hx-get.[/example]) { Example } .&btn
(&btn hx-post.[/example]) { Example } .&btn
(&btn hx-put.[/example]) { Example } .&btn
(&btn hx-delete.[/example]) { Example } .&btn
(&btn hx-target.[#targetid]) { Example } .&btn
(&btn hx-swap.[beforeend]) { Example } .&btn
```

These are commonly used attributes in htmx. To learn what they do visit the [htmx documentation](https://htmx.org/docs/#ajax).

### Example:

Load content from a URL into a target element:

```mml
(&btn hx-get.[/example] hx-target.[#result]) {Load Content} .&btn
(&ct id.[result]){}.&ct
```

When the button is clicked, a GET request is made to ``/example``, and the response is inserted into ``(&ct id.[result]){}.&ct``.

---

## More Examples

### Submitting a Form:

```mml
(&form hx-post.[/submit] hx-target.[#result]){
    (&in type.[text] name.[name] placeholder.[Your Name])
    (&btn type.[submit]) { Submit } .&btn
}.&form

(&ct id.[result]){}.&ct
```
### Swapping Content:

Control how content is replaced in the target using ``hx-swap``:
- ``outerHTML``: Replace the entire element.
- ``innerHTML``: Replace the content inside the element.
- ``beforeend``: Insert content at the end of the target.

```mml
(&btn hx-get.[/more] hx-target.[#result] hx-swap.[beforeend]) { Load More } .&btn

(&ct id.[result]){}.&ct
```

This appends the content from /more to the end of #result.

---

[<- Back to Doc Navigation](./doc_nav.md)
<br>
[Next Page ->](./doc_comments.md)