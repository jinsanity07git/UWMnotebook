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

