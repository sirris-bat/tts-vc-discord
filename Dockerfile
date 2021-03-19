FROM python:3.9

RUN pip install pipenv

ENV PROJECT_DIR /usr/local/src/tts_vc_discord

WORKDIR ${PROJECT_DIR}

COPY . ./

RUN pipenv install --system --deploy --ignore-pipfile

CMD [ "python", "-m", "tts-vc-discord" ]
