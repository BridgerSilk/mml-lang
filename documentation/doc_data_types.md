# Data Types

MML supports multiple data types with automatic recognition and explicit declaration for static variables. This page covers all available types, example values, type checking, casting, and instance creation.

---

## Supported Data Types

| Type       | Example Value             | Description                   |
| ---------- | ------------------------- | ----------------------------- |
| `str`      | `"hello"`                 | String text                   |
| `i32`      | `42`                      | 32-bit integer                |
| `float`    | `3.14`                    | Floating-point number         |
| `list`     | `[1, 2, 3]`               | Ordered list                  |
| `bool`     | `True` / `False`          | Boolean value                 |
| `nonetype` | *(automatic only)*        | Represents no value           |
| `complex`  | `4+5j`                    | Complex number                |
| `vec2i`    | `v[10, 20]`               | 2D integer vector             |
| `vec3i`    | `v[1, 2, 3]`              | 3D integer vector             |
| `vecf`     | `v[5.2, 1.4]`             | Floating-point vector         |
| `uuid`     | `uuid["0123-53165-3211"]` | Universally unique identifier |
| `bit`      | `0` / `1`                 | Single-bit value              |
| `char`     | `"A"`                     | Single character              |
| `color`    | `c["red"]`                | Color value                   |

---

## Type Checking

You can check the type of any variable or literal using the `?type` method.

```mml
myvar?type
3.14?type
```

Output:

```
str
float
```

---

## Type Casting

Type casting allows you to convert a variable or value to another type:

```mml
(<value> -> <type>)
```

### Examples

```mml
(25 -> str)       !// returns "25" //!
("45" -> i32)     !// returns 45 //!
(3.5 -> i32)      !// returns 3 //!
```

Invalid casts (like `"abc" -> i32`) are **ignored silently**.

---

## Creating New Instances

Some types support instance creation using the `new` keyword.

### Example: UUIDs

```mml
static uuid id1 = new uuid1
static uuid id4 = new uuid4
```

Available UUID versions: **1**, **3**, **4**, **5**.

Future releases will expand `new` to support other instance types.

---

[<- Back to Variables](./variables.md) <br>
[Next Page ->](./doc_importing.md)