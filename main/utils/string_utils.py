import random, string


def generate_noise(length):
    if length <= 0:
        raise Exception('length too low')
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase
                                                + string.digits)
                   for _ in range(length))
