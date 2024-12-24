from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from .models import Post , Like , Save , Followed , Notification , Profile , Story
import wikipedia

# Create your views here.
@login_required
def index(request):
    user_posts = Post.objects.annotate(like_count=Count('like')).order_by('-id')
    # userpost = Post.objects.all().order_by('-id')
    # Saves = Save.objects.filter(user=request.user)
    Likes = Like.objects.filter(user=request.user)
    
    

    return render(request, 'index.html' ,{'userpost':user_posts , 'likes':Likes ,})


def loginpage(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=uname, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
           return redirect('signup')
    return render(request, 'login.html')


def singup(request):
    if request.method == "POST":
        name = request.POST.get('username')
        print(name)

        password = request.POST.get('password')
        print(password)
        email = request.POST.get('email')
        user = User.objects.create_user(
            username=name, password=password, email=email)
        user.save()
        return redirect("loginpage")

    return render(request, 'signup.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Save, Followed, Profile

@login_required
def profile(request):
    userpost = Post.objects.filter(user=request.user)
    userProfiles ='none'
    if Profile.objects.filter(user=request.user).exists():

      userProfiles = Profile.objects.get(user=request.user)
    save = Save.objects.filter(user=request.user)
    userpostcount = userpost.count()
    userFollower = Followed.objects.filter(following=request.user)
    userFollowing = Followed.objects.filter(follower=request.user)
    userFollowercount = userFollower.count()
    userFollowingcount = userFollowing.count()

    if request.method == "POST":
        profilePicture = request.FILES.get('profile')
        isPrivet = request.POST.get('isPrivet') == 'on'  # Convert to boolean
        profile_exists = Profile.objects.filter(user=request.user).exists()

        if profile_exists:
            userProfile = Profile.objects.get(user=request.user)
            if profilePicture:
                userProfile.profile_image = profilePicture
            userProfile.privet_account = isPrivet
            userProfile.save()
        else:
            profile_details = Profile(
                user=request.user,
                profile_image=profilePicture if profilePicture else None,
                privet_account=isPrivet
            )
            profile_details.save()

        return redirect('profile')

    return render(request, 'profile.html', {
        'userpost': userpost,
        'saves': save,
        'userpostcount': userpostcount,
        'userFollowing': userFollowing,
        'userFollower': userFollower,
        'userFollowingcount': userFollowingcount,
        'userFollowercount': userFollowercount,
        'userProfile':userProfiles,
    })


@login_required


def userprofile(request, id):
    if id == request.user.id:
        return redirect('profile')
    user = get_object_or_404(User, id=id)  # Get a single user object or return a 404 page
    if user.profile.privet_account:
        userFollowingObject = Followed.objects.filter(follower = request.user , following=user).exists()
        userFollowingObject2 = Followed.objects.filter(follower=user , following=request.user)

        if(userFollowingObject and userFollowingObject2):



    
            userpost = Post.objects.filter(user=user)  # Assuming there's a 'user' field in Post model
            save = Save.objects.filter(user=user)  # Assuming there's a 'user' field in Save model
            # isFollow = False
            userpostcount = userpost.count()  # Count user posts
            userFollower = Followed.objects.filter(following=user)  
            userFollowing = Followed.objects.filter(follower=user)  
            userFollowercount = userFollower.count
            userFollowingcount = userFollowing.count

            isFollow = Followed.objects.filter(follower=user, following=request.user).exists()
            isPrivet = False
        

            
            return render(
                request, 
                "userprofile.html", 
                {
                    'userFollowing':userFollowing,
                    'userFollower':userFollower,
                    'userId':id,
                'username':user,
                    'isFollow':isFollow,
                    'userpost': userpost,
                    'saves': save,
                    'userpostcount': userpostcount,
                    'userFollowingcount': userFollowingcount,
                    'userFollowercount': userFollowercount,
                    'isPrivet':isPrivet
                })
        else :
             isPrivet = True
             userpost = Post.objects.filter(user=user).count
             userFollowercount = Followed.objects.filter(following=user).count
             userFollowingcount = Followed.objects.filter(follower=user).count
             isFollow = Followed.objects.filter(follower=user, following=request.user).exists()

             
             return render(request , "userprofile.html" , {'username':user,'userFollowingcount':userFollowingcount,
                    'userFollowercount':userFollowercount, 'userpostcount': userpost, 'isPrivet':isPrivet , 'isFollow':isFollow, 'userId':id})
    
    else:
            userpost = Post.objects.filter(user=user)  # Assuming there's a 'user' field in Post model
            save = Save.objects.filter(user=user)  # Assuming there's a 'user' field in Save model
            # isFollow = False
            userpostcount = userpost.count()  # Count user posts
            userFollower = Followed.objects.filter(following=user)  
            userFollowing = Followed.objects.filter(follower=user)  
            userFollowercount = userFollower.count
            userFollowingcount = userFollowing.count

            isFollow = Followed.objects.filter(follower=user, following=request.user).exists()
            isPrivet = False
        

            
            return render(
                request, 
                "userprofile.html", 
                {
                    'userFollowing':userFollowing,
                    'userFollower':userFollower,
                    'userId':id,
                'username':user,
                    'isFollow':isFollow,
                    'userpost': userpost,
                    'saves': save,
                    'userpostcount': userpostcount,
                    'userFollowingcount': userFollowingcount,
                    'userFollowercount': userFollowercount,
                    'isPrivet':isPrivet
                })





@login_required
def messages(request):
    user_message = ''
    ai_message = ''

    if request.method == 'POST':
        user_message = request.POST.get('message')

        if user_message.lower() == 'hi':
            ai_message = f'Hi {request.user}, how are you?'
        else:
            try:
                # Use Wikipedia library to search for the user's query
                summary = wikipedia.summary(user_message, sentences=5)
                ai_message = summary
            except wikipedia.exceptions.DisambiguationError as e:
                ai_message = "Your query is ambiguous, please specify further."
            except wikipedia.exceptions.PageError:
                ai_message = "I couldn't find any information on that topic."

    return render(request, 'message.html', {'messages': ai_message, 'user_message': user_message})


@login_required
def upload_reel(request):
    return render(request, "upload.html")


@login_required
def upload_post(request):
    if request.method == "POST":
        post = request.FILES.get('post')
        discription = request.POST.get('description')
        hastag = request.POST.get('hastag')
        user_post = Post(user = request.user,hastage=hastag , post_img = post  ,caption = discription)
        user_post.save()
        return redirect('home')
    return render(request, "postupload.html")

from django.db.models import Count

@login_required
def explore(request):
    # Annotate each post with its like count
    user_posts = Post.objects.annotate(like_count=Count('like'))
    users = User.objects.exclude(username=request.user)
    userfollows = Followed.objects.filter(following=request.user).values_list('follower', flat=True)
    fuser = User.objects.filter(id__in=userfollows)
    return render(request, "explore.html", {'userpost': user_posts, 'users': users, 'fuser': fuser})

def logoutpage(request):
    logout(request)
    return redirect('loginpage')

def save(request , id):
    post_save = Post.objects.get(id =id)
    user1 = User.objects.get(username = request.user)
    save_post = Save.objects.create(user = user1 , post = post_save)
    save_post.save()

    return redirect(request.META.get('HTTP_REFERER'))

def Unsave(request , id):
    GetPost = get_object_or_404(Post , pk=id)
    delete_post = Save.objects.get(user=request.user , post=GetPost)
    delete_post.delete()

    return redirect(request.META.get('HTTP_REFERER'))



def Follow(request, id):
    follower = get_object_or_404(User, pk=id)  # The user to be followed
    following = request.user  # The currently logged-in user
    print(follower)
    print(following)
    
    # Create a notification
    message = f'{request.user.username} started following you'
    notify = Notification.objects.create(ToMessage=follower, Message=message , FromMessage = request.user)
    notify.save()
    
    # Create the follow relationship
    user_Follow = Followed.objects.create(follower=follower, following=following)
    user_Follow.save()
    
    return redirect(request.META.get('HTTP_REFERER'))




def unfollow(request, id):
    follower = User.objects.get(id = id)
    following = request.user
    print(follower)
    print(following)
    # Delete the follow relationship if it exists
    Followed.objects.filter(follower=follower, following=following).delete()
    
    return redirect(request.META.get('HTTP_REFERER'))


def Notiy(request):
    notification = Notification.objects.filter(ToMessage = request.user).order_by('-id')
    print(notification)
    return render(request , 'Notification.html' , {'notification':notification})



def LikePost(request , id):
    user = request.user
    post = get_object_or_404(Post , pk=id)
    ifLike = Like.objects.filter(user=request.user , post=post).exists()
    if ifLike:
        Like.objects.filter(user=user , post=post).delete()

    else:        
        Likeobject = Like(user=user , post=post)
        Likeobject.save()

    return redirect(request.META.get('HTTP_REFERER'))



def HasTageView(request , id):
    # user_posts = Post.objects.annotate(like_count=Count('like'))

    postId = get_object_or_404(Post , pk=id)
    hashtage = postId.hastage
    HashPosts = Post.objects.filter(hastage = hashtage)

    return render(request , 'hastageViewer.html' , {"HashName":postId , "posts":HashPosts})


def UploadStory(request):
    if request.method == 'POST':
        StoryVideo = request.FILES.get('story')
        user = request.user
        userStory = Story(user=user , story=StoryVideo)
        userStory.save()
    return render(request , 'storyUpload.html')