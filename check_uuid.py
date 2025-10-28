#!/usr/bin/env python3
"""
check_uuid.py
Author: Blandine
Year: 2025
Description: Recursively checks all .mobileprovision files in a folder
             or a single .mobileprovision file for the presence of a given UUID
             and lists missing and matching files.
License: MIT
"""
from pathlib import Path
import sys
import os

def find_missing_uuid(uuid, input_path):
    missing_files = []
    matching_files = []

    path = Path(input_path)

    # Determine if input is a folder or a single file
    if path.is_dir():
        files = list(path.rglob("*.mobileprovision"))
    elif path.is_file() and path.suffix == ".mobileprovision":
        files = [path]
    else:
        print(f"❌ {input_path} is neither a folder nor a .mobileprovision file.")
        sys.exit(1)

    total_files = len(files)
    print(f"Found {total_files} .mobileprovision files, checking for UUID {uuid}...\n")

    for file_path in files:
        try:
            with open(file_path, "rb") as f:
                data = f.read()
                if uuid.encode() in data:
                    matching_files.append(str(file_path))
                else:
                    missing_files.append(str(file_path))
        except Exception as e:
            print(f"⚠️ Could not read {file_path}: {e}")

    # Output results
    if total_files == len(matching_files):
        print("\n✅ UUID found in all .mobileprovision files!")
    else:
        if missing_files:
            print("\n❌ UUID missing in the following files:")
            for f in missing_files:
                print(" -", f)
        if matching_files:
            print("\n✅ UUID found in the following files:")
            for f in matching_files:
                print(" -", f)

    print(f"\nChecked {total_files} files total.\n")
    return missing_files

if __name__ == "__main__":
    # Show help if requested
    if len(sys.argv) == 2 and sys.argv[1] in ("--help", "-h"):
        print("Usage: python3 check_uuid.py <UUID> <folder_or_file_path>")
        print("Recursively checks all .mobileprovision files in the given folder, or a single .mobileprovision file, for the UUID.")
        sys.exit(0)

    # Validate arguments
    if len(sys.argv) != 3:
        print("Usage: python3 check_uuid.py <UUID> <folder_or_file_path>")
        sys.exit(1)

    uuid = sys.argv[1]
    input_path = sys.argv[2]

    missing = find_missing_uuid(uuid, input_path)
