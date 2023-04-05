FROM python:3.10-slim

COPY main.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

# Run Python file
CMD ["python3","main.py"]
