#!/usr/bin/env python3
"""
check_uuid.py
Author: Blandine
Year: 2025
Description: Checks all .mobileprovision files in a folder, a single .mobileprovision file,
             or inside an .ipa archive for the presence of a given UUID,
             and lists missing and matching files.
License: MIT
"""
from pathlib import Path
import sys
import tempfile
import zipfile

def check_uuid_in_file(uuid, file_path):
    """
    Returns True if the UUID is present in the given .mobileprovision file, False otherwise.
    Handles unreadable files gracefully.
    """
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            return uuid.encode() in data
    except Exception as e:
        print(f"⚠️ Could not read {file_path}: {e}")
        return False

def check_files_for_uuid(uuid, files):
    """
    Checks a list of .mobileprovision files for the UUID.
    Returns (missing_files, matching_files, total_files)
    """
    missing_files = []
    matching_files = []

    for f in files:
        if check_uuid_in_file(uuid, f):
            matching_files.append(f)
        else:
            missing_files.append(f)
    
    total_files = len(files)
    return missing_files, matching_files, total_files

def report_results(missing_files, matching_files, total_files):
    if total_files == 0:
        print("\n⚠️  No .mobileprovision files found.")
        return

    if len(matching_files) == total_files:
        print("\n✅ UUID found in all .mobileprovision files!")
    else:
        if matching_files:
            print("\n✅ UUID found in the following files:")
            for f in matching_files:
                print(f"  - {f}")

        if missing_files:
            print("\n❌ UUID missing in the following files:")
            for f in missing_files:
                print(f"  - {f}")

if __name__ == "__main__":
    # Simple sys.argv parsing with help
    if len(sys.argv) == 2 and sys.argv[1] in ("--help", "-h"):
        print("Usage: python3 check_uuid.py <UUID> <path_to_folder_or_file_or_ipa>")
        print("Checks .mobileprovision files in the given folder, a single file, or inside an .ipa for the UUID.")
        sys.exit(0)

    if len(sys.argv) != 3:
        print("Usage: python3 check_uuid.py <UUID> <path_to_folder_or_file_or_ipa>")
        sys.exit(1)

    uuid = sys.argv[1]
    input_path = Path(sys.argv[2])

    # Detect input type
    if input_path.is_dir():
        mode = "folder"
    elif input_path.suffix == ".mobileprovision":
        mode = "file"
    elif input_path.suffix == ".ipa":
        mode = "ipa"
    else:
        print(f"❌ Unsupported input type: {input_path}")
        sys.exit(1)

    # Prepare the list of files depending on mode
    if mode == "ipa":
        print(f"Detected input type: ipa")
        print(f"Unpacking {input_path.name}...")
        with tempfile.TemporaryDirectory() as tmpdir:
            with zipfile.ZipFile(input_path, 'r') as zip_ref:
                zip_ref.extractall(tmpdir)

            extracted_path = Path(tmpdir)
            files = list(extracted_path.rglob("*.mobileprovision"))
            print(f"Found {len(files)} .mobileprovision file(s), checking for UUID {uuid}...")

            missing_files, matching_files, total_files = check_files_for_uuid(uuid, files)

    elif mode == "folder":
        print(f"Detected input type: folder")
        files = list(input_path.rglob("*.mobileprovision"))
        print(f"Found {len(files)} .mobileprovision file(s), checking for UUID {uuid}...")

        missing_files, matching_files, total_files = check_files_for_uuid(uuid, files)

    elif mode == "file":
        print(f"Detected input type: file")
        files = [input_path]
        print(f"Checking single .mobileprovision file {input_path} for UUID {uuid}...")

        missing_files, matching_files, total_files = check_files_for_uuid(uuid, files)

    # Report results
    report_results(missing_files, matching_files, total_files)

    # Print total files checked
    print(f"\nChecked {total_files} file{'s' if total_files != 1 else ''} total.")
