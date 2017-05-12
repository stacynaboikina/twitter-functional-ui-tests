import string
import random


def rand_name_generator(size=5):
    chars = "{}{}".format(string.ascii_uppercase, string.digits)
    return 'test-{}'.format(''.join(random.choice(chars) for _ in range(size)))


