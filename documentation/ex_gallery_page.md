# Example: Gallery Page

In this example, we will create a simple gallery page using MML. This page will display a collection of images arranged in a grid format.

### MML Code for the Gallery Page:

```mml
doc!.mml
(&mml lang.[en]) {
    (&head) {
        (&title){Gallery Page}.&title
        (&link rel.[stylesheet] link.[styles.css]) // Link to an optional external stylesheet
    }.&head
    (&body) {
        (&h1){Image Gallery}.&h1
        
        (&ct cl.[gallery-container]) {
            (&img src.[./image1.jpg] alt.[Image 1]).&img
            (&img src.[./image2.jpg] alt.[Image 2]).&img
            (&img src.[./image3.jpg] alt.[Image 3]).&img
            (&img src.[./image4.jpg] alt.[Image 4]).&img
            (&img src.[./image5.jpg] alt.[Image 5]).&img
        }.&ct
    }.&body
}.&mml
```

### Explanation:

- **Document Type:** The document begins with `doc!.mml`, indicating it is an MML document.
  
- **Head Section:** The `(&head)` section contains the title of the page, displayed in the browser tab, and optionally links to an external stylesheet for styling the gallery.

- **Body Section:** 
  - A main heading is created using `(&h1){Image Gallery}`.
  - A container for the gallery is defined using `(&ct cl.[gallery-container])`. This container can be styled using CSS to arrange the images in a grid format.
  - Multiple images are added using `(&img)` with the `src` attribute pointing to the image files and the `alt` attribute providing alternative text for accessibility.

This gallery page can be expanded by adding more images or integrating features like a lightbox for viewing larger versions of the images.

---

[<- Back to Doc Navigation](./doc_nav.md)
<br>
[Next Page ->](./ex_embedded_video.md)