from django.urls import path
from .views import counsellor_list_page, login_user, logout_user, student_profile, counsellor_profile, user_type_page, approval_waiting, student_list_page, my_counsil_page, my_profile_page, my_counsil_profile, student_counselling_page, college_branch_page, f_a_q_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', counsellor_list_page, name='home_page'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('user_type/', user_type_page, name='user_type'),
    path('student_profile/', student_profile, name='student_profile'),
    path('counsellor_profile/', counsellor_profile, name='counsellor_profile'),
    path('approval_waiting', approval_waiting, name='approval_waiting'),
    path('students_list', student_list_page, name='students_list'),
    path('student_counsil_page/<str:pk>/',
         student_counselling_page, name='student_counsil_page'),
    path('my_counsil_page/', my_counsil_page, name='my_counsil_page'),
    path('my_counsil_profile/', my_counsil_profile, name='my_counsil_profile'),
    path('my_profile_page/', my_profile_page, name='my_profile_page'),
    path('college_and_branch/', college_branch_page, name='college_and_branch'),
    path('frequently_asked_questions/', f_a_q_page,
         name='frequently_asked_questions'),
    #     path('video_api/', video_api,
    #          name='video_api'),




]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
