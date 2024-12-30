from src import CodebaseExtractor

extractor = CodebaseExtractor(
    base_directory="./",
    output_file="codescribe/codebase_snapshot.md",
    config_file="codescribe/codebase_config.json"

)
extractor.extract()