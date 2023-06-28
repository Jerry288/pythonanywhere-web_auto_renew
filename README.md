# Web service auto renewer for pythonanywhere

Have you always been bugged that you need to renew your web server in pythonanywhere or it would be deactivated, well worry no more. With this simple code, you will be able to renew it automatically.

## How to setup

### With executables (recommended)

1. Install the latest release executable for your operating system.
2. Install the template auth.json file.
3. Open and edit the auth.json to include your credentials.
4. Have the executable run on startup.

When using the executable for Mac or Linux, run `chmod -x renewer-mac` (or Linux) and `chmod -r auth.json`. Due to strict restrictions with macOS executables, the executable must run with sudo permissions. This is why it is recommended to use Python or docker to run the renewer on mac instead.

### With python

1. Install git if you haven't already.
2. Clone repository using `git clone https://github.com/Jerry288/pythonanywhere-web_auto_renew.git`
3. Edit auth.json to add your credentials
4. If you're on Windows, make [wrapper.bat](wrapper.bat) run on startup, if you're on macOS or a Unix operating system (such as Linux) make [wrapper.sh](wrapper.sh) run on startup.

### With docker

1. Install git if you haven't already.
2. Clone repository using `git clone https://github.com/Jerry288/pythonanywhere-web_auto_renew.git`
3. Edit auth.json to add your credentials.
4. Run the docker-daemon
5. In your terminal, navigate to the repository you just cloned and run `docker build . --tag pythonanywhere-renewer`
6. Have the command `docker run pythonanywhere-renewer` run on startup.

## How it works

1. The main script [renewer.py](renewer.py) makes a get request to the login page of pythonanywhere. It retrieves the csrf token and session id.
2. It then uses these parameters to log in.
3. It retrieves a new session id and then uses that to go to the renew server endpoint


## License

The license can be found [here](LICENSE).

If you use or remix this software, please provide proper attribution to the original creator:

- Include the name of the software: pythonanywhere-web_auto_renewer
- Mention the original creator: Wei-Jie (Jerry) Lin
- Provide a link to the original repository: https://github.com/Jerry288/pythonanywhere-web_auto_renew

Thank you for giving credit to the original work!
