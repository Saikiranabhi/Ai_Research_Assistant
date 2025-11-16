FROM python:3.11-slim

WORKDIR /app

# copy project files
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# environment variables should be provided at runtime (or via .env)
CMD ["python", "app.py"]
