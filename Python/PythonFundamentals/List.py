def show(name):
    print(f'Hi, {name}')


def list_comprehension(mylist):
    new_list = []
    for n in mylist:
        new_list.append(n*2)
    print(new_list)
    new_list = [n*2 for n in mylist]     #List comprehension
    print(new_list)
    new_list = [n*2 for n in mylist if n % 2 == 0]  #list comprehension with condition
    print(new_list)
    mylist1 = mylist
    new_list = [(n1, n2) for n1 in mylist for n2 in mylist1 if n1+n2 > 3]    #list comprehension using multiple list
    print(new_list)


if __name__ == '__main__':
    show('list')
    firstList = [1, 2, 3, 4]
    list_comprehension(firstList)