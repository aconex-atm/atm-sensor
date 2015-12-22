import sys,  os

proj_path = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..'))
sys.path.append(proj_path)

from monitor import main

main.run()
