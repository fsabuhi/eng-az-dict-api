# eng-az-dict

`eng-az-dict-api` is a RESTful API built with Django that provides English to Azerbaijani dictionary functionality. It allows users to search for English words and get their Azerbaijani translations, examples, and meanings.

This API is used by the BeSocial Bot, a Telegram bot that provides English to Azerbaijani dictionary functionality within the Telegram app. You can learn more about BeSocial at https://besocialeng.com/.

## Installation

To install `eng-az-dict-api`, you can clone the repository and install the dependencies:

```
git clone https://github.com/yourusername/eng-az-dict-api.git
cd eng-az-dict-api
pip install -r requirements.txt
```

Alternatively, you can download the source code from the repository and install the dependencies manually.

## Usage

To use `eng-az-dict-api`, you can start the Django development server:

```
python manage.py runserver
```

You can then make requests to the API using a tool like `curl` or a web browser. For example, to search for the Azerbaijani translation, example, and meaning of the English word "hello", you can make a GET request to the `/word` endpoint:

```
http://localhost:8000/word/hello
```

The API will return a JSON response with the Azerbaijani translation, example, and meaning:

```json
{
    "word": "hello",
    "translation": "salam",
    "example": "Hello, how are you?",
    "meaning": "used as a greeting or to begin a telephone conversation"
}
```

For more information on the available endpoints, please refer to the `views.py` file.

## Acknowledgments

`eng-az-dict-api` uses the `django-rest-framework` library for building the API.
