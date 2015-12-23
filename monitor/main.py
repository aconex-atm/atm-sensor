import threading
from monitor.circuit.checker_edge import Checker_circuit
from monitor.ultrasonic.checker import Checker_ultrasonic
def run():

	ultrasonic_Thread = threading.Thread(target = Checker_ultrasonic(2,150,4,3).keepCheck)

	circuit_Thread = threading.Thread(target = Checker_circuit(1).keepCheck)
	ultrasonic_Thread.start() 
	circuit_Thread.start() 
