# Example: Embedded Video

In this example, we will create a simple page that embeds a video using MML. The video will be displayed using the HTML `<video>` element in the MML syntax.

### MML Code for the Embedded Video:

```mml
doc!.mml
(&mml lang.[en]) {
    (&head) {
        (&title){Embedded Video}.&title
    }.&head
    (&body) {
        (&h1){Watch Our Video}.&h1

        (&video controls cl.[video-player]) {
            (&source src.[./video.mp4] type.[video/mp4]).&source
            (&source src.[./video.webm] type.[video/webm]).&source
            Your browser does not support the video tag.
        }.&video
    }.&body
}.&mml
```

### Explanation:

- **Document Type:** The document begins with `doc!.mml`, indicating it is an MML document.

- **Head Section:** The `(&head)` section contains the title of the page, displayed in the browser tab.

- **Body Section:** 
  - A main heading is created using `(&h1){Watch Our Video}` to introduce the video content.
  - The `(&video controls cl.[video-player])` element embeds the video player on the page, with the `controls` attribute allowing users to play, pause, and adjust the volume.
  - Inside the video element, multiple `(&source)` elements specify the video files available for playback. The `src` attribute points to the video files (in both MP4 and WebM formats), and the `type` attribute indicates the file format.
  - A fallback message is included for browsers that do not support the `<video>` element: `Your browser does not support the video tag.`

This setup allows users to view a video directly on the page, enhancing the interactivity and engagement of your content.

---

[<- Back to Doc Navigation](./doc_nav.md)