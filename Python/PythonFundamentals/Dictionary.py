


def dict_test():
    empty_dict = {}
    print (empty_dict)

    phone_book = {'shelendra' : 989876781,
                  'you': 877777899
                  }
    print (phone_book)
    print(phone_book["shelendra"])

    phone_book = dict([('shelendra',987799), ('you', 889797)])
    print(phone_book)
    print (phone_book.get("you"))

    phone_book['aa'] = 99
    del phone_book['you']

    print(phone_book)

    new_phone_book = {n*2 : person  for (n,person) in phone_book.items()}
    print(new_phone_book)


if __name__ == '__main__':
    dict_test()