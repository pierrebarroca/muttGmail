muttGmail
=========

Command line tool to configure your Gmail on mutt with pgp encryted password.

Usage
-----

usage: muttGmail.py [-h] [--f F] username name

positional arguments:
  -username    Gmail username: <username>.gmail.com
  -name        Real user name. ex: "John Doe"

optional arguments:
  -h, --help  show this help message and exit
  --f F       path for password file. Default: ~/.mutt/passwd.pgp

Example: 

.. code-block:: bash

   python muttGmail pi.barroca "Pierre Barroca" --f ~./mutt/passwd.pgp
   
Installation
------------

.. code-block:: bash

  git clone git@github.com:pierrebarroca/muttGmail.git

Requirements
^^^^^^^^^^^^

* `GNU Privacy Guard (GnuPG/GPG) <https://www.gnupg.org/>`_ `
* `Mutt E-mail client <http://www.mutt.org/>`_ `


Licence
-------

Authors
-------

`muttGmail` was written by `Pierre Barroca <pi.barroca@gmail.com>`_.
