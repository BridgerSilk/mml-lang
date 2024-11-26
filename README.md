# MML (Modern Markup Language)

MML is a new modern markup language made for front-end web development, fully based on HTML and compiled with python. MML offers several new ways of making a website, as it introduces variables, re-usable components and external file import functionality. All valid HTML code is also valid MML code, as it is built on top of HTML.

---

## Comparing HTML with MML
### HTML:
- Basic HTML page:
    ```
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>test</title>
            <link rel="stylesheet" href="test.css">
        </head>
        <body>
            <p>Hello World!</p>
        </body>
    </html>
    ```
- Doesn't support html file imports
- Doesn't support re-usable components -> not efficient
- Doesn't support variables
- Bad readability
- Doesn't support dynamic syntax writing (different ways to write the syntax) -> not user friendly

### MML:
- Basic MML page:
    ```
    doc!.mml

    !// components.mml contains the public std_head component in this case, which is a basic <head> //!
    !include [./components.mml]

    var.title = "My Website"
    var.csslink = "./style.css"

    (&mml lang.[en]) {
        (@std_head) !// calling the component //!
        (&body) {
            (&text){Hello World!}.&text !// mml uses text instead of p //!
        }.&body
    }.&mml
    ```
- Supports MML file imports
- Supports re-usable components
- Supports variables with automatic data type conversion
- Good readability due to dynamic syntax
- Supports dynamic syntax writing (different ways to write the syntax)
- All valid HTML code is also valid MML code
- Very fast compilation even with huge MML pages and external imports

## Documentation

Want to learn more about how MML works and what you can do with it? <br>
Visit the [documentation page](./documentation/doc_nav.md)!