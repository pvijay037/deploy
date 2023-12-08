from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VideoUploadForm
from .models import UploadedVideo

@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.uploaded_by = request.user
            video.save()
            return redirect('profile')
    else:
        form = VideoUploadForm()
    return render(request, 'myapp/upload.html', {'form': form})

@login_required
def profile(request):
    # Retrieve videos uploaded by the current user
    user_videos = UploadedVideo.objects.filter(uploaded_by=request.user)
    return render(request, 'myapp/profile.html', {'user_videos': user_videos})
