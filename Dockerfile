# Use a lightweight Python image
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install python-dotenv
CMD ["python", "pipeline.py"]