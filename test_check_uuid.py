import contextlib
import io
import os
import tempfile
import unittest
import zipfile
from pathlib import Path
from check_uuid import check_uuid_in_file, check_files_for_uuid


class TestCheckUUID(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.temp_dir = tempfile.TemporaryDirectory()
        self.dir_path = Path(self.temp_dir.name)

        # File with UUID
        self.file_with_uuid = self.dir_path / "with_uuid.mobileprovision"
        self.file_with_uuid.write_bytes(b"This is a test file containing UUID 1234-5678")

        # File without UUID
        self.file_without_uuid = self.dir_path / "without_uuid.mobileprovision"
        self.file_without_uuid.write_bytes(b"This file does not contain the UUID")

        # Empty file
        self.empty_file = self.dir_path / "empty.mobileprovision"
        self.empty_file.write_bytes(b"")

        # IPA file (zip containing two .mobileprovision files)
        self.ipa_file = self.dir_path / "test.ipa"
        with zipfile.ZipFile(self.ipa_file, 'w') as zipf:
            zipf.write(self.file_with_uuid, arcname="Payload/App.app/with_uuid.mobileprovision")
            zipf.write(self.file_without_uuid, arcname="Payload/App.app/without_uuid.mobileprovision")

    def tearDown(self):
        # Cleanup temporary directory
        self.temp_dir.cleanup()

    # --- Test single file ---
    def test_check_uuid_in_file_found(self):
        self.assertTrue(check_uuid_in_file("1234-5678", self.file_with_uuid))

    def test_check_uuid_in_file_not_found(self):
        self.assertFalse(check_uuid_in_file("1234-5678", self.file_without_uuid))

    def test_check_uuid_in_empty_file(self):
        self.assertFalse(check_uuid_in_file("1234-5678", self.empty_file))

    # --- Test multiple files ---
    def test_check_files_for_uuid(self):
        files = [self.file_with_uuid, self.file_without_uuid, self.empty_file]
        missing, matching, total = check_files_for_uuid("1234-5678", files)
        self.assertEqual(total, 3)
        self.assertIn(self.file_with_uuid, matching)
        self.assertIn(self.file_without_uuid, missing)
        self.assertIn(self.empty_file, missing)

    # --- Test IPA handling (simulate) ---
    def test_check_files_in_ipa(self):
        from check_uuid import check_files_for_uuid

        # Extract IPA to temp dir
        with tempfile.TemporaryDirectory() as extract_dir:
            with zipfile.ZipFile(self.ipa_file, 'r') as zipf:
                zipf.extractall(extract_dir)
            files = list(Path(extract_dir).rglob("*.mobileprovision"))
            missing, matching, total = check_files_for_uuid("1234-5678", files)
            
            self.assertEqual(total, 2)
            # One file has UUID, one does not
            self.assertEqual(len(matching), 1)
            self.assertEqual(len(missing), 1)

    # --- Test empty folder ---
    def test_check_files_in_empty_folder(self):
        empty_dir = self.dir_path / "empty_folder"
        empty_dir.mkdir()
        files = list(empty_dir.rglob("*.mobileprovision"))
        missing, matching, total = check_files_for_uuid("1234-5678", files)
        self.assertEqual(total, 0)
        self.assertEqual(len(missing), 0)
        self.assertEqual(len(matching), 0)

    # --- Test unreadable file ---
    def test_unreadable_file(self):
        unreadable_file = self.dir_path / "unreadable.mobileprovision"
        unreadable_file.write_bytes(b"Some data")
        # Make file unreadable
        os.chmod(unreadable_file, 0)
        try:
            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                result = check_uuid_in_file("1234-5678", unreadable_file)
            self.assertFalse(result)
        finally:
            # Reset permissions so tearDown can delete
            os.chmod(unreadable_file, 0o644)


if __name__ == "__main__":
    unittest.main()
