# Maps (Experimental)

MML (Modern Markup Language) also supports the use of maps to make your variables more dynamic and improve the structure of your code. This guide covers how to define, use, and manipulate maps in MML.

---

<p style="color:orange;"><b>NOTE:</b> Maps are still in development and might cause problems. Please report any bugs!</p>

---

## Defining Maps

Maps in MML are defined using the following syntax:

```mml
map.map_name {
    key1 = value
    key2 = value
}
```

Unlike in many other languages, maps in MML don't require commas to separate keys.

### Example:

```mml
map.user {
    name = "TestUser"
    id = 123
}

!// access and display data from the map //!
(&text) { Username :user.name: } .&text
```

In this example a map with the name `user` is initialized with 2 items, `name` and `id`. The `name` item is then accessed using :user.name: and displayed in a `&text` element.

---

<p style="color:orange;"><b>NOTE:</b> Mathematical operations and manipulation of Map Items are not supported yet. WIP</p>

---

## Accessing Map Items

Once defined, map items can be accessed inside any MML element by wrapping the map name along with the item key in `:mapname.key:`.

### Example:

```mml
map.user {
    name = "TestUser"
    id = 123
}

!// access and display an item from the map //!
(&text) { Username :user.name: } .&text
```

This will output:

```html
<p>Username TestUser</p>
```

### Accessing Map Items inside of Components

Map items can be accessed inside reusable components if the map is initialized in the same file where the component is called. However, maps cannot be initialized directly inside a component itself.

### Example:

```mml
$export.example
(&text){:mymap.mykey:}.&text
$/export

!// Call the component and display the item //!
(@example)
```

In this example, the `mykey` item key of the map `mymap` can be used within the `example` component because it's initialized before the component is called.

---

## Case Sensitivity

MML map names and item keys are **case-sensitive**. This means that `map.myMap` and `map.mymap` are considered two different maps.

```mml
map.myMap {}
map.mymap {}
```

---

<p style="color:orange;"><b>NOTE:</b> All variable rules are also valid rules for maps and map items!</p>

---

## Mathematical Expressions & Map Manipulation

Not yet supported, but it is being developed. Be patient.

---

Using maps is a great way to maintain and work with many variables, as they make your code more structured and readable.

---

[<- Back to Doc Navigation](./doc_nav.md)
<br>
[Next Page ->](./doc_comments.md)