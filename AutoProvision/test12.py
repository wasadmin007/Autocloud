import boto3

region = 'us-east-2'
ec2 = boto3.client('ec2',region)
azs = ec2.describe_availability_zones(Filters=[
        {
            'Name': 'region-name',
            'Values': [
                region,
            ]
        },
    ],)
cho = []
for key  in azs['AvailabilityZones']:
       cho.append((key['ZoneName'],key['ZoneName']),)
print cho
