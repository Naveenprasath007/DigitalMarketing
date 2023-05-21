from django.shortcuts import render,redirect,HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import Video_form,Question
from .models import Video,TbVideo,Campaignvideo,TbCampaignquestion,TbQuestion,Campaignquestionresponse
import pandas as pd
import json

import speech_recognition as sr 
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

import uuid


def createrupload(request):
    if request.method == "POST":
            videoform=Video_form(data=request.POST,files=request.FILES)
            q0 = request.POST.get('q0')
            q1 = request.POST.get('q1')
            q2 = request.POST.get('q2')
            q3 = request.POST.get('q3')
            q4 = request.POST.get('q4')
            Qlist=[q0,q1,q2,q3,q4]
            Qlist=list(filter(None,Qlist))
            print(Qlist)


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
                    data=TbQuestion.objects.all()
                    dataQ=TbCampaignquestion.objects.all()

                    lenOfList=len(data)
                    listOfQuestion=[]
                    for i in data:
                        output=i.questiontext
                        listOfQuestion.append(output)
                    questionsText = {}
                    for i in range(0,lenOfList):
                        QT=listOfQuestion[i]
                        questionsText["q"+str(i)] = QT
                    print(questionsText)

                    listOfQuestionResponse=[]
                    for i in data:
                        output=i.questionresponse.split("|")
                        listOfQuestionResponse.append(output)

                    QuestionResponse = {}
                    for i in range(0,lenOfList):
                        lQR=listOfQuestionResponse[i]
                        QuestionResponse["k"+str(i)] = lQR
                    print(QuestionResponse)



                    return render(request,'tc_DigitalMarketing/createrupload.html',{"form":videoform,
                                                                                    "video":url,"text":text,
                                                                                    'qT':questionsText,
                                                                                    'qR':QuestionResponse,
                                                                                    "data":data,'dataQ':dataQ})
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
            print(q0,q1,q2,q3)

            # Generate a new UUID
            new_id = uuid.uuid4()
            str(new_id)

            T=Title1
            # video_details2 = TbVideo(videoid=new_id,videoname=T,videopath=url1,
            #                          previousvideoid=0,videotranscription=text)
            # video_details2.save()
            # video_details3 = Campaignvideo(campaignvideoid=new_id,
            #                                videoid=TbVideo.objects.get(videoname = T)
            #                                ,campaignid=1,previousvideoid=0)
            # video_details3.save()

            # video_details4 = TbCampaignquestion(campaignquestionid='AA',
            #                                campaignvideoid=Campaignvideo.objects.get(campaignvideoid = new_id)
            #                                ,userroleid=1,questionid=TbQuestion.objects.get(questionid=1))
            # video_details4.save()   

            cQresponse=TbCampaignquestion.objects.all()
            lenOfList=len(cQresponse)
            listOfcQresponse=[]
            for i in cQresponse:
                output=i.campaignquestionid
                listOfcQresponse.append(output)

            import itertools

            for (a, b) in itertools.zip_longest(listOfcQresponse,Qlist):
                    video_details5 = Campaignquestionresponse(campaignquestionid=TbCampaignquestion.objects.get(campaignquestionid = a),
                                            userid=1,response= b)
                    video_details5.save()  

            return HttpResponse("submitted succesfully")
    else:
        Qlist=["q0","q1","q2","q3"]
        videoform=Video_form()
        data=TbQuestion.objects.all()
        dataQ=TbCampaignquestion.objects.all()
        lenOfList=len(data)
        listOfQuestion=[]
        for i in data:
            output=i.questiontext
            listOfQuestion.append(output)
        questionsText = {}
        for i in range(0,lenOfList):
            QT=listOfQuestion[i]
            questionsText["q"+str(i)] = QT
        print(questionsText)

        listOfQuestionResponse=[]
        for i in data:
            output=i.questionresponse.split("|")
            listOfQuestionResponse.append(output)

        QuestionResponse = {}
        for i in range(0,lenOfList):
            lQR=listOfQuestionResponse[i]
            QuestionResponse["k"+str(i)] = lQR
        print(QuestionResponse)


        cQresponse=Campaignquestionresponse.objects.all()
        lenOfList=len(cQresponse)
        listOfcQresponse=[]
        for i in cQresponse:
            output=i.campaignquestionid
            listOfcQresponse.append(output)

        # print(listOfcQresponse)
        # for i in listOfcQresponse:
        #     print(i)
        # for i in Qlist:
        #     print(i)

        i=0
        while i<lenOfList:
            print(listOfcQresponse[i])
            i = i+1


        df = pd.DataFrame(list(TbQuestion.objects.all().values()))
        df['questionresponse']=df['questionresponse'].str.split("|", n = 5, expand = False)
        json_records = df.reset_index().to_json(orient ='records')
        arr = []
        arr = json.loads(json_records)    

        return render(request,'tc_DigitalMarketing/createrupload.html',{"form":videoform,"data":data,
                                                                        'qT':questionsText,'qR':QuestionResponse,
                                                                        'd':arr,'dataQ':dataQ})
    
def approver(request):
    if request.method == "POST":
        return render(request,'tc_DigitalMarketing/createrupload.html')
    else:
        data = video_details.objects.all()
        return render(request,'tc_DigitalMarketing/approver.html',{"data":data})



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
