# emacs-etags-files-list

This is a Python script that searches directories for files that fit certain criteria (e.g. files that match a certain regular expression), and creates an output file containing full paths to those files.

The script takes a JSON file containing the criteria as input, e.g.:

```json
{
    "output": "c:/projects/.emacs-js-tags-files",
    "log": "c:/projects/.emacs-js-tags-files.log",
    "dirs": [{
        "dir": "c:/projects",
        "exclude": ["c:/projects/nodetest/node_modules"],
        "include_regex": [".*?\\.js$"],
        "exclude_regex": [".*?\\.min\\.js$"]
    },{
        "dir": "c:/projects2",
        "exclude": [],
        "include_regex": [".*?\\.js$"],
        "exclude_regex": [".*?\\.min\\.js$"]
    }]
}
```
