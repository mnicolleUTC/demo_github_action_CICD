FROM python:3.10-slim

COPY main.py .

# Run Python file
CMD ["python3","main.py"]
