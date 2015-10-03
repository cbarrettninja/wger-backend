# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

from django.core.urlresolvers import reverse
from wger.gym.models import Contract

from wger.manager.tests.testcase import WorkoutManagerAccessTestCase, delete_testcase_add_methods
from wger.manager.tests.testcase import WorkoutManagerEditTestCase
from wger.manager.tests.testcase import WorkoutManagerAddTestCase
from wger.manager.tests.testcase import WorkoutManagerDeleteTestCase


class AddDocumentTestCase(WorkoutManagerAddTestCase):
    '''
    Tests uploading a new user document
    '''

    object_class = Contract
    url = reverse('gym:contract:add', kwargs={'user_pk': 14})
    data = {'amount': 30,
            'payment': '2'}
    user_success = ('manager1',
                    'manager2')
    user_fail = ('admin',
                 'general_manager1',
                 'test',
                 'member1',
                 'member2',
                 'member3',
                 'member4',
                 'member5')
