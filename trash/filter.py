import os

def main():
    file_path = 'finallist.txt'
    if not os.path.isfile(file_path):
        print("File not found.")
        return

    anime_list = extract_anime_list(file_path)
    anime_list = remove_duplicates(anime_list)
    manually_filter_anime(anime_list)
    update_anime_list(file_path, anime_list)

def extract_anime_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().splitlines()
    return content

def remove_duplicates(anime_list):
    return list(dict.fromkeys(anime_list))

def manually_filter_anime(anime_list):
    i = 0
    while i < len(anime_list):
        j = i + 1
        while j < len(anime_list):
            if is_subset_or_duplicate(anime_list[i], anime_list[j]):
                print(f"1: {anime_list[i]}")
                print(f"2: {anime_list[j]}")
                choice = input("Select a number to remove (1 or 2) or press Enter to skip: ")
                if choice == '1':
                    anime_list.pop(i)
                    j = i + 1  # Reset j to check the new anime_list[i] against the rest
                elif choice == '2':
                    anime_list.pop(j)
                else:
                    j += 1
            else:
                j += 1
        i += 1

def is_subset_or_duplicate(anime1, anime2):
    anime1_lower = anime1.lower()
    anime2_lower = anime2.lower()
    return anime1_lower in anime2_lower or anime2_lower in anime1_lower

def update_anime_list(file_path, anime_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(anime_list))

if __name__ == "__main__":
    main()