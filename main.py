from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

list = [random_koala_fact()]


def unique_koala_facts(nr):
    my_list = []
    i = len(list)
    while i > 0:
        if (i == nr):
            break
        i -= 1
    my_list.append(list[i])
    return my_list


'''
def num_joey_facts():
    i = 10
    while i >= 0:
        print('num of just something:', list[i])
        i -= 1
    else:
        print('number of joey facts', i)
'''

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print('lets see:', random_koala_fact())

print('Funny characteristics:', list)

print('unique characteristic:\n', unique_koala_facts(2))

# print('num of Joey facts', num_joey_facts())
