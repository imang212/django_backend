FROM python:3.11
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y python3-opencv
COPY . .
WORKDIR /app/todo_project
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "todo_project.wsgi:application"]