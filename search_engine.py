"""
Author: Anant
Date: 4/11/21
Purpose: Practice of python.
"""


def search_engin(list, search):
    """This is a function which returns the matches sentences from a list..
    which are searched by the user.."""
    search = search.lower()  # Converting searched and existing sentence to found relevant matches easily..
    for index, i in enumerate(list):
        i = i.lower()
        index1 = []
        how_many_time_list = []
        # print(search, i)
        if search in i:
            # getting one list element break into a list to search.
            list_i = i.split(" ")
            how_many_time = 0
            for k in list_i:  # searching in list's sentences index by index.
                if k == search:
                    # How many times that searched word came in that list..
                    how_many_time += 1
            # print(f"Index is {index} and {how_many_time} it comes..")
            how_many_time_list.append(how_many_time)
            index1.append(index)
            # Adding index of main list element and how many times searched word came into that
        else:
            pass

    for i in range(len(index1)):
        print(
            f"Index is {index1[i]} and {how_many_time_list[i]} times it comes.")


if __name__ == '__main__':
    list1 = ["I am a very good boy", "Hariom is also a good boy", "Sharukh khan is bad boy",
"Everybody is gonna die", "My father told me to be only with good boys and help others",
"If someone is giving someone something so it's good.", "Good boy is too good",
"Good boy are those boys which are good and have good nature", "When I went to delhi I met some good boys",
"Bad boys are bad", "The only person who can help you is you yourself"]

    search = input("Please input your query string.\n")
    search_engin(list1, search)
