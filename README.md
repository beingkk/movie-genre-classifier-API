# Movie genre classifier app
Flask app with REST API for classifying movie genres based on their title and description. This is an exercise to deploy this [movie genre classifier](https://github.com/beingkk/movie-genre-classifier) model with an API.

## Installation

To get the app and install the dependencies, navigate to a convenient directory and run the following commands from the terminal:

```shell
$ git clone https://github.com/beingkk/movie-genre-classifier-API
$ cd movie-genre-classifier-API
$ python3 -m venv movie_genre_classifier_API
$ source movie_genre_classifier_API/bin/activate
$ pip3 install -r requirements.txt
```

## Usage
To start predicting movie genres, first you need to start the server:

```shell
$ python3 server.py 
```

After the server is running, you can predict movie genres by using the `request.py` script to make requests to the API

```shell
$ python3 request.py --title "The Matrix" --description "A programmer is brought back to reason and reality when learning he was living in a program created by gigantic machines which make human birth artificial. In order to set humanity free, Neo will have to face many enemies by using technologies and self-trust."
{
    "description": "A programmer is brought back to reason and reality when learning he was living in a program created by gigantic machines which make human birth artificial. In order to set humanity free, Neo will have to face many enemies by using technologies and self-trust.",
    "genre": "Science Fiction, Action",
    "title": "The Matrix"
}
```

Alternatively, you can also make API requests, e.g., with CURL

```shell
$ curl -d '{"title" : "The Matrix", "description": "A programmer is brought back to reason and reality when learning he was living in a program created by gigantic machines which make human birth artificial."}' http://localhost:5000/api
{
  "description": "A programmer is brought back to reason and reality when learning he was living in a program created by gigantic machines which make human birth artificial.",
  "genre": "Science Fiction",
  "title": "The Matrix"
}
```

## More information

Please find more information about the prediction model at its [corresponding github repo](https://github.com/beingkk/movie-genre-classifier).

