import os
import boto.ec2
import logging

from django.conf import settings

logger = logging.getLogger('devops.user')


def create_instance(user):
    connection = boto.ec2.connect_to_region(
        settings.REGION,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

    logger.info('Provisioning new VM')
    reservation = connection.run_instances(
        image_id=settings.AMI_ID,
        min_count=1,
        max_count=1,
        key_name=settings.KEY_NAME,
        security_groups=settings.SECURITY_GROUPS,
        user_data=user_data(),
        instance_type=settings.INSTANCE_TYPE,
        instance_profile_name=settings.INSTANCE_PROFILE_NAME)

    for instance in reservation.instances:
        instance.add_tag('Name', 'devops-battlefield-%s' % user.email)
    logger.info('Finished provisioning instance for %s' % user.email)


def user_data():
    script_location = os.path.join(
        settings.PROJECT_ROOT, 'devops/user/scripts/user_data.sh')
    with open(script_location, 'r') as user_data_file:
        return user_data_file.read()
