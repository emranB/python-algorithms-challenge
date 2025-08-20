# Python Challenge

## How to run

### Option 1: Run locally with Python
```bash
python -m __main__.py
```

### Option 2: Run in Docker
```bash
docker build -t python-challenge .
docker run --rm -it python-challenge
```

### Expected Results

The script validates all questions and prints which ones pass. Typical output:
```bash
question 1 has passed
question 2 has passed
question 3 has passed
question 4 has passed
question 5 has passed
```

Then it waits for Enter to exit.

