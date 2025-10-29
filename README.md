# check_uuid.py

Recursively checks all `.mobileprovision` files in a folder, a single `.mobileprovision` file, or inside an `.ipa` archive for the presence of a given UUID and lists missing and matching files.

## Author

**Blandine Rumeau**, 2025

## License

MIT License – see [LICENSE](LICENSE) file.

## Description

This Python script is useful for iOS developers, DevOps, or anyone working with provisioning profiles.
It searches through a folder, a single file, or an `.ipa` archive and reports which `.mobileprovision` files contain (or are missing) a specified UUID.

---

## Features

* Recursively scans all `.mobileprovision` files in a folder
* Supports checking a single `.mobileprovision` file
* Supports checking `.mobileprovision` files inside an `.ipa`
* Checks for the presence of a UUID
* Lists files that are missing the UUID
* Lists files that contain the UUID (if not all files match)
* Handles unreadable files gracefully
* Provides clear terminal output with emojis for quick visibility

---

## Requirements

* Python 3.6+
* Works on macOS, Linux, and Windows (with Python 3 installed)

---

## Usage

### Check a folder

```bash
python3 check_uuid.py <UUID> <folder_path>
```

Example:

```bash
python3 check_uuid.py 12345678-ABCD /Users/me/Profiles
```

### Check a single `.mobileprovision` file

```bash
python3 check_uuid.py <UUID> <file_path>
```

Example:

```bash
python3 check_uuid.py 12345678-ABCD /Users/me/Profiles/Dev.mobileprovision
```

### Check an `.ipa` file

```bash
python3 check_uuid.py <UUID> <ipa_file_path>
```

Example:

```bash
python3 check_uuid.py 12345678-ABCD /Users/me/Apps/MyApp.ipa
```

### Help

```bash
python3 check_uuid.py --help
```

Output:

```
Usage: python3 check_uuid.py <UUID> <path_to_folder_or_file_or_ipa>
Checks .mobileprovision files in the given folder, a single file, or inside an .ipa for the UUID.
```

---

## Example Output

**Case 1: All files contain UUID**

```
Found 7 .mobileprovision files, checking for UUID 12345678-ABCD...

✅ UUID found in all .mobileprovision files!

Checked 7 files total.
```

**Case 2: Some files missing UUID**

```
Found 7 .mobileprovision files, checking for UUID 12345678-ABCD...

❌ UUID missing in the following files:
 - /path/to/file1.mobileprovision

✅ UUID found in the following files:
 - /path/to/file2.mobileprovision
 - /path/to/file3.mobileprovision

Checked 7 files total.
```

**Case 3: Some files unreadable**

```
Found 7 .mobileprovision files, checking for UUID 12345678-ABCD...

⚠️ Could not read /path/to/file4.mobileprovision: [Error message]

❌ UUID missing in the following files:
 - /path/to/file1.mobileprovision

✅ UUID found in the following files:
 - /path/to/file2.mobileprovision
 - /path/to/file3.mobileprovision

Checked 7 files total.
```

**Case 4: Checking an IPA**

```
Detected input type: ipa
Unpacking MyApp.ipa...
Found 1 provisioning file(s) inside IPA.

✅ UUID found in all .mobileprovision files!
Checked 1 file total.
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
