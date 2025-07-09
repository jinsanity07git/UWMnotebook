# Jupyter Notebook Parser

A Python utility to parse Jupyter notebooks and extract content into structured formats (Markdown table and DOCX).

## Features

- **Parse Jupyter notebooks**: Extract all cell content with metadata
- **3-column table format**: Order, Content, Comment
- **Multiple export formats**: Markdown table and DOCX document
- **Cell type detection**: Identifies code, markdown, and raw cells
- **Metadata extraction**: Includes execution counts, tags, and output types
- **Summary statistics**: Cell counts, types, and content analysis

## Installation

### Core functionality (no additional dependencies)
The parser works with Python's standard library for basic functionality.

### Optional dependencies for enhanced features
```bash
pip install python-docx nbformat
```

## Usage

### Basic Usage

```python
from nbparser import NotebookParser

# Initialize parser with notebook path
parser = NotebookParser("path/to/your/notebook.ipynb")

# Parse all cells
cells = parser.parse_notebook()

# Parse only markdown cells
markdown_cells = parser.parse_notebook(cell_type_filter='markdown')

# Parse only code cells
code_cells = parser.parse_notebook(cell_type_filter='code')

# Generate markdown table (all cells)
markdown_content = parser.to_markdown_table("output.md")

# Generate markdown table (markdown cells only)
markdown_only = parser.to_markdown_table("markdown_only.md", cell_type_filter='markdown')

# Generate DOCX file (requires python-docx)
parser.to_docx("output.docx")

# Generate DOCX file (markdown cells only)
parser.to_docx("markdown_only.docx", cell_type_filter='markdown')

# Convenience method for markdown-only export
parser.export_markdown_only("markdown_export.md", "markdown_export.docx")

# Get summary statistics
summary = parser.get_summary()
print(f"Total cells: {summary['total_cells']}")
print(f"Cell types: {summary['cell_types']}")

# Get summary for markdown cells only
md_summary = parser.get_summary(cell_type_filter='markdown')
print(f"Markdown cells: {md_summary['total_cells']}")
```

### Command Line Usage

Run the main script:
```bash
python nbparser.py
```

Or test with the test script:
```bash
python test_nbparser.py
```

## Output Format

### 3-Column Table Structure

| Column | Description | Example |
|--------|-------------|---------|
| Order | Sequential cell number | 1, 2, 3, ... |
| Content | Cell source code or markdown | `print("Hello")` or `# Title` |
| Comment | Cell metadata and type info | `Cell type: code; Execution count: 1` |

### Comment Field Details

The comment field includes:
- **Cell type**: code, markdown, or raw
- **Execution count**: For code cells that have been executed
- **Tags**: Any tags assigned to the cell
- **Output types**: Types of outputs generated (stream, display_data, etc.)

## File Structure

```
utility/
├── nbparser.py           # Main parser implementation
├── test_nbparser.py      # Test script with sample notebook
├── requirements.txt      # Optional dependencies
└── README_nbparser.md    # This documentation
```

## Classes and Methods

### `NotebookParser`

Main class for parsing Jupyter notebooks.

#### Methods

- `__init__(notebook_path: str)`: Initialize with notebook file path
- `parse_notebook(cell_type_filter: str = None) -> List[CellData]`: Parse notebook and return cell data
  - `cell_type_filter`: Optional filter ('code', 'markdown', 'raw')
- `to_markdown_table(output_path: str = None, cell_type_filter: str = None) -> str`: Generate markdown table
  - `cell_type_filter`: Optional filter for cell types
- `to_docx(output_path: str, cell_type_filter: str = None) -> None`: Generate DOCX file
  - `cell_type_filter`: Optional filter for cell types
- `get_summary(cell_type_filter: str = None) -> Dict[str, Any]`: Get notebook statistics
  - `cell_type_filter`: Optional filter for cell types
- `export_markdown_only(markdown_output_path: str = None, docx_output_path: str = None) -> str`: Convenience method for markdown-only export

### `CellData`

Data structure for cell information.

#### Attributes

- `order: int`: Cell order number
- `content: str`: Cell source content
- `comment: str`: Cell metadata and comments

## Example Output

### Markdown Table
```markdown
# Jupyter Notebook Content

| Order | Content | Comment |
|-------|---------|---------|
| 1 | import sys<br>sys.path.insert(0, f'{sys.path[0].split("course-content")[0]}/example-package') | Cell type: code; Execution count: 1 |
| 2 | # 估计模型参数 | Cell type: markdown |
| 3 | 假设我们有一些汽车(car)或公交车(bus)的行程观察数据... | Cell type: markdown |
```

### Summary Statistics

**All cells:**
```
Total cells: 129
Cell types: {'code': 65, 'markdown': 64}
Total characters: 22678
Average cell length: 175.8 characters
```

**Markdown cells only:**
```
Total cells: 64
Cell types: {'markdown': 64}
Total characters: 11234
Average cell length: 175.5 characters
```

## Error Handling

The parser includes comprehensive error handling for:
- Missing notebook files
- Invalid JSON format
- Missing dependencies (graceful degradation)
- Empty or malformed cells

## Configuration

### Default Settings

- **Notebook path**: Set in `nburl` variable
- **Content truncation**: Long content truncated at 200 characters for table display
- **Encoding**: UTF-8 for all file operations
- **Cell filtering**: No filter by default (includes all cell types)

### Cell Type Filtering

The parser supports filtering by cell type:
- `'code'`: Include only code cells
- `'markdown'`: Include only markdown cells
- `'raw'`: Include only raw cells
- `None` (default): Include all cell types

**Example usage:**
```python
# Export only markdown cells
parser = NotebookParser("notebook.ipynb")
parser.export_markdown_only("markdown_content.md", "markdown_content.docx")

# Or use the filter parameter directly
markdown_cells = parser.parse_notebook(cell_type_filter='markdown')
parser.to_markdown_table("markdown_table.md")
```

### Customization

You can modify the parser behavior by:
- Changing the content truncation limit in `to_markdown_table()`
- Adjusting column widths in `to_docx()`
- Modifying comment extraction logic in `_extract_comment()`

## Testing

The package includes a comprehensive test suite:

```bash
python test_nbparser.py
```

This will:
1. Test with the original notebook (if available)
2. Create a sample notebook for testing
3. Verify all functionality
4. Generate sample output files

## Troubleshooting

### Common Issues

1. **FileNotFoundError**: Check notebook path is correct
2. **JSONDecodeError**: Ensure notebook file is valid JSON
3. **ImportError for DOCX**: Install `python-docx` package
4. **Encoding issues**: Ensure notebook uses UTF-8 encoding

### Performance Notes

- Large notebooks (>1000 cells) may take longer to process
- DOCX generation is slower than markdown for large notebooks
- Memory usage scales with notebook size

## License

This utility is part of the UWMnotebook project.