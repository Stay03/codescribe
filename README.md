# CodeScribe

A powerful tool for extracting and documenting codebases for LLM analysis.

## Features

- Extracts code from your entire codebase into a single, well-formatted document
- Configurable ignore patterns for files and directories
- Handles binary files appropriately
- Generates markdown output with proper syntax highlighting
- Includes metadata and file structure
- Customizable via JSON configuration

## Installation

Clone and install from source:

```bash
git clone https://github.com/Stay03/codescribe.git

```

## Usage

### Basic Usage

```bash
python codescribe/run.py
```

This will automatically create a `codebase_snapshot.md` file in your project directory containing all your codebase's documentation.

You can also use it programmatically in your code:

```python
from src import CodebaseExtractor

extractor = CodebaseExtractor(
    base_directory="./",
    output_file="./codebase_snapshot.md",
    config_file="codescribe/codebase_config.json"
)
extractor.extract()

```

## Default Configuration File

```json
{
    "ignore_patterns": ["codescribe", "env", "venv", ".git", "codebase_snapshot.md"],
    "ignore_extensions": [".log", ".tmp", ".gitignore"],
    "list_only_extensions": [".png",".jpg",".jpeg",".gif",".ico",".svg",".db",".sqlite",".pdf",".zip"],
    "max_file_size_mb": 5
}
```


## Configuration Options

- `ignore_patterns`: List of file/directory names to ignore
- `ignore_extensions`: List of file extensions to ignore
- `list_only_extensions`: List of file extensions to list without extracting its content
- `max_file_size_mb`: Maximum file size to process in MB