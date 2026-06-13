FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt  
#(-r Read package names from requirements.txt)
#--no-cache-dir gives smaller docker image by deleting temporary files

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


