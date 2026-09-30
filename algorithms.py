# algorithms used in the waste tracker.


def summation(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total


def find_maximum(numbers):
    if len(numbers) == 0:
        return 0

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


def count_items(items, target):
    count = 0

    for item in items:
        if item == target:
            count = count + 1

    return count


def remove_duplicates(items):
    unique_items = list(set(items))
    return unique_items


def partition_records(records, category):
    selected = []

    for record in records:
        if record["category"] == category:
            selected.append(record)

    return selected
