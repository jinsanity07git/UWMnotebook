


## Everything

Q: 
* To search for all Markdown files (typically having the .md extension) recursively in a directory using "Everything," a desktop search utility for Windows that can instantly locate files and folders by name,

A: 

1. **Specify the Directory:** To search within a specific directory, you'll need to use the path of the directory as part of your search query. For your example directory (`J:\My Drive`), you would start your query with the path, ensuring to use double quotes if your path contains spaces.
2. **Use Wildcards for Recursive Search:** To find all Markdown files recursively, use a wildcard pattern that matches `.md` files.
3. **Combine Path and Pattern:** Your search query in Everything should look like this:

```bash
"J:\My Drive" *.md
```

---

Q:
 search for a path that contains a specific keyword, such as "github"

A:
1. Modifiers: Functions and regular search terms can be prefixed with a modifier.

2. | `childcount:<count>`           | Search for folders that contain the specified number of subfolders and files. |
   | ------------------------------ | ------------------------------------------------------------ |
   | `folder:folders:nofolderonly:` | Match folders only.                                          |
```bash
count:5 path: github\tdm23 
```



## References

[^1]: [everything search Syntax](https://www.voidtools.com/support/everything/searching/)

