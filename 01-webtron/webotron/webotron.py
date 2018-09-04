import boto3
import click

session = boto3.Session(profile_name='logic')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('lb')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('lbo')
@click.argument('bucketname')
def list_bucket_objects(bucketname):
    "List objects in an s3 bucket"
    for obj in s3.Bucket(bucketname).objects.all():
        print(obj)

if __name__=='__main__':
    cli()
