# Petshop API

This is a project to help pet shops register the animals they receive for treatment, specifying the groups of animals and their characteristics

# Clone

Clone this repository on your local machine. 

Use the terminal for this.

```bash
git clone git@gitlab.com:CarlosMartorini/kenzie-pet.git
```

# Installation

Enter the project dependencies and install the virtual environment.

```bash
python -m venv venv
```

Enter the virtual environment

```bash
source venv/bin/activate
```

And now install the dependencies stored in the requirements.txt file

```bash
pip install -r requirements.txt
```

# Usage

Run migrations with the following command so that db.sqlite is created.

```bash
python manage.py migrate
```

Put the local server to run.

```bash
python manage.py runserver
```

Local server URL: http://127.0.0.1:8000/

# Routs

## Registering an animal:

- POST api/animals/
- Status HTTP 201 CREATED

```JSON
{
    "name": "Frank",
    "age": 5,
    "weight": 34,
    "sex": "male",
    "group": {
      "name": "dog",
      "scientific_name": "canis familiaris"
    },
    "characteristics": [
      {
        "name": "furry"
      },
      {
        "name": "large size"
      }
    ]
  }
```

## Reading the registered animals:

- GET api/animals/
- Status HTTP 200 OK

```JSON
{
    "name": "Frank",
    "age": 5,
    "weight": 34,
    "sex": "male",
    "group": {
      "name": "dog",
      "scientific_name": "canis familiaris"
    },
    "characteristics": [
      {
        "name": "furry"
      },
      {
        "name": "large size"
      }
    ]
  },
  {
    "name": "Max",
    "age": 8,
    "weight": 12,
    "sex": "male",
    "group": {
      "name": "dog",
      "scientific_name": "canis familiaris"
    },
    "characteristics": [
      {
        "name": "short hair"
      },
      {
        "name": "small size"
      }
    ]
  }
```

## Filtering animals:

- GET api/animals/<int:animal_id>/
- Status HTTP 200 OK

```JSON
{
    "id": 2,
    "name": "Max",
    "age": 8,
    "weight": 12,
    "sex": "male",
    "group": {
      "name": "dog",
      "scientific_name": "canis familiaris"
    },
    "characteristics": [
      {
        "name": "short hair"
      },
      {
        "name": "small size"
      }
    ]
  }
```

## Deleting animals:

- DELETE api/animals/<int:animal_id>/
- Status HTTP 204 NO CONTENT

```JSON
// RESPONSE STATUS -> HTTP 204 (no content)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

```bash
python manage.py test -v 2 &> report.txt
```

# Thank's!

## License
[MIT](https://choosealicense.com/licenses/mit/)
