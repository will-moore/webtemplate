OMERO.webtemplate
===============
This is a django app for the OMERO.web framework that you can use to get you started with your own code.

Requirements
============

* OMERO 4.4.0 or later

Development Installation
========================

Clone the repository in to your OMERO.web installation:

    cd components/tools/OmeroWeb/omeroweb/
    git clone git://github.com/will-moore/webtemplate.git
    path/to/bin/omero config set omero.web.apps '["webtemplate"]'
    cd webtemplate
    git status    # you can now commit etc.