from django.urls import path

from . import views

app_name = 'judge'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('courses/', views.CourseListView.as_view(), name='courses'),
    path('course/add/', views.CourseCreate.as_view(), name='course_create'),
    path('course/<int:course_pk>/update/', views.CourseUpdate.as_view(), name='course_update'),
    path('course/<int:course_pk>/students/add', views.CourseAddStudents.as_view(), name='course_add_students'),
    path('course/<int:course_pk>/delete/', views.CourseDelete.as_view(), name='course_delete'),
    path('course/<int:course_pk>/problems/', views.ProblemListView.as_view(), name='problems'),
    path('course/<int:course_pk>/grades/', views.CourseGrades.as_view(), name='course_grades'),
    path('course/<int:course_pk>/grades.csv', views.course_grades_csv, name='course_grades_csv'),
    path('course/<int:course_pk>/students/', views.StudentListView.as_view(), name='students'),
    path('course/<int:course_pk>/students/remove/', views.remove_user, name='remove_users'),
    path('course/<int:course_pk>/problem/add/', views.ProblemCreate.as_view(), name='problem_create'),
    path('course/<int:course_pk>/problem/<int:problem_pk>/update/',
         views.ProblemUpdate.as_view(), name='problem_update'),
    path('course/<int:course_pk>/problem/<int:problem_pk>/delete/',
         views.ProblemDelete.as_view(), name='problem_delete'),
    path('course/<int:course_pk>/problem/<int:problem_pk>/', views.ProblemDetailView.as_view(), name='detail'),
    path('course/<int:course_pk>/problem/<int:problem_pk>/solution/<int:solution_pk>/source/',
         views.SourceCodeView.as_view(), name='source_code'),
    path('course/<int:course_pk>/problem/<int:pk>/grades/', views.ProblemGradesView.as_view(), name='problem_grades'),
    path('course/<int:course_pk>/problem/<int:problem_pk>/tests/',
         views.TestCaseView.as_view(), name='test_cases'),
    path('course/<int:course_pk>/problem/<int:problem_pk>/test/add/',
         views.TestCaseCreate.as_view(), name='test_case_create'),
    path('course/<int:course_pk>/problem/<int:problem_pk>/test/<int:test_case_pk>/update/',
         views.TestCaseUpdate.as_view(), name='test_case_update'),
    path('course/<int:course_pk>/problem/<int:problem_pk>/test/<int:test_case_pk>/delete/',
         views.TestCaseDelete.as_view(), name='test_case_delete'),
    path('course/<int:course_pk>/problem/<int:problem_pk>/solution/<int:solution_pk>/download/',
         views.download_solution, name='download_solution'),
    path('course/<int:course_pk>/problem/<int:problem_pk>/solutions/download/',
         views.download_all_solutions, name='download_all_solutions'),
    path('course/<int:course_pk>/problem/<int:problem_pk>/solution/send/', views.send_solution, name='send'),
]
