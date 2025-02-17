# CSCE3335-Project1
Project 1 for CSCE 3335 Networks and Data Communication with Dr. Habib Amari

This project implements a client-server model using TCP/IP sockets to transmit and sort sequences of 'T','A','M' letters through both a GUI and command-line interface

## **Technologies Used:**
	•	Python 3.12
	•	Tkinter (for the GUI)
	•	Pytest (for automated testing)
	•	Socket (for networking)
	•	Subprocess (for managing client and server executions)

## **File Structure:**
📂 CSCE3335-Project1  
 ┣ 📂 gui/                # Contains the Tkinter GUI <br>
 ┣ 📂 tests/              # Contains Pytest test scripts <br>
 ┣ 📜 main.py             # Entry point for the application <br>
 ┣ 📜 algorithm.py         # Dutch National Flag algorithm implementation <br>
 ┣ 📜 networking.py        # Client-server logic with sockets <br>
 ┗ 📜 README.md            # Project documentation <br>

## **Installation Instructions:**
```
git clone https://github.com/rener2104/CSCE3335-Project1.git
cd CSCE3335-Project1
pip install pipenv
pipenv install
pipenv shell
```
## **Running the Program:**
#### Help:
`python main.py`
## Using GUI:
#### Start GUI:
`python main.py start`
## Using Command Line Interface
#### Start the Server:
`python main.py server`
#### Start the Client:
`python main.py client`
#### Run Automated Tests:
`python main.py tests`




