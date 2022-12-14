color_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

one = input()
two = input()
three = input()

print((color_list.index(one)*10 + color_list.index(two)) * (10 ** color_list.index(three)))