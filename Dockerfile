FROM ubuntu

RUN mkdir -p /tests

COPY requirements.txt /tests/requirements.txt

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    mc \
    unzip \
    software-properties-common \
    xvfb \
    fonts-liberation \
    libnss3 \
    libnspr4 \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatspi2.0-0 \
    libgtk-3-0 \
    libxtst6 \
    libxss1 \
    lsb-release \
    xdg-utils \
    apt-utils \
    nano \
    libgconf-2-4 \
    locales \
    python3-setuptools \
    python3-pip \
    language-pack-ru \
    antiword \
    && pip3 install --upgrade --isolated  pip

RUN pip3 install -r /tests/requirements.txt

# Установка русской кодировки
ENV LANGUAGE ru_RU.UTF-8
ENV LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8
RUN locale-gen ru_RU.UTF-8 && dpkg-reconfigure locales

# Установка Хрома
RUN curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /chrome.deb
RUN dpkg -i /chrome.deb || apt-get install -yf
RUN rm /chrome.deb

RUN cd /tmp && wget "https://chromedriver.storage.googleapis.com/80.0.3987.16/chromedriver_linux64.zip"  && unzip chromedriver_linux64.zip && mv /tmp/chromedriver /usr/bin/ && chmod a+x /usr/bin/chromedriver

ENV PYTHONPATH $PYTHONPATH:/tests
WORKDIR /tests

RUN apt-get clean && apt-get -y autoremove && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/ /usr/share/man/

