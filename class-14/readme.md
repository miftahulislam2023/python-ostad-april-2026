# Class 14

## Today's Topic
- Tuples
  - immutable
  - usage
  - unpacking

Here is the properly formatted Markdown table comparing Lists and Tuples, expanded with the key technical differences to give you a complete overview.

| Feature         | List                                                  | Tuple                                            |
| --------------- | ----------------------------------------------------- | ------------------------------------------------ |
| **Syntax**      | `[element1, element2]`                                | `(element1, element2)`                           |
| **Mutability**  | **Mutable** (can be changed after creation)           | **Immutable** (cannot be changed after creation) |
| **Performance** | Slower (requires more memory overhead)                | Faster (more memory efficient)                   |
| **Size**        | Dynamic (can grow or shrink)                          | Fixed                                            |
| **Methods**     | Built-in methods like `append()`, `insert()`, `remove()` | Only has `count()` and `index()`                 |
| **Use Case**    | Used for collections of data that will change         | Used for write-protected, constant data          |

---

### Key Takeaway

> **Rule of thumb:** Use a **list** when you have a collection of items that you expect to modify, sort, or append to later. Use a **tuple** when the data should remain a constant, read-only sequence throughout your program.

## Mutability - পরিবর্তনযোগ্যতা
- Mutable -> যা পরিবর্তন করা যায়
- Immutable -> যা পরিবর্তন করা যায় না