# emacs-etags-files-list

## What does this do?

This is a Python script that searches directories for files that fit certain criteria (e.g. files that match a certain regular expression), and creates an output file containing full paths to those files. The output file is then used an input to the ctags command, to help create an exuberant ctags index that covers specific files.

## Why would I use this?

If you're working in a huge project, your etags files can easily become huge. This script helps create the etags index file small.

## Example JSON Input

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

## Example Output

The output file contains paths, e.g.:

```
c:\projects\js\animals.js
c:\projects\js\companies.js
c:\projects\foods.js
c:\projects\index.js
c:\projects\test.js
c:\projects2\colors.js
```
