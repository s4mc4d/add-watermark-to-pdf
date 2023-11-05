# add-watermark-to-pdf
Quick code to add custom watermark to existing pdf files from a directory


# Prerequisites

Install libraries

```shell
pip install -r requirements.txt
```

# Structure

- config.py : loads environment variables from .env file and makes them available
- watermark.py : generates the watermark as a pdf-ready file. Possible usage alone :

```shell
python watermark.py -p /path/to/new_watermark.pdf
```

- add_watermark.py : main entrypoint for processing a full folder

# Usage

- Copy .env.example to .env
- Put all pdf files inside a known directory, say "input_dir"
- Fill in the variables inside the .env file
- Launch command :

```shell
python add_watermark.py
```
