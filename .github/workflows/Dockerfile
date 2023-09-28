FROM python:3.9.7

RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN groupadd -g 799 siyingchen && \
    useradd -r -u 999 -g siyingchen siyingchen

# Set up a working folder and install the pre-reqs
WORKDIR /app

RUN pip install Flask

USER siyingchen

COPY --chown=siyingchen:siyingchen . .

CMD [ "python", "./run.py" ]



