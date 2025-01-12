## RPC Hello World

**Description**  
This project demonstrates a basic implementation of an XML-RPC server and client using Python. The server listens for requests on a specified port, while the client sends a "Hello, World" message to the server, which responds accordingly.

**Technologies**  
Python: Version 3.11 or higher  
XML-RPC: Built-in Python library for remote procedure calls  
Docker: To containerize and run the project  

**Requirements**  
Python installed (version 3.11 or higher).  
Docker installed and running.  

**How to Clone the Project**  
To clone the repository, execute the following commands:  
git clone <repository-url>  
cd hola_mundo_rpc  
Replace <repository-url> with the actual repository link from GitHub or GitLab.

**How to Run**  
Run the Server  
Start the XML-RPC server by executing:  
```bash
python server.py  
```
You should see the following output:  
RPC server started and listening on port 8000...  
#Run the Client  
To connect to the server and send a request, run the client:  
```bash
python client.py
```  
Expected output:  
Server response: Hello, World  

**How to Dockerize**  
Build the Docker Image  
Create a Docker image for the project:  
docker build -t rpc-hello-world .  
Run the Server in a Container  
Start the server inside a Docker container:  
docker run -d -p 8000:8000 --name rpc-server rpc-hello-world  
Run the Client in a Container  
Run the client from another Docker container:  
docker run --rm --name rpc-client rpc-hello-world python client.py  

**Docker Hub Link**  
Replace <docker-hub-link> with the link to your Docker Hub repository.  

**Docker Hub Repository**  
Provide the actual Docker Hub repository URL to pull the pre-built images.
