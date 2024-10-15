# Nesting HTML Code

In MML (Modern Markup Language), all valid HTML code is also valid MML code. This feature allows you to seamlessly integrate standard HTML elements and structures directly into your MML files, providing flexibility and familiarity for users transitioning from HTML to MML.

---

## Using HTML Code in MML

You can nest HTML code within your MML files, either as single lines or as multiple lines of HTML. This allows you to take advantage of existing HTML structures and elements while leveraging the features and enhancements provided by MML.

### Single Line HTML Example:

You can include simple HTML elements directly within your MML file:

```mml
(&mml lang.[en]) {
    (&body) {
        (&h1){Welcome to My MML Page}.&h1
        <p>This is a paragraph written in standard HTML.</p>
    }.&body
}.&mml
```

### Multiple Lines HTML Example:

You can also include more complex HTML structures that span multiple lines:

```mml
(&mml lang.[en]) {
    (&body) {
        (&h2){About Us}.&h2
        <div>
            <p>This is a paragraph inside a div.</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
    }.&body
}.&mml
```

### Mixing HTML and MML

You can mix MML and HTML code freely, allowing you to take advantage of MML's features (like shorthand syntax and components) while still using standard HTML when necessary:

```mml
(&mml lang.[en]) {
    (&head) {
        (&title){My Mixed Page}.&title
    }.&head
    (&body) {
        (&h1){Welcome to My Mixed Page}.&h1
        <p>This page uses both MML and HTML elements.</p>
        
        (&ct) {
            (&text){This is a paragraph created with MML.}.&text
        }.&ct
    }.&body
}.&mml
```

---

## Important Considerations

- **Validation:** While nesting HTML is allowed, ensure that your HTML code is valid and well-formed to avoid unexpected behavior in the rendered output.
- **MML Features:** Remember that MML features (like variables and components) cannot be used directly inside HTML tags. Use MML constructs outside the HTML code or integrate them creatively.
- **Styling and Scripts:** For including styles or scripts, use the MML syntax `(&style)` or `(&script)` instead of HTML `<link>` or `<script>` tags.

---

By allowing HTML code to be nested within MML files, you can create rich, dynamic web pages while enjoying the enhancements and ease of use that MML offers.

---

[<- Back to Doc Navigation](./doc_nav.md)
<br>
[Next Page ->](./doc_creating_graphics.md)