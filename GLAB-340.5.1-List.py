""" 
create a game that will present the users with a list of words,
andmake them  perform various operations on the list to transform 
it into a target list.
"""


def gen_target_list(number_words, current_list):
    """ Create a function to generate a target list, which can be random or pre-defined."""
    return current_list[:number_words]


def display_current_target_list(current_list, target_list):
    """ Create a function to display the current list and target list to the user."""

    return current_list, target_list


def perform_operation(current_list):
    """ Create a function to allow the user to perform operations on the list"""

    current_list.append("chicken")
    new_list = ["dog", "cat", "rat"]
    current_list.extend(new_list)
    list_concat = current_list[1] + current_list[4]

    return current_list, list_concat


def current_matches_taget_list(current_list, target_list):
    """ Create a function to check if the current list matches the target list and end the game if it does."""
    if current_list == target_list:
        return True
    else:
        return False


def main():
    current_list = ["banana", "orange", "cherry",
                    "apple", "mango", "kiwi", "pineapple"]
    # Generate target lists
    target_list = gen_target_list(4, current_list)

    # Displaying current and target lists.
    print("Displaying current and target lists:")
    print(display_current_target_list(current_list, target_list))

    # Performing operations on the list
    print("\nPerforming operations on the list:")
    modified_list, concat_result = perform_operation(current_list.copy())
    print(f"Modified list after operations: {modified_list}")
    print(f"Concatenated strings: {concat_result}")

    # Check if the current list matches the target list
    if current_matches_taget_list(current_list, target_list):
        print("Current list matches the target list! Game Over.")
    else:
        print("Current list does not match the target list Keep playing.")


if __name__ == "__main__":
    main()
