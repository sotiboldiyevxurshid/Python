

# Base image
FROM python:3.8

# Set working directory
WORKDIR /app

# Copy the application code

COPY . .

RUN pip freeze > requirements.txt
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2
# Command to run the application
CMD [ "python", "index.py" ]