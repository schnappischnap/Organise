# Organise.py

Python script to organise files in a directory based on extension.

* Moves all files to sub-folders based on the files extension.
* The extensions and sub-folder names are defined in `Organise.json`.

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
