"""
A management command which deletes expired accounts (e.g.,
accounts which signed up but never activated) from the database.

Calls ``RegistrationProfile.objects.delete_expired_users()``, which
contains the actual logic for determining which accounts are deleted.

"""

from django.core.management.base import NoArgsCommand
from django_couchdb_utils import auth
from registration_couchdb.models import get_registration_user_data


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        auth.migrate_users(get_registration_user_data)

