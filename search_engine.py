"""
Author: Anant
Date: 4/11/21
Purpose: Practice of python.
"""

def search_engin(list, search):
    """This is a function which returns the matches sentences from a list..
    which are searched by the user.."""
    search = search.lower() # Converting searched and existing sentence to found relevant matches easily..
    for index, i in enumerate(list):
        i = i.lower()
        dic = {}
        # print(search, i)
        if search in i:
            list_i = i.split(" ") # getting one list element break into a list to search.
            print(list_i)
            how_many_time = 0
            for k in list_i: # searching in list's sentences index by index.
                if k == search:
                    how_many_time += 1 # How many times that searched word came in that list..

            # Adding index of main list element and how many times searched word came into that
            dic[index] = how_many_time 
        else:
            pass
    
    print(dic)


if __name__ == '__main__':
    list1 = ["I am a very good boy", "Hariom is also a good boy", "Sharukh khan is bad boy",\
    "Everybody is gonna die", "My father told me to be only with good boys and help others",\
    "If someone is giving someone something so it's good.", "Good boy is too good",\
    "Good boy are those boys which are good and have good nature", "When I went to delhi\
    I met some good boys", "Bad boys are bad", "The only person who can help you is \
    you yourself"]
    
    search = input("Please input your query string.\n")
    search_engin(list1, search)
