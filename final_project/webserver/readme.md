# Web Server

## Port number
The port our service runs on is 52048.

## How our service can and should be used
The server is started by running `python main.py` (python 3.6.1) in the webserver directory.  Then, users can submit get, post, put, and delete requests to the server according to the JSON guide (json_guide.pdf, or at this link: `https://docs.google.com/document/d/1I-N-W1Vq2LD-QqAIzOy-HOz32LTq61lNA8nGnECO_Og/edit?usp=sharing`) that is included in the webserver directory.  In order to test that the service works, run `python test_ws.py` in the webservice directory while the webservice is running (note that this makes a separate system call, and the actual unittest code is in various files inside the tests directory).
