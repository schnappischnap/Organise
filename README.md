# Organise.py

Python script to organise files in a directory based on extension.

* Moves all files to sub-folders based on the files extension.
* Moves files in the current working directory or the first command line argument.
* Can specify certain files to be ignored, preventing them from being moved.
* The extensions, sub-folder names, and exclusions are defined in `Organise.json`.

`Organise.json` is used in this format:
```JSON
{
  "Exclude": [
    "filename1",
    "filename2"
  ],
  "Directories": {
    "Folder1": [
      ".extension1",
      ".extension2"
    ],
    "Folder2": [
      ".extension3"
    ]
  }
}
```
