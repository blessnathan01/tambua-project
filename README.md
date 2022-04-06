# TambuaBot project (Back-end)

## Introduction

This is my final year project (FYP) environment with all necessary files for the FYP to be done. 

FYP Title: Child Violence Awareness and Reporting System (Chatbot)
FYP Description: The project is all about developing a ChatBot named Tavio which tries to answer any question pertaining to Child Violence. Tavio will be using Swahili language.
Methodology used: Human Centered Design (HCD) 
Language used: Python 3.8.8
Libraries used: Natural Language Processing (NLP) libraries
Modules used: chatterbot with a ChatBot, ListTrainer (from chatterbot.trainers)
Version: 1

## Get Started with Chatbots

### Consider the following steps to get started with Rasa chatbots:
1. Install Anaconda (latest version)
2. Open Anaconda prompt
3. Create a folder for your project
4. Enter into the folder you created
5. Create an environment, say my_env, by running the following command into the anaconda prompt: conda create --name my_env
6. Activate the created environment by running the following command into the anaconda prompt: conda activate my_env
7. Install ujson that enables dependencies installation by running the following command into the anaconda prompt: conda install ujson
8. Install tensorflow that enables ML libraries installation by running the following command into the anaconda prompt: conda install tensorflow
9. Install rasa by running the following command into the anaconda prompt: pip install rasa
10. Intiate rasa by running the following command into the anaconda prompt: rasa init
11. Train the model by running the following command into the anaconda prompt: rasa train nlu
12. Chat with bot using command line interface to see its intent and confidence by running the following command into the anaconda prompt: rasa shell nlu

## Get Started with Rasa X

### Consider the following steps to get started with Rasa X:
1. Downgrade pip by running the following command into the anaconda prompt: pip install --upgrade pip==20.2
2. Check the version of pip by running the following command into the anaconda prompt: pip -V
3. Install ujson by running the following command into the anaconda prompt: conda install ujson==1.35
4. Install rasa x by running the following command into the anaconda prompt: pip install -U rasa-x --extra-index-url https://pypi.rasa.com/simple
5. Start rasa x server by running the following command into the anaconda prompt: rasa x
6. Agree to the license agreement and terms
7. Rasa X server is up, you're good to go :)

## Deploy rasa chatbot to Heroku using docker on Ubuntu

### Consider the following steps to deploy Rasa chatbot to Heroku using docker on Ubuntu 20.04:
1. [Log into Heroku](https://id.heroku.com/login) by running the following command into the terminal: heroku login
2. Add all file to the heroku git by running the following command into the terminal: git add -A
3. Commit the changes by running the following command into the terminal: git commit -m "changes were made"
4. Login into docker container by running the following command into the terminal: sudo docker login --username=_ --password=$(heroku auth:token) registry.heroku.com
5. Push the docker container into heroku by running the following command into the terminal: sudo /snap/bin/heroku container:push web
6. Release the docker container by running the following command into the terminal: sudo /snap/bin/heroku container:release web
7. The rasa chatbot is deployed and you're good to access it through heroku api for example https://app-name.herokuapp.com/webhooks/rest/webhook

Author: Blessing Nathaniel Rweikiza
Bio: Rasa Chatbot Developer | Flutter Developer | Software Engineer

Copyright 2020-2021
