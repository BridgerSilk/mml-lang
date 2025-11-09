# Variables

MML (Modern Markup Language) supports variables to make your code dynamic, flexible, and reusable. Variables can be either **static** or **dynamic**, with strict or flexible typing rules. This guide explains how to define, use, and manage variables in MML.

---

## Defining Variables

Variables are declared using either the `static` or `dynamic` keyword.

```mml
static <type> <name> = <value>
dynamic <name> = <value>
```

* **Static variables** have a fixed data type and cannot change to another type after declaration.
* **Dynamic variables** can hold any type and change type during runtime.

### Examples

```mml
static str greeting = "Hello, world!"
static i32 count = 42
dynamic value = True
```

In this example:

* `greeting` is a static string.
* `count` is a static 32-bit integer.
* `value` is a dynamic variable, starting as a boolean.

> 💡 See the [Data Types page](./doc_data_types.md) for a full list of supported types.

---

## Using Variables in Elements

Variables are referenced in elements using the `:variable_name:` syntax.

```mml
(&text){:greeting:}.&text
```

Output:

```html
<p>Hello, world!</p>
```

---

## Using Variables Inside Components

You can use variables inside components as long as the variable is defined before the component call.

```mml
$export.message
(&text){:greeting:}.&text
$/export

(@message)
```

---

## Checking Variable Types

You can check the type of a variable or value using the `?type` method.

### Examples

```mml
greeting?type
65?type
```

Outputs:

```
str
i32
```

---

## Type Casting

MML supports type casting using the `(<value> -> <type>)` syntax.

### Examples

```mml
(myvar -> str)
(25 -> float)
```

If a cast is invalid (e.g., `str` → `i32`), it is **ignored silently** without throwing an error.

---

## UUID Generation

UUIDs can be generated directly using the `new` keyword.

### Example

```mml
static uuid id1 = new uuid1
static uuid id4 = new uuid4
```

Supported UUID types: `1`, `3`, `4`, `5`.

---

## Case Sensitivity

Variable names in MML are **case-sensitive**.

```mml
static str MyVar = "Hello"
static str myvar = "World"
```

These are **two separate variables**.

---

## Example Combining Variables, Casting, and Components

```mml
static str title = "Welcome"
dynamic value = 25
value = (value -> float)

$export.header
(&text cl.[header]){:title:}.&text
$/export

(@header)
(&text cl.[footer]){Value Type: :value?type:}.&text
```

Output:

```html
<p class="header">Welcome</p>
<p class="footer">Value Type: float</p>
```

---

[<- Back to Doc Navigation](./doc_nav.md) <br>
[Next Page ->](./data_types.md)