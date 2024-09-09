import csv
import os
from collections import Counter

def main():
    file_path = input("Enter the path to the name.txt file: ")
    if not os.path.isfile(file_path):
        print("File not found.")
        return

    name = os.path.splitext(os.path.basename(file_path))[0]
    anime_list = extract_anime_list(file_path)
    anime_count = Counter(anime_list)
    
    write_to_csv(name, anime_count, os.path.join(os.path.dirname(file_path), 'list.csv'))

def extract_anime_list(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Convert each anime name to lowercase
        return [anime.lower() for anime in content.split('\n')]

def write_to_csv(name, anime_count, csv_path):
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'anime', 'count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for anime, count in anime_count.items():
            writer.writerow({'name': name, 'anime': anime, 'count': count})

if __name__ == "__main__":
    main()