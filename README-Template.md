# TEXT SIMILARITY COMPARISON

The below challenge is focused on comparing the similarity between two texts. The designed program will check for each word that is same and the frequency of the word appeared in both texts.
The desired output is scaled in a range from 0 to 1 based on the level of matched texts.

## Development

There are a bunch of decisions made to develop Text Similarity Algorithm.
*The algorithm is built by using the '.' punctuation as a separator. Once the text is split into sentences, then every sentence is split by using ' '.
*The words which are same in both texts and the count of each word in both texts are matched. In this case, no ordering of words was done.
*This algorithm is developed using python data structures like Lists and dictionaries. The implementation of these data structures to solve this problem is mentioned in code as comments.


### Prerequisites
This web app requires the following to be up and running:
```
*python(Environment is set up in the Docker image)
*Flask
*Docker
```

### Installing

*Install docker desktop from https://www.docker.com/
*Fork the repository and maintain the below file structure
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

 *Open any code editor and Unix shell.
 *For docker, a dockerfile is designed so that it will be build by using compose commands. Inorder  to do this, make sure that Docker is up and running.
 *Once you are inside Fetch-Rewards-Coding-Challenge folder, use below command to compose Docker image
```
   docker build -t text-similarity .
```
 *After the docker image is built successfully, use the below command to assign a port number to the container on which the python flask app will be Running
```
   docker run -d -p 80:80 text-similarity
```
 *Enter Localhost:80 in any web browser and you can see the web application where you can copy and paste text samples in two boxes and click on generate button to get the similarity scale.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
