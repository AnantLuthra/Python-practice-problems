"""
Author: Anant
Date: 4/11/21
Purpose: Practice of python.
"""

def search_engin(list, search):
    """This is a function which returns the matches sentences from a list..
    which are searched by the user.."""
    search = search.lower() # Converting searched and existing sentence to found relevant matches easily..
    for i in list:
        i = i.lower()
        dic = {}
        if search in i:
            dic.append(index)
            for index, k in enumerate(i): # searching in list's sentences index by index.
                if k == search:
                    how_many_time += 1
                    


if __name__ == '__main__':
    list1 = ["I am a very good boy..", "Hariom is also a good boy", "Sharukh khan is bad boy.."\
        "Everybody is gonna die.", "My father told me to be only with good boys. and help others.", \
            "If someone is giving someone something so it's good.", "Good boy is too good."\
                "Good boy are those boys which are good and have good nature." , "When I went to delhi\
                    I met some good boys.", "Bad boys are bad.", "The only person who can help you is \
                        you yourself."]
    
    search = input("Please input your query string.\n")
    search_engin(list1, search)
