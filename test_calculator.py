from calculator import add, subtract, multiply, divide, Circle_Area

def test_multiply():
	assert multiply (7, 4) == 28

def test_subtract():
	assert subtract (9, 4) == 5

def test_add():
	assert add (2,3) == 5

def test_divide():
	assert divide(6, 2) == 3

def test_divide_uneven():
	#arrange
	a, b = 5, 2
	#act
	result = divide(a, b)
	#assert
	assert result == 2.5

def test_circleArea():
	assert Circle_Area(-4) == "Error"
