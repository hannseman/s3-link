s3-link
=======

Generate urls for pre-signed S3 object urls with expiration.


Installation:

~~~ sh
$ python setup.py install
~~~

Usage: 
~~~ sh
s3-link -f manifest.plist --key [bucket] --secret [secret] --bucket [bucket] --expires 72
~~~

Expiry time defaults to 24 hours.

Additional information:
~~~ sh
s3-link --help
~~~
