import os

def main():
    file_path = 'ken.txt'
    if not os.path.isfile(file_path):
        print("File not found.")
        return

    update_file(file_path)

def update_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().splitlines()
    
    unique_content = sorted(content)  # Remove duplicates while preserving order
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(unique_content))

if __name__ == "__main__":
    main()