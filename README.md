# Twibbon Find IT! 2023

Ini merupakan repo ML API untuk pengecekan twibbon peserta Find IT!.

<br>

## Prerequisite

- python3.10
- python3.10-venv

Create python virtual environment ex; python-venv, python-virtualenv etc.
Type script on active directories

```sh
$ virtualenv -m venv
```

Activate your python environment
```sh
$ source bin/activate
(venv)$ 
```

Install dependencies.
```sh
(venv)$ pip install -r requirements.txt
```

## Activate FastApi

```sh
(venv)$ python src/main.py
```

Access at `http://0.0.0.0:8000/docs/`

**Input instagram format** 

`https://www.instagram.com/p/Co3XdlDBqQx/`
`https://www.instagram.com/p/Co3XdlDBqQx`

**Curl Example**

```sh
curl -X 'POST' \
  'http://10.211.55.3:8000/v1/predict/tf/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "category": "string",
  "img_url": ["https://www.instagram.com/p/Co4mP5nBQ6B/", "https://www.instagram.com/p/Co4mNvrh_lv/", "https://www.instagram.com/p/Co4mKhWh-MK/", "https://www.instagram.com/p/Co3XkbyBQ9H/"]
}'
```