# check_uuid.py

Recursively checks all `.mobileprovision` files in a folder, or a single `.mobileprovision` file, for the presence of a given UUID and lists missing and matching files.

## Author

**Blandine**, 2025

## License

MIT License – see [LICENSE](LICENSE) file.

## Description

This Python script is useful for iOS developers, DevOps, or anyone working with provisioning profiles.  
It searches through a folder and its subfolders, or checks a single `.mobileprovision` file, and reports which ones contain (or are missing) a specified UUID.

---

## Features

- Recursively scans all `.mobileprovision` files in a folder
- Supports checking a single `.mobileprovision` file
- Checks for the presence of a UUID
- Lists files that are missing the UUID
- Lists files that contain the UUID (if not all files match)
- Handles unreadable files gracefully
- Provides clear terminal output

---

## Requirements

- Python 3.6+
- Works on macOS, Linux, and Windows (with Python 3 installed)

---

## Usage

### Check a folder

```bash
python3 check_uuid.py <UUID> <folder_path>
```

#### Example:

```bash
python3 check_uuid.py 12345678-ABCD /Users/me/Profiles
```

### Check a single .mobileprovision file

```bash
python3 check_uuid.py <UUID> <file_path>
```

#### Example:

```bash
python3 check_uuid.py 12345678-ABCD /Users/me/Profiles/Dev.mobileprovision
```

## Help

Print a short usage guide:

```bash
python3 check_uuid.py --help
```

#### Output:

```bash
Usage: python3 check_uuid.py <UUID> <folder_or_file_path>
Recursively checks all .mobileprovision files in the given folder,
or a single .mobileprovision file, for the UUID.
```
