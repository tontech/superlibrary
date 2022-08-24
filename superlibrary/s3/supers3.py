# AUTHOR: nmacatangay

from boto.s3.key import Key
import boto
import os

def connect_to_amazon(key, secret):

    # CONNECT TO AMAZON S3
    amazon = boto.connect_s3(key, secret)

    return amazon

def disconnect_from_amazon(amazon):

    # DISCONNECT FROM AMAZON
    amazon.close

    return None

def connect_to_s3_bucket(name, amazon):

    # CONNECT TO AMAZON S3 BUCKET
    bucket = amazon.get_bucket(name, validate=True)

    return bucket

def download(
        bucket,
        bucket_file,
        download_path,
        headers={}):

    key = Key(bucket, bucket_file)
    try:
        key.get_contents_to_filename(download_path, headers)
    except:
        nothing = 1

    return None

def upload(
        bucket,
        bucket_file,
        file,
        callback=None,
        md5=None,
        reduced_redundancy=False,
        content_type=None):

    # GET FILESIZE FOR FINAL VALIDATION 
    try:
        size = os.fstat(file.fileno()).st_size
    except:
        file.seek(0, os.SEEK_END)
        size = file.tell()

    # DEFINE KEY
    bucket_key = Key(bucket)
    bucket_key.key = bucket_file

    # SPECIFY METADATA IF CONTENT TYPE IS NOT NONE
    if content_type:
        bucket_key.set_metadata("Content-Type", content_type)

    # START UPLOAD
    sent = bucket_key.set_contents_from_file(
            file,
            cb=callback,
            md5=md5,
            reduced_redundancy=reduced_redundancy,
            rewind=True)

    # REWIND FOR LATER USE
    file.seek(0)

    retval = False
    if sent == size:
        retval = True

    return retval

def delete(bucket, bucket_file):

    # DEFINE KEY
    bucket_key = Key(bucket)
    bucket_key.key = bucket_file

    # DELETE FILE
    bucket_key.delete
