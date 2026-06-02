FROM ubuntu:latest
LABEL authors="szymonkaletka"

ENTRYPOINT ["top", "-b"]