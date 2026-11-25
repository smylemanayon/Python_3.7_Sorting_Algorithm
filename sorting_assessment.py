"""
Assessment 3.7: Sorting Algorithms
Student Name: Smyle Rojo Manayon
Sorting Method: Merge Sort (Divide and Conquer)
"""


def extract_unique_letters(full_name: str, case_sensitive: bool = False) -> list[str]:
    """
    Extracts alphabetic letters only (excluding spaces and symbols)
    and discards duplicate letters while preserving first-seen order.
    """
    unsorted_unique: list[str] = []
    seen: set[str] = set()

    for ch in full_name:
        if ch.isalpha():
            letter = ch if case_sensitive else ch.lower()
            if letter not in seen:
                seen.add(letter)
                unsorted_unique.append(letter)

    return unsorted_unique


def merge_sort(arr: list[str]) -> list[str]:
    """Sorts a list of letters alphabetically using Merge Sort."""
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])

    return merge(left_sorted, right_sorted)


def merge(left: list[str], right: list[str]) -> list[str]:
    """Merges two sorted lists into one sorted list."""
    merged: list[str] = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def main() -> None:
    full_name = "Smyle Rojo Manayon"

    # 1. Unsorted array (symbols/spaces excluded, duplicates discarded)
    unsorted_letters = extract_unique_letters(full_name, case_sensitive=False)

    # 2. Sorted array using Merge Sort
    sorted_letters = merge_sort(unsorted_letters)

    print(f"Full Name      : {full_name}")
    print(f"Unsorted Array : {unsorted_letters}")
    print(f"Sorted Array   : {sorted_letters}")


if __name__ == "__main__":
    main()