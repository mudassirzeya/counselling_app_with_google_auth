from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import UserProfile, StudentExtendedProfile, CounsellorExtendedProfile, Comment, Frequestly_Asked_Question
from django.shortcuts import get_object_or_404
from .forms import CommentForm
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from PIL import Image
from councelling_app.settings import UPLOAD_IMAGE_URL
import requests


# Create your views here.


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("user", password, username)
        user = authenticate(request, username=username, password=password)
        print("us", user)
        if user is not None:
            login(request, user)
            # staffProfile = UserProfile.objects.get(user=user)
            # usertype = staffProfile.user_type
            # if usertype == 'admin':
            #     return redirect('admin_page')
            # elif usertype == 'law':
            return redirect('home_page')
        else:
            messages.info(request, 'Username or Password is in correct')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def user_type_page(request):
    user = request.user
    try:
        staffProfile = UserProfile.objects.get(user=user)
    except Exception:
        staffProfile = None

    try:
        usertype = staffProfile.user_type
    except Exception:
        usertype = None
    if usertype:
        if usertype == 'student':
            return redirect('/')
        elif usertype == 'counsellor':
            return redirect('/')
    else:
        context = {}
        return render(request, "user_type.html", context)


@login_required(login_url='login')
def counsellor_list_page(request):
    user = request.user
    counsellor = CounsellorExtendedProfile.objects.all()
    try:
        staffProfile = UserProfile.objects.get(user=user)
    except Exception:
        staffProfile = None
    try:
        usertype = staffProfile.user_type
    except Exception:
        usertype = None
    context = {'staffprofile': staffProfile, 'counsellor': counsellor}
    if usertype:
        if usertype == 'student':
            if staffProfile.user_status == 'approved':
                return render(request, "home.html", context)
            else:
                return redirect('approval_waiting')
        elif usertype == 'counsellor':
            if staffProfile.user_status == 'approved':
                return render(request, "home.html", context)
            else:
                return redirect('approval_waiting')
    else:
        return redirect('user_type')
    return render(request, "home.html", context)


@login_required(login_url='login')
def student_list_page(request):
    user = request.user
    student = StudentExtendedProfile.objects.all()
    try:
        staffProfile = UserProfile.objects.get(user=user)
    except Exception:
        staffProfile = None
    try:
        usertype = staffProfile.user_type
    except Exception:
        usertype = None

    context = {'staffprofile': staffProfile, 'students': student}
    if usertype:
        if usertype == 'student':
            if staffProfile.user_status == 'approved':
                return render(request, "students_list_page.html", context)
            else:
                return redirect('approval_waiting')
        elif usertype == 'counsellor':
            if staffProfile.user_status == 'approved':
                return render(request, "students_list_page.html", context)
            else:
                return redirect('approval_waiting')
    else:
        return redirect('user_type')
    return render(request, "students_list_page.html", context)


# @login_required(login_url='login')
# def student_comment_page(request, pk):
#     student_profile = StudentExtendedProfile.objects.get(id=pk)
#     staffProfile = UserProfile.objects.get(user=student_profile.user.user)

#     context = {'student_profile': student_profile,
#                'staffprofile': staffProfile}
#     return render(request, 'student_comment_page.html', context)


@login_required(login_url='login')
def my_counsil_page(request):
    user = request.user
    try:
        staffProfile = UserProfile.objects.get(user=user)
    except Exception:
        staffProfile = None
    try:
        usertype = staffProfile.user_type
    except Exception:
        usertype = None
    my_profile = StudentExtendedProfile.objects.get(user=staffProfile)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            reply_obj = None
            try:
                reply_id = int(request.POST.get('reply_id'))
            except:
                reply_id = None
            if reply_id:
                reply_obj = Comment.objects.get(id=reply_id)

            # author = form.cleaned_data['author']
            comment = form.cleaned_data['content']
            if reply_obj:
                Comment(content=comment,
                        parent=reply_obj, comment_to=my_profile, commented_by=staffProfile).save()
            else:
                Comment(content=comment,
                        comment_to=my_profile, commented_by=staffProfile).save()
            return redirect('my_counsil_page')
    else:
        form = CommentForm()
    counsellors = CounsellorExtendedProfile.objects.all()
    comments = Comment.objects.filter(
        comment_to=my_profile, parent=None).order_by('date_posted')
    context = {
        'post': my_profile,
        'form': form,
        'comments': comments,
        'my_profile': my_profile, 'staffprofile': staffProfile,
        'counsellors': counsellors
    }
    # context = {'staffprofile': staffProfile, 'my_profile': my_profile}
    if usertype:
        if usertype == 'student':
            if staffProfile.user_status == 'approved':
                return render(request, "my_counsil_page.html", context)
            else:
                return redirect('approval_waiting')
        elif usertype == 'counsellor':
            if staffProfile.user_status == 'approved':
                return redirect('students_list')
            else:
                return redirect('approval_waiting')
    else:
        return redirect('user_type')
    return render(request, 'my_counsil_page.html', context)


@login_required(login_url='login')
def my_counsil_profile(request):
    user = request.user
    try:
        staffProfile = UserProfile.objects.get(user=user)
    except Exception:
        staffProfile = None
    try:
        usertype = staffProfile.user_type
    except Exception:
        usertype = None
    my_profile = StudentExtendedProfile.objects.get(user=staffProfile)
    context = {'staffprofile': staffProfile, 'my_profile': my_profile}
    if request.method == 'POST':
        full_name = request.POST.get('name')
        college = request.POST.get('college')
        rank = request.POST.get('rank')
        description = request.POST.get('description')

        staffProfile.fullname = full_name
        staffProfile.save()

        my_profile.prepared_from = college
        my_profile.rank = rank
        my_profile.description = description
        my_profile.save()
        return redirect('my_counsil_page')

    if usertype:
        if usertype == 'student':
            if staffProfile.user_status == 'approved':
                return render(request, "my_counsil_page.html", context)
            else:
                return redirect('approval_waiting')
        elif usertype == 'counsellor':
            if staffProfile.user_status == 'approved':
                return redirect('students_list')
            else:
                return redirect('approval_waiting')
    else:
        return redirect('user_type')
    return render(request, 'my_counsil_page.html', context)


@login_required(login_url='login')
def my_profile_page(request):
    user = request.user
    try:
        staffProfile = UserProfile.objects.get(user=user)
    except Exception:
        staffProfile = None
    try:
        usertype = staffProfile.user_type
    except Exception:
        usertype = None
    try:
        counsellor_profile = CounsellorExtendedProfile.objects.get(
            user=staffProfile)
    except Exception:
        counsellor_profile = None
    context = {'staffprofile': staffProfile,
               'counsellor_profile': counsellor_profile}
    if request.method == 'POST':
        full_name = request.POST.get('name')
        phone = request.POST.get('phone')
        college = request.POST.get('college')
        from_yr = request.POST.get('from_yr')
        to_yr = request.POST.get('to_yr')
        current_job = request.POST.get('current_job')
        description = request.POST.get('description')

        staffProfile.fullname = full_name
        staffProfile.phone = phone
        staffProfile.save()

        counsellor_profile.college = college
        counsellor_profile.from_yr = from_yr
        counsellor_profile.to_yr = to_yr
        counsellor_profile.current_job = current_job
        counsellor_profile.counselling_thought = description
        counsellor_profile.save()
        return redirect('my_profile_page')
    if usertype:
        if usertype == 'student':
            if staffProfile.user_status == 'approved':
                return redirect('students_list')
            else:
                return redirect('approval_waiting')
        elif usertype == 'counsellor':
            if staffProfile.user_status == 'approved':
                return render(request, "my_profile.html", context)
            else:
                return redirect('approval_waiting')
    else:
        return redirect('user_type')
    return render(request, 'my_profile.html', context)


@login_required(login_url='login')
def student_profile(request):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    if request.method == "POST":
        full_name = request.POST.get('name')
        prepared_from = request.POST.get('prepared_from')
        rank = request.POST.get('rank')
        description = request.POST.get('description')
        userprofile.fullname = full_name
        userprofile.user_type = 'student'
        userprofile.save()
        StudentExtendedProfile.objects.create(
            user=userprofile,
            prepared_from=prepared_from,
            rank=rank,
            description=description
        )
        return redirect('approval_waiting')
    context = {'userprofile': userprofile}
    return render(request, "student_profile.html", context)


@login_required(login_url='login')
def counsellor_profile(request):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    if request.method == "POST":
        full_name = request.POST.get('name')
        phone = request.POST.get('phone')
        college = request.POST.get('college')
        from_yr = request.POST.get('from_yr')
        to_yr = request.POST.get('to_yr')
        current_job = request.POST.get('current_job')
        description = request.POST.get('description')

        userprofile.fullname = full_name
        userprofile.phone = phone
        userprofile.user_type = 'counsellor'
        userprofile.save()
        CounsellorExtendedProfile.objects.create(
            user=userprofile,
            college=college,
            from_yr=from_yr,
            to_yr=to_yr,
            current_job=current_job,
            counselling_thought=description
        )
        return redirect('approval_waiting')
    context = {'userprofile': userprofile}
    return render(request, "counsellor_profile.html", context)


def student_counselling_page(request, pk):
    # get post object
    student_profile = StudentExtendedProfile.objects.get(id=pk)
    staffprofile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            reply_obj = None
            try:
                reply_id = int(request.POST.get('reply_id'))
            except:
                reply_id = None
            if reply_id:
                reply_obj = Comment.objects.get(id=reply_id)

            # author = form.cleaned_data['author']
            comment = form.cleaned_data['content']
            if reply_obj:
                Comment(content=comment,
                        parent=reply_obj, comment_to=student_profile, commented_by=staffprofile).save()
            else:
                Comment(content=comment,
                        comment_to=student_profile, commented_by=staffprofile).save()
            return redirect('student_counsil_page', pk)
    else:
        form = CommentForm()
    counsellors = CounsellorExtendedProfile.objects.all()
    comments = Comment.objects.filter(
        comment_to=student_profile, parent=None).order_by('date_posted')
    context = {
        'post': student_profile,
        'form': form,
        'comments': comments,
        'student_profile': student_profile, 'staffprofile': staffprofile,
        'counsellors': counsellors
    }
    return render(request, 'student_comment_page.html', context)


@login_required(login_url='login')
def approval_waiting(request):
    user = request.user
    try:
        staffProfile = UserProfile.objects.get(user=user)
    except Exception:
        staffProfile = None

    try:
        usertype = staffProfile.user_type
    except Exception:
        usertype = None
    if usertype:
        if usertype == 'student':
            if staffProfile.user_status == 'approved':
                return redirect('/')
            else:
                return render(request, "waiting.html")
        elif usertype == 'counsellor':
            if staffProfile.user_status == 'approved':
                return redirect('/')
            else:
                return render(request, "waiting.html")
    context = {'userprofile': staffProfile}
    return render(request, "waiting.html", context)


def get_timestamp():
    """
    Used to return current timestamp in integer
    :return: int value

    """
    import time
    millis = int(round(time.time() * 1000))
    return millis


def update_user_social_data(strategy, *args, **kwargs):
    response = kwargs['response']
    backend = kwargs['backend']
    user = kwargs['user']
    user, bool = UserProfile.objects.get_or_create(user=user)
    if kwargs['is_new']:
        if response['picture']:
            image_url = response['picture']
            # im = Image.open(requests.get(image_url, stream=True).raw)
            # timestamp = get_timestamp()
            # filename = str(user.id) + str(timestamp) + '.jpg'
            # path = UPLOAD_IMAGE_URL + str(filename)
            # im.save(path)
            user.google_picture = image_url
            user.save()
    else:
        pass


@login_required(login_url='login')
def college_branch_page(request):
    user = request.user
    staffProfile = UserProfile.objects.get(user=user)
    # student_profile = StudentExtendedProfile.objects.get(user)
    context = {'staffprofile': staffProfile}
    return render(request, 'college_branch.html', context)


@login_required(login_url='login')
def f_a_q_page(request):
    user = request.user
    staffProfile = UserProfile.objects.get(user=user)
    question_answer = Frequestly_Asked_Question.objects.all()
    # student_profile = StudentExtendedProfile.objects.get(user)
    context = {'staffprofile': staffProfile,
               'question_answer': question_answer}
    return render(request, 'faq.html', context)
