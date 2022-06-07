from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Image, User, Comments
from .forms import PostForm, LoginForm, SignUpForm, UpdateProfileForm

# Create your views here.
def index(request):
    # current_user = request.user
    # if request.method == 'POST':
    #     form = LoginForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.username = current_user.username
    #         user.save()
    #         return redirect('home')
    # else:
    #     form = LoginForm()
        
    # context= {
    #     'form': form
    # }
    return render(request, 'insta/index.html')
 
@login_required(login_url='/accounts/login/')
def home(request):
    allimages = Image.objects.all()
    comments = Comments.objects.all()
    allusers = Profile.objects.all()
    
    context =  {
        'posts': allimages,
        'users': allusers,
        'comments': comments
    }
    
    return render(request, 'insta/home.html', context, )

@login_required(login_url='/accounts/login/')
def upload(request):
    form = PostForm()
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post= form.save(commit=False)
            post.profile = current_user
            post.save()
            messages.success(request, 'Post Succesfully Uploaded', extra_tags='alert alert-success')              
            return redirect('home')
    
        
        # messages.error(request, 'Form data is invalid', extra_tags='alert alert-danger')
        # return redirect('home')
        
        
    return render(request, 'insta/upload.html', {'postform': form})


# @login_required(login_url='/accounts/login/')
# def profile(request, user_id):
#     # current_user = request.user
#     # user = User.objects.get(id=current_user.id)
#     profile = Profile.objects.get(current_user)
#     images = Image.objects.get(pk=user_id)

#     # current_user=get_object_or_404(User,id=username)
#     # current_user = request.user
#     # images = Image.objects.filter(id==current_user.id)
#     # profile = get_object_or_404(Profile,id = current_user.id)
#     return render(request, 'insta/profile.html', {'profile':profile, 'posts':images})


@login_required(login_url='/accounts/login/')
def profile(request):
    # current_user=get_object_or_404(User,id=profileId)
    current_user = request.user.id
    images = Image.objects.filter(id=current_user)
    profile = Profile.objects.filter(user=current_user)
    # profile = get_object_or_404(Profile,id = current_user.id)
    return render(request, 'profile/profile.html', {"images": images, "profile": profile})


@login_required(login_url='/accounts/login/')
def updateprofile(request):
    form = UpdateProfileForm()
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    current_user = request.user
    profile_details = Profile.objects.all()
    return render(request, 'profile/updateprofile.html', {'profiles':profile_details, 'current_user':current_user, 'form':form})


def logout(request):
    return render(request, '/')


def search_results(request):
    if 'term' in request.GET and request.GET["term"]:
        search_term = request.GET.get("term")
        searched_terms = Image.search_by_name(search_term)
        message = f"{search_term}"
        return render(request, 'search/search.html',{"message":message,"terms": searched_terms})
    else:
        message = "Searched term not found"
        return render(request, 'search/search.html', {"message":message})
