FROM python:3.10-slim

# Copy file into the container
COPY main.py . 

# Run Python file
CMD ["python3","main.py"]
