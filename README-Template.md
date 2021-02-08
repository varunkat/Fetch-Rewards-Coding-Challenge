# TEXT SIMILARITY COMPARISON

The below challenge is focused on comparing the similarity between two texts. The designed program will check for each word that is same and the frequency of the word appeared in both texts.
The desired output is scaled in a range from 0 to 1 based on the level of matched texts.

## Development

There are a bunch of decisions made to develop Text Similarity Algorithm.
* The algorithm is built by using the '.' punctuation as a separator. Once the text is split into sentences, then every sentence is split by using space as separator.
* The words which are same in both texts and the count of each word in both texts are matched. In this case, no ordering of words was done.
* This algorithm is developed using python data structures like Lists and dictionaries. The implementation of these data structures to solve this problem is mentioned in code as comments.


### Prerequisites
This web app requires the following to be up and running:
```
-Docker
-python(Environment is set up in the Dockerfile and requirements.txt)
-Flask(Environment is set up in Dockerfile and requirements.txt)
```

### Installing

* Install docker desktop from https://www.docker.com/
* Fork the repository and maintain the below file structure
```
 Fetch-Rewards-Coding-challenge
 |--Text-similarity
    |--templates
       |--text-similarity.html
    |--app.py
    |--requirements.text
 |--Dockerfile
 |--README.md
 ```

 * Open any code editor and Unix shell.
 * For docker, a dockerfile is designed so that it will be build by using below commands. In  order to do this, make sure that Docker is up and running.
 * Once you are inside Fetch-Rewards-Coding-Challenge folder, use below command to Build Docker image
```
   docker build -t text-similarity .
```
 * After the docker image is built successfully, use the below command to assign a port number to the container on which the python flask app will be running
```
   docker run -d -p 80:80 text-similarity
```
 * Enter Localhost:80 in any web browser and you can see the web application where you can copy and paste text samples.


## Running the tests

Once the web app is running, just copy and paste the text contents for which similarity check must be performed in the respective text inputs and click on generate to see the level of matched content on a scale of 0 to 1.



## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [Maven](https://www.python.org/) - Coding language used
* [Docker](https://www.docker.com/) - Used to deploy application without dependencies
