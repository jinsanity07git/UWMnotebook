cheatsheet 



### JavaScript

To search for `console.log` statements in Visual Studio Code while excluding lines that are commented out, you can use the following regular expression in the search:

```bash
^(?![ \t]*\/\/).*console\.log
```

Here's a breakdown of the regex:

- `^` asserts the start of a line.
- `(?![ \t]*\/\/)` is a **negative lookahead** that asserts the line does not start with zero or more spaces or tabs `[ \t]*` followed by `//`. This part is crucial for excluding lines that start with comments.
- `.*console\.log` matches any characters (except for line terminators) followed by `console.log`. The `.` is escaped as `\.` to match the literal dot character.

#### `.*`

- `.` (dot) is a special character in regular expressions that matches any single character except for newline characters. It's one of the most commonly used metacharacters in regex because of its broad matching capability.
- `*` (asterisk) is a quantifier in regular expressions that matches zero or more occurrences of the preceding element. When used after the dot, `.*` essentially matches any sequence of characters (including no characters at all), up to the newline character or the end of the string if it's a single-line search.

When you combine `.*` with `console.log`, the expression can be broken down as follows:

- `.*` will match any sequence of characters at the beginning of a string or line. This allows the regex to match `console.log` regardless of what precedes it on the same line, except for the scenarios explicitly excluded by the rest of the regex pattern. It's a way of saying, "Match `console.log` no matter what characters come before it."



### Python 

```bash
^(?![ \t]*#).*print
```

Here's a breakdown of the regex:



### negative lookahead



The logic of `(?!_)` in a regular expression is part of what's called a "negative lookahead". Let's break down its components:

- **`(  )`**: Parentheses are used in regular expressions to group parts of the pattern. In the context of lookaheads, they don't capture the text inside for later use (like a capturing group would) but are rather used to apply the lookahead logic as a single unit.
- **`?!`**: This is the specific syntax that defines a negative lookahead. The `?` at the beginning indicates that it's a **lookahead** (a type of zero-width assertion), and the `!` specifies that it's negative. A lookahead itself doesn't consume any characters on the string; it just looks ahead to see if a certain pattern does or does not match. If the pattern does match, the lookahead is considered unsuccessful (in the case of a negative lookahead).
- **`_`**: This is the specific pattern the lookahead is checking for. In this case, it's looking ahead to see if an underscore `_` is present.

Putting it all together, `(?!_)` looks ahead in the string **from the current position to check if the next character is not** an underscore. If the next character is an underscore, the lookahead condition fails, and the match (for the whole pattern it's part of) is not successful at that position in the string. If the next character is anything other than an underscore, the lookahead condition succeeds, but it doesn't consume any characters — the regex engine's "cursor" remains where it was, ready to continue matching the rest of the pattern.

So, in the context of `lgrps(?!_)`, the expression will match any occurrence of "lgrps" that is not immediately followed by an underscore, because the negative lookahead ensures that the match fails if "lgrps" is directly followed by `_`.
