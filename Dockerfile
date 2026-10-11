FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1\
    PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

ENV PORT=9000

EXPOSE 9000

# Start the application using Gunicorn
CMD ["gunicorn", "helpdesk_it_admin.wsgi:application", "--bind", "0.0.0.0:9000"]