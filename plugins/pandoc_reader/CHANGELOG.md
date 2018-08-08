# Changelog for pandoc_reader

## October 7, 2017

*   Modify command-line arguments passed to pandoc in `pandoc_reader.py` when generating HTML output
    
    *   Arguments changed from
        
        ```python
        pandoc_cmd = ["pandoc", "--from=markdown" + extensions, "--to=html5"]
        ```
        to
        
        ```python
        pandoc_cmd = [
            "pandoc", "+RTS", "-K512m", "-RTS", "--from=markdown" + extensions,
            "--to=html5"
        ]
        ```

