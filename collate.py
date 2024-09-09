import csv
import os
from collections import defaultdict, Counter

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
    
    anime_data = defaultdict(lambda: {'count': 0, 'appearances': set()})

    for file_path in file_paths:
        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
            continue

        name = os.path.splitext(os.path.basename(file_path))[0]
        anime_list = extract_anime_list(file_path)
        update_anime_data(anime_data, name, anime_list)
    
    write_to_csv(anime_data, os.path.join(os.path.dirname(file_paths[0]), 'animedata.csv'))

def extract_anime_list(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        return [anime.lower() for anime in content.split('\n') if anime.strip()]

def update_anime_data(anime_data, name, anime_list):
    for anime in anime_list:
        anime_data[anime]['count'] += 1
        anime_data[anime]['appearances'].add(name)

def write_to_csv(anime_data, csv_path):
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['anime', 'count', 'appearances']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for anime, data in anime_data.items():
            writer.writerow({
                'anime': anime,
                'count': data['count'],
                'appearances': ', '.join(data['appearances'])
            })

if __name__ == "__main__":
    main()