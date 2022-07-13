# from the image file
FROM python:3.7 
# Copy from folder
COPY . /app     
# Working directory
WORKDIR /app
# Run command
RUN pip install -r requirements.txt
# Giving the Port
EXPOSE $PORT
# binding the port passing the command
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app

