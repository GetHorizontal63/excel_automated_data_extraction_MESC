import os
import shutil


def delete_fake_kdrive():
    BASE_DIR = r"C:\Data Projects\Fake KDrive"

    # Check if the directory exists
    if not os.path.exists(BASE_DIR):
        print(f"Directory '{BASE_DIR}' does not exist.")
        return

    # Ask for confirmation
    print(f"About to delete the entire directory: {BASE_DIR}")
    confirm = input("Are you sure you want to proceed? (yes/no): ").lower()

    if confirm == 'yes':
        try:
            shutil.rmtree(BASE_DIR)
            print(f"Successfully deleted '{BASE_DIR}'")
        except Exception as e:
            print(f"Error deleting directory: {str(e)}")
    else:
        print("Operation cancelled.")


if __name__ == "__main__":
    delete_fake_kdrive()