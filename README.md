# Web service auto renewer for pythonanywhere

Have you always been bugged that you need to renew your web server in pythonanywhere or it would be deactivated, well worry no more. With this simple code, you will be able to renew it automatically.

## How to setup

1. Install git if you haven't already.
2. Clone repository using `git clone https://github.com/Jerry288/pythonanywhere-web_auto_renew.git`
3. Edit auth.json to add your credidentials
3. If you're on windows, make [wrapper.bat](wrapper.bat) run on startup, if you're on macOS or a Unix operating system (such as linux) make [wrapper.sh](wrapper.sh) run on startup.

If you want, you may use docker. The dockerfile is provided.

## How it works

1. The main script [renewer.py](renewer.py) makes a get request to the login page of pythonanywhere. It retrieves the csrf token and session id.
2. It then uses the these params to login.
3. It retrieves a new session id and them uses that to go to the renew server endpoint


## License

The license can be found [here](LICENSE).

If you use or remix this software, please provide proper attribution to the original creator:

- Include the name of the software: pythonanywhere-web_auto_renewer
- Mention the original creator: Wei-Jie (Jerry) Lin
- Provide a link to the original repository: https://github.com/Jerry288/pythonanywhere-web_auto_renew

Thank you for giving credit to the original work!