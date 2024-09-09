import os

def main():
    file_paths = [
        'names/abo.txt',
        'names/bacon.txt',
        'names/bry.txt',
        'names/hy.txt',
        'names/kar.txt',
        'names/ken.txt',
        'names/red.txt',
        'names/tune.txt'
    ]
    
    for file_path in file_paths:
        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
            continue

        sort_file(file_path)

def sort_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().splitlines()  # Split content into lines
    
    sorted_content = sorted(content)  # Sort the lines alphabetically
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(sorted_content))  # Join sorted lines and write back

if __name__ == "__main__":
    main()