#Github OAuth Config
from oauthenticator.github import GitHubOAuthenticator
c.JupyterHub.authenticator_class = GitHubOAuthenticator
c.JupyterHub.authenticator_class.oauth_callback_url = 'https://[your registered FQDN]/hub/oauth_callback'
c.JupyterHub.authenticator_class.client_id  = '[get client id from GitHub]'
c.JupyterHub.authenticator_class.client_secret = '[get client secret from GitHub]'

#/root binds to docker host diretory where 'jupyterhub_config.py' and '*.pem' files can be stored
#Argument option used in docker run: '-v [host folder path contain]:/root
#Argument option used in docker run: '-p 443:443
c.JupyterHub.port = 443
c.JupyterHub.ssl_key = '/root/privkey.pem' #generated using certbot   
c.JupyterHub.ssl_cert = '/root/cert.pem'   #generated using certbot
c.Authenticator.whitelist = {'lraeman'}
c.Authenticator.admin_users = {'lraeman'}
c.JupyterHub.ip = '0.0.0.0'             #all interface IPs
c.JupyterHub.hub_ip = '0.0.0.0'         #all interface IPs    
c.JupyterHub.hub_connect_ip = '0.0.0.0' #all interface IPs            
c.JupyterHub.cookie_secret_file = '/opt/conda/share/jupyterhub/jupyterhub_cookie_secret'
c.Spawner.notebook_dir = '/root/notebooks'