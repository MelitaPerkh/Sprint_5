import random
import string
def generate_random_email(self):
        letters = string.ascii_lowercase
        rand_email = ''.join(random.sample(letters, 9))+"@example.com"
        return rand_email