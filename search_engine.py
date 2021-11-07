"""
Author: Anant
Date: 4/11/21
Purpose: Practice of python.
"""


def search_engin(list, search):
    """This is a function which returns the matches sentences from a list..
    which are searched by the user.."""
    search = search.lower(
    )  # Converting searched and existing sentence to found relevant matches easily..
    for index, word2 in enumerate(list):
        word2 = word2.lower()
        word1 = search.split(" ")

        world worl
        # getting one list element break into a list to search.
        how_many_time = 0
        for k in list_i:  # searching in list's sentences index by index.
            if k == search:
                # How many times that searched word came in that list..
                how_many_time += 1
            # print(f"Index is {index} and {how_many_time} it comes..")
            # Adding index of main list element and how many times searched word came into that
        else:
            pass


if __name__ == '__main__':
    list1 = ["I am a very good boy", "Hariom is also a good boy", "Sharukh khan is bad boy",
             "Everybody is gonna die", "My father told me to be only with good boys and help others",
             "If someone is giving someone something so it's good.", "Good boy is too good",
             "Good boy are those boys which are good and have good nature", "When I went to delhi I met some good boys",
             "Bad boys are bad", "The only person who can help you is you yourself"]

    search = input("Please input your query string.\n")
    search_engin(list1, search)
