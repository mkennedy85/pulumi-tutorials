# Use an official Python runtime as a parent image
FROM python:2.7-slim
WORKDIR /app
COPY __main__.py /app
RUN pip install --trusted-host pypi.python.org Flask
ENV NAME World
CMD ["python", "/app/__main__.py"]