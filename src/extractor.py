import os
import datetime
from typing import List, Optional, Dict
import json

class CodebaseExtractor:
    """A tool for extracting and documenting code from a codebase."""
    
    def __init__(self, 
                 base_directory: str,
                 output_file: str = 'codebase_snapshot.md',
                 config_file: Optional[str] = None):
        self.base_directory = os.path.abspath(base_directory)
        self.output_file = output_file
        self.config = self._load_config(config_file) if config_file else self._default_config()
        
    def _default_config(self) -> Dict:
        return {
            "ignore_patterns": [
                'env', 'venv', '.git', '__pycache__', 
                'node_modules', 'build', 'dist', '.idea', 'app.py', 'codebase_snapshot.md'
            ],
            "ignore_extensions": [
                '.log', '.tmp', '.bak', '.pyc', '.pyo', 
                '.pyd', '.so', '.dll', '.dylib'
            ],
            "list_only_extensions": [
                '.png', '.jpg', '.jpeg', '.gif', '.ico', 
                '.svg', '.db', '.sqlite', '.pdf', '.zip'
            ],
            "max_file_size_mb": 10
        }
    
    def _load_config(self, config_file: str) -> Dict:
        """Load configuration from a JSON file."""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config file: {e}. Using default config.")
            return self._default_config()
    
    def _should_skip_file(self, filepath: str) -> bool:
        """Determine if a file should be skipped based on configuration."""
        filename = os.path.basename(filepath)
        
        # Check file size
        try:
            if os.path.getsize(filepath) > self.config['max_file_size_mb'] * 1024 * 1024:
                return True
        except OSError:
            return True
            
        # Check patterns and extensions
        return (any(pattern in filepath for pattern in self.config['ignore_patterns']) or
                any(filename.endswith(ext) for ext in self.config['ignore_extensions']))
    
    def _is_list_only(self, filename: str) -> bool:
        """Check if file should only be listed without content extraction."""
        return any(filename.endswith(ext) for ext in self.config['list_only_extensions'])
    
    def extract(self, add_metadata: bool = True) -> None:
        """Extract and document the codebase."""
        try:
            with open(self.output_file, 'w', encoding='utf-8', errors='ignore') as output:
                if add_metadata:
                    self._write_metadata(output)
                
                for root, dirs, files in os.walk(self.base_directory):
                    # Skip ignored directories
                    dirs[:] = [d for d in dirs if not any(
                        pattern in d for pattern in self.config['ignore_patterns']
                    )]
                    
                    for filename in sorted(files):
                        filepath = os.path.join(root, filename)
                        if self._should_skip_file(filepath):
                            continue
                            
                        relative_path = os.path.relpath(filepath, self.base_directory)
                        self._process_file(relative_path, filepath, output)
                        
            print(f"✓ Codebase documentation generated: {self.output_file}")
            
        except Exception as e:
            print(f"❌ Error during extraction: {e}")
    
    def _write_metadata(self, output_file) -> None:
        """Write metadata information to the output file."""
        metadata = {
            "Extraction Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        
        output_file.write("# Codebase Documentation\n\n")
        output_file.write(json.dumps(metadata, indent=2) + "\n\n")
    
    def _process_file(self, relative_path: str, filepath: str, output_file) -> None:
        """Process and write a single file's content."""
        output_file.write(f"### {relative_path}\n```\n")
        if self._is_list_only(filepath):
            output_file.write("```\n[Binary file - content not extracted]\n```\n\n")
            return
            
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                output_file.write(content)
                output_file.write("\n```\n\n")
        except Exception as e:
            output_file.write(f"```\nError reading file: {e}\n```\n\n")

if __name__ == "__main__":
    # Example usage
    extractor = CodebaseExtractor(
        base_directory=".",  # Current directory
        output_file="codebase_snapshot.md",  # Output file
        config_file="codebase_config.json"  # Optional config file
    )
    extractor.extract()