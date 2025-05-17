# CSCE3335-Project3
Project 1 for CSCE 3335 Networks and Data Communication with Dr. Habib M. Ammari

## Special Encoding Scheme Implementation

This project implements a client-server socket program that demonstrates a special encoding scheme for integers between -121 and 121 using powers of 3.

### Problem Description

The encoding scheme works as follows:
- Input integers (N) must be non-zero values between -121 and 121
- Numbers are decomposed using powers of 3: 1 (3⁰), 3 (3¹), 9 (3²), 27 (3³), and 81 (3⁴)
- Each power of 3 appears exactly once in the decomposition
- Each power of 3 is preceded by a coefficient that can be -1, 0, or 1
- The resulting sequence of coefficients is sent from server to client

### Examples

1. N = -3
   - Decomposition: 0 × 81 + 0 × 27 + 0 × 9 - 1 × 3 + 0 × 1
   - Code: (0, 0, 0, -1, 0)

2. N = 7
   - Decomposition: 0 × 81 + 0 × 27 + 1 × 9 - 1 × 3 + 1 × 1
   - Code: (0, 0, 1, -1, 1)

3. N = -5
   - Decomposition: 0 × 81 + 0 × 27 - 1 × 9 + 1 × 3 + 1 × 1
   - Code: (0, 0, -1, 1, 1)

### Implementation Details

The project consists of two main components:

1. **Client**
   - Receives integer input from user (-121 to 121)
   - Sends the integer to the server
   - Receives and visualizes the encoded sequence

2. **Server**
   - Receives integer from client
   - Generates the encoded sequence using the special encoding scheme
   - Sends the sequence back to the client

### Key Observations

The following intervals play a particular role in the encoding scheme:
- [-121, -41]
- [-40, -14]
- [-13, -5]
- [-4, -2]
- [-1, -1]
- [1, 1]
- [2, 4]
- [5, 13]
- [14, 40]
- [41, 121]

### Requirements

- Python 3.x
- Socket programming libraries

### How to Run

1. Start the server:
```bash
python server.py
```

2. Start the client:
```bash
python client.py
```

3. Enter an integer between -121 and 121 when prompted by the client

### Project Structure

- `server.py`: Server implementation
- `client.py`: Client implementation
- `README.md`: Project documentation
