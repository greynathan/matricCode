FROM python:3.8.5
COPY . /Users/nathangrey/Desktop/matricCode
WORKDIR /Users/nathangrey/Desktop/matricCode
RUN pip install -r requirements.txt
EXPOSE 5150
ENTRYPOINT ["python"]
CMD [ "app.py" ]