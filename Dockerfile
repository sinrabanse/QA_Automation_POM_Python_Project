FROM python:3.11-slim

WORKDIR /POM_python_project

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest"]
