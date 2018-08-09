FROM jupyterhub/jupyterhub

RUN apt-get update --yes 
RUN pip install --upgrade pip
RUN pip install oauthenticator notebook pandas elasticsearch netaddr np
RUN adduser -q --disabled-password --disabled-login --gecos "" lraeman

EXPOSE 443 80 22