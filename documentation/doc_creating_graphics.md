# Creating Graphics

In MML (Modern Markup Language), you can create graphics using the `<canvas>` and `<svg>` elements just like in HTML, but with the MML syntax. This allows you to leverage MML's features while working with graphics.

---

## Using the Canvas Element

The `<canvas>` element in MML allows you to define a drawing area on your webpage. However, without JavaScript, you won't be able to dynamically draw on the canvas, but you can still include it as part of your layout.

### Example of a Canvas Element:

```mml
(&mml lang.[en]) {
    (&body) {
        (&h2){Drawing on Canvas}.&h2
        
        (&ct id.[myCanvas] style.[border:1px solid #000; width:300px; height:200px;]) {
            (&canvas width.[300] height.[200]).&canvas
        }.&ct
    }.&body
}.&mml
```

In this example, a canvas area is defined, but since no scripts are used, nothing will be drawn on it.

---

## Using SVG Elements

SVG (Scalable Vector Graphics) can be defined directly within MML using the MML syntax. SVG allows for the creation of shapes and images.

### Example of SVG Elements:

```mml
(&mml lang.[en]) {
    (&body) {
        (&h2){Creating SVG Graphics}.&h2
        
        (&svg width.[200] height.[200]) {
            (&circle cx.[100] cy.[100] r.[80] fill.[green]).&circle
            (&rect x.[20] y.[20] width.[150] height.[100] fill.[blue]).&rect
        }.&svg
    }.&body
}.&mml
```

In this example, a green circle and a blue rectangle are created using SVG elements, all defined using MML syntax.

---

## Important Considerations

- **Canvas Limitations:** Without JavaScript, the canvas will not display any drawings or graphics. It can serve as a placeholder or layout element.

- **Styling:** You can apply CSS styles to canvas and SVG elements using the MML shorthand for attributes.

- **Compatibility:** Ensure that your graphics render correctly across different browsers, as rendering may vary slightly.

---

By utilizing both Canvas and SVG in MML, you can set up a framework for graphics and enhance your web pages visually, even if dynamic drawing is not possible without scripts.

---

[<- Back to Doc Navigation](./doc_nav.md)
<br>
[Next Page ->](./ex_login_form.md)