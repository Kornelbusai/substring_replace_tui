# Substring replacer in names for all files within a directory

## Description 

Script that removes substring from all file names within a directory.

## Usage

To use the script use the following command in terminal:

```bash
substring-replace --path "/path" --substring "text"
```

With /path being the exact pathname of the folder that the operation will be preformed on and text being the substring removed. If the filename continations a space or any character after the text include that space/character as well otherwise those space/character will be kept within the filename.


## Installation

Install the script using `pip`:

```bash
pip install git+https://github.com/Kornelbusai/substring_replace_tui
```

