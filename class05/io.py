# To write:

with open(the_filename, 'wb') as f:
    pickle.dump(my_list, f)

# To read:

with open(the_filename, 'rb') as f:
    my_list = pickle.load(f)
