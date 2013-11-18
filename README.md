s3-link
=======

Generate pre-signed urls for S3 objects with expiration.


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
