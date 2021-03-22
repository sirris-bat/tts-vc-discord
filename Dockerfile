FROM python:3.9.2

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg

RUN pip install pipenv

ENV PROJECT_DIR /usr/local/src/tts_vc_discord

WORKDIR ${PROJECT_DIR}

COPY . ./

RUN pipenv install --system --deploy --ignore-pipfile

CMD [ "python", "-m", "tts-vc-discord" ]
