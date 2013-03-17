from django.conf.urls import patterns, url
from django.contrib.auth.decorators import permission_required

from wger.exercises.views import exercises
from wger.exercises.views import comments
from wger.exercises.views import categories

urlpatterns = patterns('wger.exercises.views',

    # Exercises
    url(r'^overview/$', 'exercises.exercise_overview'),

    url(r'^muscle/overview/$',
        exercises.MuscleListView.as_view(),
        name='muscle-overview'),
    url(r'^search/$', 'exercises.exercise_search'),
    url(r'^(?P<id>\d+)/view/(?P<slug>[-\w]+)/$', 'exercises.exercise_view'),
    url(r'^(?P<id>\d+)/view/$', 'exercises.exercise_view'),
    url(r'^add/$',
        permission_required('exercises.change_exercise')(exercises.ExerciseAddView.as_view()),
        name='exercise-add'),
    url(r'^(?P<pk>\d+)/edit/$',
        permission_required('exercises.change_exercise')(exercises.ExerciseUpdateView.as_view()),
        name='exercise-edit'),
    url(r'^(?P<pk>\d+)/delete/$',
        permission_required('exercises.change_exercise')(exercises.ExerciseDeleteView.as_view()),
        name='exercise-delete'),

    # Comments
    url(r'^(?P<exercise_pk>\d+)/comment/add/$',
        permission_required('exercises.change_exercise')(comments.ExerciseCommentAddView.as_view()),
        name='exercisecomment-add'),
    url(r'^comment/(?P<pk>\d+)/edit/$',
        permission_required('exercises.change_exercise')(comments.ExerciseCommentEditView.as_view()),
        name='exercisecomment-edit'),
    url(r'^comment/(?P<id>\d+)/delete/$',
        'comments.exercisecomment_delete',
        name='exercisecomment-delete'),

    # Categories
    url(r'^category/(?P<pk>\d+)/edit/$',
        permission_required('exercises.change_exercise')(categories.ExerciseCategoryUpdateView.as_view()),
        name='exercisecategory-edit'),
    url(r'^category/add/$',
        permission_required('exercises.change_exercise')(categories.ExerciseCategoryAddView.as_view()),
        name='exercisecategory-add'),
    url(r'^category/(?P<pk>\d+)/delete/$',
        permission_required('exercises.change_exercise')(categories.ExerciseCategoryDeleteView.as_view()),
        name='exercisecategory-delete'),
)
