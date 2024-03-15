# jupyter-mentor
A chatbot to coach you through learning new things in Jupyter Notebooks

## Developing on MacOS

1. Install Docker with `brew install --cask docker`. If this command does not work, you may need to [install Homebrew](https://brew.sh/)
2. Start Docker by clicking on application icon or by running `open -a Docker`
3. Pull the docker image from DockerHub to you local machine using `docker image pull brewer36/jupyter-mentor:macos`
4. `cd <location_of_your_clone>` 
5. Launch JupyterLab with `docker run -it --rm -p 8888:8888 brewer36/jupyter-mentor:macos jupyter lab --ip=0.0.0.0 --port=8888`

## Updating brewer36/jupyter-mentor:latest (linux) image with GitHub acitons
No extra steps required. This GitHub action automatically updates the image with each new commit.

## Updating brewer36/jupyter-mentor:macos (arm64 for M1 chip) image with repo2docker

1. Install repo2docker with `python3 -m pip install jupyter-repo2docker`
2. `cd <location_of_your_clone>` 
3. `repo2docker --Repo2Docker.platform=linux/arm64 --image-name=brewer36/jupyter-mentor:macos ./` 

Note: I probably need to make a group DockerHub account so that others can also update the image. Or at least to trigger an email when the environment configurations files have been changed and need to be updated locally. 
