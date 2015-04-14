iosr-crawler
============

Semantic web crawler developed during Software Engineering of Distributed Systems course at AGH university of Science 
and Technology, Cracow 2015.

Prerequisites
-------------

* python 2.7
* pip
* virtualenv 

Requirements
------------

The list of requirements is presented below. It is an output of `pip freeze` command run in virtual environment.

* Django==1.8
* oauthlib==0.7.2
* PyJWT==1.0.1
* python-openid==2.2.5
* python-social-auth==0.2.5
* requests==2.6.0
* requests-oauthlib==0.4.2
* six==1.9.0

Architecture
------------

We distinguish three main parts in our system:

* user interface implemented using Django framework
* web crawler build on `Scrupy` library
* natural language processor using nltk library enables semantic recognition

User authentication is achieved with OAuth2 standard and third party providers.
In order to store crawling results distributed Raik database is used.