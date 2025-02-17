# Lists:
# <my_list> = [1, 2, "apple"] # Create a list
# <my_list>[0] # Access element at index 0
# <my_list>[-1] # Access last element
# <my_list>.append(4) # Add to end
# <my_list>.extend(<another_list>) # Append all items in <another_list> to <my_list>
# <my_list>.remove(1) # Remove first matching element
# del <my_list>[0] # Remove element at index 0

# Dictionaries:
# <my_dict> = {"a": 1, "b": "hello"} # Create a dictionary
# <my_dict>["a"] # Access value for key "a"
# <my_dict>.get("a") # Access value for key "a" (safer)
# <my_dict>["c"] = 3 # Insert key-value pair
# del <my_dict>["a"] # Remove key "a" and its value
# <my_dict>.pop("a") # Remove key "a" and its value

# OUT OF THE BOX FOR LOOP syntax
# for i in <my_list>:
# for k in <my_dict>.keys():
# for v in <my_dict>.values():
# for k, v in <my_dict>.items():

# OUT OF THE BOX if statement syntax
# if <boolean expression>:

# IF STATEMENT TO CHECK IF AN ELEMENT EXISTS IN A CONTAINER
# use the "in" keyword (operator) to construct a boolean expression of the form:
# <element> in <container>
# put the boolean expression in your if statement:
# if <element> in <container>:
# if i in <my_list>: # returns true if <my_list> contains i
# if k in <my_dict>: # returns true if <my_dict>.keys() contains k


def count_even(nums: list[int]) -> int:
    # function to count the number of even numbers in a list

    # initialize variable to count answer to 0
    ans: int = 0

    # iterate through nums
    for x in nums:
        # check if x is even - check if remainder of x and 2 is 0
        if x % 2 == 0:
            ans += 1

    # return number of even numbers
    return ans


def course_roster(students: dict[str, list[str]], course: str) -> list[str]:
    # make a list for the roster
    roster: list[str] = []

    # iterate through the students dictionary
    # for k, v in dict.items():
    for student, courses in students.items():
        # first iteration:
        # student: str = 'jake'; courses = ['physics', 'chem']
        # second iteration:
        # student: str = 'john'; courses = ['english']
        # cycle through courses, which is a list of strings
        for c in courses:
            # check if the value of c is the same as course
            if c == course:
                # add student to the roster
                roster.append(student)

    # return the list of students
    return roster


def merge_dictionaries(
    dict1: dict[str, list[int]], dict2: dict[str, list[int]]
) -> dict[str, list[int]]:
    # we will merge dict2 into dict1 directly and return dict1
    # no need to create a new "answer" dictionary

    # iterate over the ITEMS (key-value pairs) in dict2
    for key, vals in dict2.items():
        # check if the key key is in dict1 already
        if key in dict1:
            # if it is, we need to add vals to dict1[key]
            for i in vals:
                dict1[key].append(i)
            # we could avoid the for loop with the following line:
            # dict1[key].extend(vals)
        else:
            # if it is not, we need to create dict1[key], and set it to vals
            dict1[key] = vals

    return dict1


def main() -> None:
    print(count_even([1, 2, 3]))
    assert count_even([1, 2, 3]) == 1
    print(
        course_roster(
            {"jake": ["physics", "chemistry"], "john": ["english"]}, "physics"
        )
    )
    assert course_roster(
        {"jake": ["physics", "chemistry"], "john": ["english"]}, "physics"
    ) == ["jake"]
    print(
        merge_dictionaries({"a": [1, 2, 3], "b": [4, 5]}, {"b": [5, 6, 7], "c": [8, 9]})
    )
    assert merge_dictionaries(
        {"a": [1, 2, 3], "b": [4, 5]}, {"b": [5, 6, 7], "c": [8, 9]}
    ) == {"a": [1, 2, 3], "b": [4, 5, 5, 6, 7], "c": [8, 9]}


if __name__ == "__main__":
    main()
