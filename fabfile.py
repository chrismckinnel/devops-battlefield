import boto.ec2

import utils
from fabconfig import *  # noqa


def deploy_challenge(challenge, dev):
    connection = boto.ec2.connect_to_region(
        env.REGION,
        aws_access_key_id=env.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=env.AWS_SECRET_ACCESS_KEY)

    utils.notify('Provisioning new VM')
    reservation = connection.run_instances(
        image_id=env.AMI_IDS[challenge],
        min_count=1,
        max_count=1,
        key_name=env.KEY_NAME,
        security_groups=env.SECURITY_GROUPS,
        user_data=user_data(),
        instance_type=env.INSTANCE_TYPE,
        instance_profile_name=env.INSTANCE_PROFILE_NAME)

    for instance in reservation.instances:
        instance.add_tag('Name', 'devops-battlefield-%s-%s' % (challenge, dev))
    print('Finished provisioning VM')


def deploy_challenges():
    connection = boto.ec2.connect_to_region(
        env.REGION,
        aws_access_key_id=env.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=env.AWS_SECRET_ACCESS_KEY)

    utils.notify('Provisioning new VM for all devs')
    for challenge, dev in env.DEVS.items():
        reservation = connection.run_instances(
            image_id=env.AMI_IDS[challenge],
            min_count=1,
            max_count=1,
            key_name=env.KEY_NAME,
            security_groups=env.SECURITY_GROUPS,
            user_data=user_data(),
            instance_type=env.INSTANCE_TYPE,
            instance_profile_name=env.INSTANCE_PROFILE_NAME)

        for instance in reservation.instances:
            instance.add_tag('Name', 'devops-battlefield-%s-%s' % (challenge, dev))
        print('Created instance: devops-battlefield-%s-%s' % (challenge, dev))
    print('Finished provisioning VM for devs')


def describe_instances():
    connection = boto.ec2.connect_to_region(
        env.REGION,
        aws_access_key_id=env.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=env.AWS_SECRET_ACCESS_KEY)
    reservations = connection.get_all_instances()
    for reservation in reservations:
        for instance in reservation.instances:
            if instance.public_dns_name:
                print('Name: %s, Public DNS: %s' % (instance.tags['Name'], instance.public_dns_name))


def terminate_challenges():
    connection = boto.ec2.connect_to_region(
        env.REGION,
        aws_access_key_id=env.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=env.AWS_SECRET_ACCESS_KEY)

    utils.notify('Terminating challenges')
    reservations = connection.get_all_instances()
    for reservation in reservations:
        instance_ids = [
            instance.id
            for instance in reservation.instances
        ]
        connection.terminate_instances(instance_ids=instance_ids)
    print('Finished terminating challenges')


def user_data():
    with open('user-data.sh', 'r') as user_data_file:
        return user_data_file.read()
