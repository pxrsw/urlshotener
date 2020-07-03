import random


def code_generator(size = 6, chars = string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size = 6):
	new_code = code_generator(size = size)
	klass = instance.__class__
	qs_exist = klass.object.filter(shortcode = new_code).exist()

	if qs_exist:
		return create_shortcode(size = size)
	return new_code