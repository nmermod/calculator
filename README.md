A python3 calculator that is operated using the terminal, built in SCCM4910.

What Will it do?

Add, subtract, multiply and divide two numbers, then display the result.


How to run it:

Run: python3 calculator.py
OR
Run: ./run.sh

Enter the first number, the second number, and then the operator (+,-,*,/)
The program prints out Result: followed by the result of the operation.

To stop it, press Ctrl+C.

HOW TO TEST IT

run source /opt/python-venv/sccm-4910/bin/activate 
run ./check.sh

This will run a test that takes some inputs and check they give the required
results when ran with an operator.
Running the first line activtes the SCCM4910 environment so that ./check.sh
can be ran.

