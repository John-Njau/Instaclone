from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Image, User, Comments, Likes
from .forms import PostForm, UpdateProfileForm, CommentForm

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
    return redirect('/accounts/login/')
 
@login_required(login_url='/accounts/login/')
def home(request):
    # image = get_object_or_404(Profile, pk=request.user.id)
    
    allimages = Image.objects.all()
    comments = Comments.objects.filter(pk=request.user.id)
    allusers = Profile.objects.filter(id=request.user.id).first()
    
    # if request.method == 'POST':
    #     commentform = CommentForm(data=request.POST)
    #     if commentform.is_valid():
    #         new_comment = commentform.save(commit=False)
    #         new_comment.image =image
    #         new_comment.save()
    
    # else:
    commentform = CommentForm()
    
    context =  {
        'posts': allimages,
        'users': allusers,
        'comments': comments,
        'commentform': commentform
    }
    return render(request, 'insta/home.html', context, )


def addcomment(request, pk):
    image = get_object_or_404(Image,pk=pk)
    
    
    # allimages = Image.objects.all()
    comments = image.comments.filter(id=image.id)
    # allusers = Profile.objects.all()
    
    if request.method == 'POST':
        commentform = CommentForm(data=request.POST)
        if commentform.is_valid():
            new_comment = commentform.save(commit=False)
            new_comment.image =image
            new_comment.save()
    
    else:
        commentform = CommentForm()
    
    context =  {
        'comments': comments,
        'commentform': commentform
    }
    return render(request, 'insta/home.html', context, )


@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post= form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post Succesfully Uploaded', extra_tags='alert alert-success')              
        return redirect('home')
    else:
        form = PostForm()
        # messages.error(request, 'Form data is invalid', extra_tags='alert alert-danger')
        # return redirect('home')
    return render(request, 'insta/upload.html', {'postform': form, })


@login_required(login_url='/accounts/login/')
def profile(request):
    # current_user=get_object_or_404(User,id=profileId)
    current_user = request.user.id
    images = Image.objects.filter(id=current_user)
    profile = Profile.objects.filter(user=current_user).first()
    # profile = get_object_or_404(Profile,id = current_user.id)
    return render(request, 'profile/profile.html', {"images": images, "profile": profile})


@login_required(login_url='/accounts/login/')
def updateprofile(request):
    current_user = request.user
    profile_details = Profile.objects.filter(id=current_user.id).first()
    form = UpdateProfileForm()
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
        return redirect('profile')
    
    return render(request, 'profile/updateprofile.html', {'profiles':profile_details, 'current_user':current_user, 'form':form})


def like_image(request,operation,pk):
    image = get_object_or_404(Image,pk=pk)
    # like = Likes.objects.filter(image = image ,user = request.user).first()
    # if like is None:
    #     like = Likes()
    #     like.image = image
    #     like.user = request.user
    #     like.save()
    # else:
    #     like.delete()
    if operation == 'like':
        image.likes += 1
        image.save()
    elif operation =='unlike':
        image.likes -= 1
        image.save()
    return redirect('home')


def search_results(request):
    if 'term' in request.GET and request.GET["term"]:
        search_term = request.GET.get("term")
        searched_terms = Image.search_by_name(search_term)
        message = f"{search_term}"
        return render(request, 'search/search.html',{"message":message,"terms": searched_terms})
    else:
        message = "Searched term not found"
        return render(request, 'search/search.html', {"message":message})



def logout(request):
    return render(request, '/')


