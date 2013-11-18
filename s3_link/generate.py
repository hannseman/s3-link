#!/usr/bin/env python
from boto.s3.connection import S3Connection
from optparse import OptionParser
from datetime import datetime, timedelta
import s3_link


def main():
    usage = "Usage: %prog [options] [action]..."

    parser = OptionParser(usage, version="%%prog v%s" % s3_link.__version__)

    parser.add_option("-f", "--file",
                      dest="file",
                      default="",
                      help="S3 object path")

    parser.add_option("-k", "--key",
                      dest="key",
                      default="",
                      help="S3 access key")

    parser.add_option("-s", "--secret",
                      dest="secret",
                      default="",
                      help="S3 secret")

    parser.add_option("-b", "--bucket",
                      dest="bucket",
                      default="",
                      help="S3 bucket")

    parser.add_option("-t", "--expires",
                      dest="expires",
                      default="24",
                      help="Expire time in hours")

    parser.add_option("-c", "--content-type",
                      dest="content_type",
                      default="text/plain",
                      help="Content type")

    ### Parse command line
    (options, args) = parser.parse_args()

    ### Validate required input
    if not options.key:
        parser.error('--key is required')
    if not options.file:
        parser.error('--file is required')
    if not options.secret:
        parser.error('--secret is required')
    if not options.bucket:
        parser.error('--bucket is required')
    options = vars(options)

    # Create S3 connection
    connection = S3Connection(
        aws_access_key_id=options['key'],
        aws_secret_access_key=options['secret'])

    # Handle expire
    expires = int(options['expires'])
    expires_seconds = expires * 60 * 60  # convert to seconds
    expire_date = datetime.now() + timedelta(hours=expires)

    # Generate URL
    url = connection.generate_url(
        expires_seconds,
        'GET',
        options['bucket'],
        options['file'],
        response_headers={
            'response-content-type': options['content_type']
        }
    )
    print '######## GENERATED URL (EXPIRE %s) ########' % expire_date
    print url
    print '######## END GENERATED URL ########'

if __name__ == "__main__":
    main()
