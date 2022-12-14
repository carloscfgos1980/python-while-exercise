from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

list = random_koala_fact()


def unique_koala_facts(nr):
    i = 0
    while i < nr:
        print('unique characteristic', list[i])
        i = i + 1


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print('lets see:', random_koala_fact())

print('Funny characteristics:', list)

print('unique characteristic', unique_koala_facts(5))
