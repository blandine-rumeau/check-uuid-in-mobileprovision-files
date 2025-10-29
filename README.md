# check_uuid.py
[![Python Tests](https://github.com/blandine-rumeau/check-uuid-in-mobileprovision-files/actions/workflows/python-tests.yml/badge.svg)](https://github.com/blandine-rumeau/check-uuid-in-mobileprovision-files/actions/workflows/python-tests.yml)

A Python utility to check for a given UUID inside `.mobileprovision` files — either in a folder, a single file, or even inside an `.ipa` archive.

---

## 🧑‍💻 Author

**Blandine** — 2025  
MIT License

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).

---

## 📘 Description

This script helps developers verify whether a specific UUID (for example, a provisioning profile identifier) exists within their iOS provisioning files.  
It supports three input modes:

- A **folder** containing multiple `.mobileprovision` files (recursive)
- A **single `.mobileprovision` file**
- An **`.ipa` file** (automatically unpacked and checked inside)

---

## ✨ Features

- Checks recursively through directories
- Handles `.ipa` archives automatically
- Displays matching and missing files
- Handles unreadable files gracefully
- Lightweight — no external dependencies

---

## ⚙️ Requirements

- Python **3.7+**
- Runs on macOS, Linux, or Windows

---

## 🚀 Usage

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

### Example 1 – Folder mode

```bash
python3 check_uuid.py 12345678-ABCD-90EF-1234-567890ABCDEF ~/ProvisionProfiles/
```

Output example:

```
Detected input type: folder
Found 168 .mobileprovision file(s), checking for UUID 12345678-ABCD-90EF-1234-567890ABCDEF...

✅ UUID found in the following files:
  - /Users/blandine/ProvisionProfiles/dev_team.mobileprovision

❌ UUID missing in the following files:
  - /Users/blandine/ProvisionProfiles/old_profile.mobileprovision

Checked 168 files total.
```

---

### Example 2 – Single file mode

```bash
python3 check_uuid.py 12345678-ABCD-90EF-1234-567890ABCDEF ~/Downloads/MyProfile.mobileprovision
```

Output example:

```
Detected input type: file
Checking single .mobileprovision file /Users/blandine/Downloads/MyProfile.mobileprovision for UUID 12345678-ABCD-90EF-1234-567890ABCDEF...

✅ UUID found in all .mobileprovision files!
Checked 1 file total.
```

---

### Example 3 – IPA mode

```bash
python3 check_uuid.py 12345678-ABCD-90EF-1234-567890ABCDEF MyApp.ipa
```

Output example:

```
Detected input type: ipa
Unpacking MyApp.ipa...
Found 2 .mobileprovision file(s), checking for UUID 12345678-ABCD-90EF-1234-567890ABCDEF...

✅ UUID found in the following files:
  - Payload/MyApp.app/embedded.mobileprovision

Checked 2 files total.
```

