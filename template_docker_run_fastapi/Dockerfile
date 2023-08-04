FROM python:latest

# Set working directory
WORKDIR /app

# Install all dependencies
# This structure is best because all time you change the codes, the dependencies wount be updated
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy all files
COPY . /app

# Start server and expose port
CMD uvicorn main:app --host 0.0.0.0 --port 80