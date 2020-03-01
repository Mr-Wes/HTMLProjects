def test_name(user_name):
	if user_name.strip():
		return True
	else:
		return False

def test_pass(user_password):
	if user_password:
		return True
	else:
		return False
		