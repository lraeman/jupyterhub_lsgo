# jupyterhub_lsgo
Complete working Jupyter Notebook server based off Jupyter/Jupyterhub (https://hub.docker.com/r/jupyterhub/jupyterhub/)

It uses built-in spawner and GitHub OAuth.

Rough step-by-step guide:
<p>In order to use you must first get a valid Domain and registered SSL certificate and key. You can use certbot and noip for example.
<p>Register an OAth application in GitHub to get "CLIENT_ID" and "CLIENT_SECRET"
<p>Update the jupyterhub_config.py file with location of the certificate file. 
<p>Pull/run the docker image. Run jupyter hub using this command: docker run -it -v [location of config file]:/root lraeman:jupyterhub-lsgo bash
<p>In shell of the docker container, 
<p><li>add a new user with the same login name as in GitHub.
<li>update ENV variables with "CLIENT_ID" and "CLIENT_SECRET" values
<li>run "jupyterhub -f [path to jupyterhbu_config.py]"
<p>You should by now login to your jupyterhub domain using GitHub creds and start using Jupyter Notebook
<p>Enjoy!
 



