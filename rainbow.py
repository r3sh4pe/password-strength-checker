import hashlib
import os


def create_sha1_hash_files() -> None:
    wordlist_dir = './password_lists/'

    if not os.path.exists(wordlist_dir):
        print(f"Directory {wordlist_dir} does not exist.")
        return

    for wordlist_file in os.listdir(wordlist_dir):
        if wordlist_file.endswith('.sha1'):
            continue

        input_path = os.path.join(wordlist_dir, wordlist_file)
        output_path = os.path.join(wordlist_dir, f"{wordlist_file}.sha1")

        if os.path.exists(output_path):
            print(f"Skipping {wordlist_file} as {output_path} already exists.")
            continue

        print(f"Processing {wordlist_file}...")

        try:
            with open(input_path, 'r', encoding='utf-8', errors='ignore') as infile:
                passwords = infile.read().splitlines()

            with open(output_path, 'w', encoding='utf-8') as outfile:
                for password in passwords:
                    if password:
                        sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
                        outfile.write(f"{sha1_hash}\n")

            print(f"Created {output_path} with {len(passwords)} hashed passwords.")

        except Exception as e:
            print(f"Error processing {wordlist_file}: {str(e)}")


if __name__ == "__main__":
    create_sha1_hash_files()