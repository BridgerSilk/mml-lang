# Variables

MML (Modern Markup Language) supports the use of variables to make your code more dynamic and reusable. This guide covers how to define, use, and manipulate variables in MML.

---

## Defining Variables

Variables in MML are defined using the following syntax:

```mml
var.var_name = value
```

### Example:

```mml
var.greeting = "Hello, world!"
var.number = 42
var.pi = 3.14
```

In this example, the variables `greeting`, `number`, and `pi` are defined as a string, integer, and float, respectively.

---

## Using Variables

Once defined, variables can be used inside any MML element by wrapping the variable name in `:variable_name:`.

### Example:

```mml
(&text){:greeting:}.&text
```

This will output:

```html
<p>Hello, world!</p>
```

### Using Variables Inside Components

Variables can be used inside reusable components if the variable is defined in the same file where the component is called. However, variables cannot be defined directly inside a component itself.

### Example:

```mml
!export.example
(&text){:greeting:}.&text
!/export

!// Call the component and use the variable //!
(@example)
```

In this example, the `greeting` variable can be used within the `example` component because it's defined before the component is called.

---

## Case Sensitivity

MML variables are **case-sensitive**. This means that `var.myVar` and `var.myvar` are considered two different variables.

```mml
var.myVar = "This is MyVar"
var.myvar = "This is myvar"
```

---

## Supported Data Types

MML supports the following data types for variables:

- **String**: Enclosed in double quotes.
  ```mml
  var.message = "Hello, world!"
  ```

- **Integer**: Whole numbers.
  ```mml
  var.age = 25
  ```

- **Float**: Decimal numbers.
  ```mml
  var.pi = 3.14
  ```

---

## Mathematical Expressions

MML supports simple mathematical expressions with variables. You can use addition, subtraction, multiplication, and division.

### Example:

```mml
var.result = 5 + 2 * 3
```

You can then display the result of the expression:

```mml
(&text){:result:}.&text
```

This will output:

```html
<p>11</p>
```

---

## Example Combining Variables and Components

```mml
var.title = "Welcome"
var.year = 2024

!export.header
(&text cl.[header]){:title:}.&text
!/export

!// Call the header component //!
(@header)

(&text cl.[footer]){Current Year: :year:}.&text
```

This example defines two variables (`title` and `year`) and uses them inside both a reusable component (`header`) and directly in the page.

---

Understanding how to define and use variables will help make your MML code more dynamic and easier to maintain.

---

[<- Back to Doc Navigation](./doc_nav.md)
<br>
[Next Page ->](./doc_maps.md)