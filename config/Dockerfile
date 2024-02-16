FROM python:3.12.1

ENV APPNAME=ai-sandbox
ENV HOME_FOLDER=/workspaces/$APPNAME
WORKDIR $HOME_FOLDER
ENV TEMPFOLDER=/tmp/mytmp

# Provide python packages
COPY ./config/requirements.txt $TEMPFOLDER/requirements.txt

# -------------------------------------------------------------------------------------------------
## Install necessary packages to donwload and install tools
# -------------------------------------------------------------------------------------------------
# Install Terraform CLI
RUN apt-get update && apt-get install -y gnupg software-properties-common jq curl unzip 
# Install all python packages
RUN    pip install --upgrade pip \ 
    && pip install --no-cache-dir -r $TEMPFOLDER/requirements.txt

CMD ["bash"]
