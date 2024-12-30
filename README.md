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

```bash
pip install codescribe
```

Or clone and install from source:

```bash
git clone https://github.com/Stay03/codescribe.git
cd codescribe
pip install -e .
```

## Usage

### Basic Usage

```python
from codescribe import CodebaseExtractor

extractor = CodebaseExtractor(
    base_directory="./your/project/path",
    output_file="codebase_snapshot.md"
)
extractor.extract()
```

### With Custom Configuration

Create a config file `codebase_config.json`:

```json
{
    "ignore_patterns": ["env", "venv", ".git"],
    "ignore_extensions": [".log", ".tmp"],
    "list_only_extensions": [".png", ".jpg"],
    "max_file_size_mb": 10
}
```

Then use it in your code:

```python
extractor = CodebaseExtractor(
    base_directory="./your/project/path",
    output_file="codebase_snapshot.md",
    config_file="codebase_config.json"
)
extractor.extract()
```

## Configuration Options

- `ignore_patterns`: List of file/directory names to ignore
- `ignore_extensions`: List of file extensions to ignore
- `list_only_extensions`: List of file extensions to list without content
- `max_file_size_mb`: Maximum file size to process in MB