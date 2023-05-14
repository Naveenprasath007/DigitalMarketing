from django.shortcuts import render,redirect,HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import Video_form
from .models import Video,video_details

import speech_recognition as sr 
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip



def createrupload(request):
    if request.method == "POST":
            videoform=Video_form(data=request.POST,files=request.FILES)
            q = request.POST.get('qo')
            qc = request.POST.get('qc')
            c = request.POST.get('co')
            cc = request.POST.get('cc')
            print(q)
            print(qc)
            print(c)
            print(cc)
            if videoform:
                if videoform.is_valid():
                    videoform.save()
                    all_video=Video.objects.all()
                    for i in all_video:
                        url=i.video.url
                    url1=url[1:]
                    print(url1)
                    text=videotranscribe(url1)
                    # print(text)
                    # return url,text
                    return render(request,'tc_DigitalMarketing/createrupload.html',{"form":videoform,"video":url,"text":text,})
            all_video=Video.objects.all()
            for i in all_video:
                url=i.video.url
                Title1=i.Title
                # q1=i.question1
            url1=url[1:]
            text=videotranscribe(url1)
            print(text)
            print(url)
            print(Title1)
            
            T=Title1
            video_details1 = video_details(Title=T,video=url1,quality=q,qualitycommmand=qc,complaint=c,complaintcommand=cc,transcribe=text)
            video_details1.save()
            return HttpResponse("submitted succesfully")
    else:
        videoform=Video_form()
        return render(request,'tc_DigitalMarketing/createrupload.html',{"form":videoform})
    


def videotranscribe(url):
    num_seconds_video= 52*60
    print("The video is {} seconds".format(num_seconds_video))
    l=list(range(0,num_seconds_video+1,60))

    diz={}
    for i in range(len(l)-1):
        ffmpeg_extract_subclip(url, l[i]-2*(l[i]!=0), l[i+1], targetname="chunks/cut{}.mp4".format(i+1))
        clip = mp.VideoFileClip(r"chunks/cut{}.mp4".format(i+1)) 
        clip.audio.write_audiofile(r"converted/converted{}.wav".format(i+1))
        r = sr.Recognizer()
        audio = sr.AudioFile("converted/converted{}.wav".format(i+1))
        with audio as source:
            r.adjust_for_ambient_noise(source)  
            audio_file = r.record(source)
        result = r.recognize_google(audio_file)
        diz['chunk{}'.format(i+1)]=result

        l_chunks=[diz['chunk{}'.format(i+1)] for i in range(len(diz))]
        text='\n'.join(l_chunks)

        return text
