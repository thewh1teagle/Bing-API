# Bing-API

Unofficial `API` for Bing in Python

## What is Bing-API?
Bing `API` is set of `Libraries` for Using AI related `API's` of `Bing` developed by `Microsoft`

## Features
- Create Images using [Dall-E 3](https://www.bing.com/create)

## Install
```shell
pip install -U api4bing
```

## Usage
```python
from bingapi import BingAPI

api = BingAPI()
images = api.create_images("Blue screen of windows")
for index, image in enumerate(images):
    image.save(f'image-{index}.jpg')
```

## Telegram Bot
You can spawn your own Telegram bot which will allow creating images
see `telegram_bot` folder.