import pytest
import diceRollingSimulator
from unittest import mock
def test_die():
	with mock.patch('builtins.input', input_value=range(1,10)):
		assert diceRollingSimulator.run()==range(1,7)
	with mock.patch('builtins.input',input_value=0):
		assert diceRollingSimulator.run()=="Game Terminated!"
	with mock.patch('builtins.input', input_value='a'):
		assert diceRollingSimulator.run()=="Only integers are allowed"
if __name__=='__main__':
	pytest.main()