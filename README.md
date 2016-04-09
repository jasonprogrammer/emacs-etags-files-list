# Search directories and create a file containing file paths

## What does this do?

This is a Python script that searches directories for files that fit certain criteria (e.g. files that match a certain regular expression), and creates an output file containing full paths to those files.

## Why would I use this?

Whenever you need to generate a file that contains file paths. If you're using Emacs, and generating [exuberant ctags](http://ctags.sourceforge.net/) while working in a huge project, your TAGS files can easily become huge. This script helps generate an input file for the ctags command, allowing you to specify exactly which files will be indexed.

For example, once I've generated the file containing file paths (.emacs-js.tags-files), I run this:

c:\ctags\ctags.exe -e -L .emacs-js-tags-files -f .emacs-js-tags

and get a smaller tags file (.emacs-js-tags).

## Dependencies

Python 3

## How do I run the script?

python3 create_files_list.py &lt;input_json_file&gt;

## Example JSON Input

The script takes a JSON file containing the criteria as input, e.g.:

```json
{
    "output": "c:/projects/.emacs-js-tags-files",
    "log": "c:/projects/.emacs-js-tags-files.log",
    "dirs": [{
        "dir": "c:/projects",
        "exclude": ["nodetest/node_modules"],
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
This example JSON file indicates that two separate directories should be recursively searched. Files with the extension (.js) will be included, but files with extension (.min.js) will be excluded. The *c:/projects/nodetest/node_modules* directory will not be traversed.

### JSON Parameters
*output* - A path to the output file (containing file paths)

*log* - A path to a log file file (for detail on files that were included/excluded)

*dirs* - An array of multiple configurations (so you can search multiple directories)

*dir* - A directory to search recursively

*exclude* - Relative paths (to directories or files) to exclude. This exclude rule runs first (has priority over the regular expressions).

*include_regex* - An array of regular expression patterns (for directories or files) to include.

*exclude_regex* - An array of regular expression patterns (for directories or files) to exclude. This runs last, and will take priority over include_regex.

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

##License

MIT License
