from src import CodebaseExtractor

extractor = CodebaseExtractor(
    base_directory=".",
    output_file="codebase_snapshot.md",
    config_file="config/codebase_config.json"

)
extractor.extract()