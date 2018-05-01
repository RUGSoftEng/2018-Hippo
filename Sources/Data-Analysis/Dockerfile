FROM java:8 

RUN apt-get update
RUN apt-get install -y maven

WORKDIR /code

ADD data-streamer/pom.xml /code/pom.xml
RUN ["mvn", "dependency:resolve"]
RUN ["mvn", "verify"]

ADD data-streamer /usr/src
RUN ["mvn", "package"]

ADD data-streamer /code

CMD tail -f /dev/null