from django.shortcuts import render,redirect,HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import Video_form,Question,userRole,TbUser
from .models import Video,TbVideo,Campaignvideo,TbCampaignquestion,TbQuestion,Campaignquestionresponse,TbUserrole,cVideoId
import pandas as pd
import json

import speech_recognition as sr 
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

import uuid
from django.contrib import messages

from django.db import connection

def createrupload(request,id):
        if request.method == "POST":
            videoform=Video_form(data=request.POST,files=request.FILES)
            q0 = request.POST.get('q0')
            q1 = request.POST.get('q1')
            q2 = request.POST.get('q2')
            q3 = request.POST.get('q3')
            q4 = request.POST.get('q4')
            q5 = request.POST.get('q5')
            q6 = request.POST.get('q6')
            Campaignvideoid=request.POST.get('campaign')
            Qlist=[q0,q1,q2,q3,q4,q5,q6]
            Qlist=list(filter(None,Qlist))
            print(Qlist)
            print(Campaignvideoid)
            CVID=Campaignvideoid
            print(CVID)

            if videoform:
                if videoform.is_valid():
                    videoform.save()
                    all_video=Video.objects.all()
                    for i in all_video:
                        url=i.video.url
                        Title1=i.Title
                    url1=url[1:]
                    print(url1)
                    text=videotranscribe(url1)

                    data=TbQuestion.objects.all()

                    # dataQ = TbCampaignquestion.objects.filter(campaignvideoid=CVID)
                    # listOfDataQ=[]
                    # for i in dataQ:
                    #     output=i.questionid
                    #     listOfDataQ.append(output)
                    # lenOfList=len(listOfDataQ)

                    # listOfQuestion=[]
                    # for i in listOfDataQ:
                    #     output=i.questiontext
                    #     listOfQuestion.append(output)
                    # questionsText = {}
                    # for i in range(0,lenOfList):
                    #     QT=listOfQuestion[i]
                    #     questionsText["q"+str(i)] = QT


                    # listOfQuestionResponse=[]
                    # for i in listOfDataQ:
                    #     output=i.questionresponse.split("|")
                    #     listOfQuestionResponse.append(output)

                    # QuestionResponse = {}
                    # for i in range(0,lenOfList):
                    #     lQR=listOfQuestionResponse[i]
                    #     QuestionResponse["k"+str(i)] = lQR


                    # Generate a new UUID
                    new_id = uuid.uuid4()
                    str(new_id)
                    print(str(new_id))

                    
                    video_id = cVideoId(VideoID=new_id)
                    video_id.save()

                    T=Title1
                    video_details2 = TbVideo(videoid=new_id,videoname=T,videopath=url1,
                                            previousvideoid=0,videotranscription=text)
                    video_details2.save()

                    video_details3 = Campaignvideo(campaignvideoid=new_id,
                                                videoid=TbVideo.objects.get(videoname = T)
                                                ,campaignid=1,previousvideoid=0)
                    video_details3.save()

                    if CVID == 'ABCD':    
                        video_details4 = TbCampaignquestion(campaignquestionid=str(new_id)+str(1),
                                                    campaignvideoid=Campaignvideo.objects.get(campaignvideoid=new_id)
                                                    ,userroleid=TbUserrole.objects.get(userroleid='U1'),
                                                    questionid=TbQuestion.objects.get(questionid='1'))
                        video_details4.save()

                        video_details4 = TbCampaignquestion(campaignquestionid=str(new_id)+str(2),
                                                    campaignvideoid=Campaignvideo.objects.get(campaignvideoid=new_id)
                                                    ,userroleid=TbUserrole.objects.get(userroleid='U1'),
                                                    questionid=TbQuestion.objects.get(questionid='2'))
                        video_details4.save()

                        video_details4 = TbCampaignquestion(campaignquestionid=str(new_id)+str(3),
                                                    campaignvideoid=Campaignvideo.objects.get(campaignvideoid=new_id)
                                                    ,userroleid=TbUserrole.objects.get(userroleid='U1'),
                                                    questionid=TbQuestion.objects.get(questionid='3'))
                        video_details4.save()

                        video_details4 = TbCampaignquestion(campaignquestionid=str(new_id)+str(4),
                                                    campaignvideoid=Campaignvideo.objects.get(campaignvideoid=new_id)
                                                    ,userroleid=TbUserrole.objects.get(userroleid='U1'),
                                                    questionid=TbQuestion.objects.get(questionid='4'))
                        video_details4.save()
                        
                        # video_details4 = TbCampaignquestion(campaignquestionid=new_id,
                        #                             campaignvideoid=Campaignvideo.objects.get(previousvideoid=0)
                        #                             ,userroleid='U1',questionid='2')
                        # video_details4.save()
                        
                        # video_details4 = TbCampaignquestion(campaignquestionid=new_id,
                        #                             campaignvideoid=Campaignvideo.objects.get(previousvideoid=0)
                        #                             ,userroleid='U1',questionid='3')
                        # video_details4.save()

                        # video_details4 = TbCampaignquestion(campaignquestionid=new_id,
                        #                             campaignvideoid=Campaignvideo.objects.get(previousvideoid=0)
                        #                             ,userroleid='U1',questionid='4')
                        # video_details4.save()

                        # video_details4 = TbCampaignquestion(campaignquestionid=new_id,
                        #                             campaignvideoid=Campaignvideo.objects.get(previousvideoid=0)
                        #                             ,userroleid='U1',questionid='5')
                        # video_details4.save()


                        # video_details4 = TbCampaignquestion(campaignquestionid=new_id,
                        #                             campaignvideoid=Campaignvideo.objects.get(previousvideoid=0)
                        #                             ,userroleid='U1',questionid='6')
                        # video_details4.save()
                    

                    dataQ = TbCampaignquestion.objects.filter(campaignvideoid=new_id)
                    listOfDataQ=[]
                    for i in dataQ:
                        output=i.questionid
                        listOfDataQ.append(output)
                    lenOfList=len(listOfDataQ)

                    listOfQuestion=[]
                    for i in listOfDataQ:
                        output=i.questiontext
                        listOfQuestion.append(output)
                    questionsText = {}
                    for i in range(0,lenOfList):
                        QT=listOfQuestion[i]
                        questionsText["q"+str(i)] = QT


                    listOfQuestionResponse=[]
                    for i in listOfDataQ:
                        output=i.questionresponse.split("|")
                        listOfQuestionResponse.append(output)

                    QuestionResponse = {}
                    for i in range(0,lenOfList):
                        lQR=listOfQuestionResponse[i]
                        QuestionResponse["k"+str(i)] = lQR

                    # return render(request,'tc_DigitalMarketing/createrupload.html',{"form":videoform,
                    #                                                                 "video":url,"text":text,})
                    return render(request,'tc_DigitalMarketing/createrupload.html',{"form":videoform,
                                                                                    "video":url,"text":text,
                                                                                    'qT':questionsText,
                                                                                    'qR':QuestionResponse,
                                                                                    "data":data,'dataQ':dataQ})
            all_video=Video.objects.all()
            # cV=Campaignvideo.objects.all()
            
            # for i in cV:
            #     CVID=i.campaignvideoid

            cursor=connection.cursor()
            cursor.execute("SELECT TOP 1 VideoID FROM DigitalMarketing_cvideoid ORDER BY id DESC;")
            result=cursor.fetchall()
            print(result)
            CVID=result[0][0]
            
            for i in all_video:
                url=i.video.url
                Title1=i.Title
                # q1=i.question1
            url1=url[1:]
            text=videotranscribe(url1)
            print(text)
            print(url)
            print(Title1)
            print(CVID)
            print(q0,q1,q2,q3)
            print(id)
  
# ___problem is in CVID___#
            cQresponse=TbCampaignquestion.objects.filter(campaignvideoid=CVID)
            lenOfList=len(cQresponse)
            listOfcQresponse=[]
            for i in cQresponse:
                output=i.campaignquestionid
                listOfcQresponse.append(output)
            print(listOfcQresponse)
            import itertools

            for (a, b) in itertools.zip_longest(listOfcQresponse,Qlist):
                    video_details5 = Campaignquestionresponse(campaignquestionid=TbCampaignquestion.objects.get(campaignquestionid = a),
                                            userid=TbUser.objects.get(userid = str(id)),response= b)
                    video_details5.save()  

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



        
    
def UserIndexpage(request):
        if request.method == 'POST':
            userName = request.POST.get('username')
            Password = request.POST.get('pass')
            data = TbUser.objects.filter(username=userName,password=Password).values()
            for i in data:
                print(i)
                a=i
            if data:
                value=a.get('userroleid_id')
                print(value)
                if value == "U1":
                    val=a.get('userid')
                    return redirect('/dm/createrupload/'+str(val)) 
                if value == "R1":
                    return redirect('/dm/approver')

            return redirect('/dm/UserIndexpage')    
        else:
            return render(request, 'tc_DigitalMarketing/UserindexPage.html')


    
def approver(request):
    if request.method == "POST":
        return render(request,'tc_DigitalMarketing/createrupload.html')
    else:
        # cursor=connection.cursor()
        # cursor.execute("select UserName from tb_User WHERE UserRoleID='U1';")
        # result=cursor.fetchall()
        # print(result)

        cursor1=connection.cursor()
        cursor1.execute("select CampaignVideoID from tb_User u inner join CampaignQuestionResponse cqr on u.UserID = cqr.UserID inner join tb_CampaignQuestion cq on cq.CampaignQuestionID=cqr.CampaignQuestionID;")
        result1=cursor1.fetchall()
        print(result1)
        listOfVid=[]
        uniresult=unique_numbers(result1)
        for i in uniresult:
            OUTPUT=i[0]
            listOfVid.append(OUTPUT)
        print(listOfVid)

        listOfuserName=[]
        for i in listOfVid:
            cursor=connection.cursor()
            cursor.execute("select UserName,CampaignVideoID from tb_User u inner join CampaignQuestionResponse cqr on u.UserID = cqr.UserID inner join tb_CampaignQuestion cq on cq.CampaignQuestionID=cqr.CampaignQuestionID AND cq.CampaignVideoID='{val}';".format(val=i))
            result=cursor.fetchall()
            result=unique_numbers(result)
            listOfuserName.append(result)
            
        
        print(listOfuserName)
        return render(request,'tc_DigitalMarketing/approver.html',{"r":listOfuserName})



def approverview(request,id):
    if request.method == "POST":
        return render(request,'tc_DigitalMarketing/approverview.html',{})
    else:
        CVID=id
        dataQ = TbCampaignquestion.objects.filter(campaignvideoid=CVID)
        listOfDataQ=[]
        for i in dataQ:
            output=i.questionid
            listOfDataQ.append(output)
        lenOfList=len(listOfDataQ)

        listOfQuestion=[]
        for i in listOfDataQ:
            output=i.questiontext
            listOfQuestion.append(output)
        questionsText = {}
        for i in range(0,lenOfList):
            QT=listOfQuestion[i]
            questionsText["q"+str(i)] = QT


        listOfQuestionResponse=[]
        for i in listOfDataQ:
            output=i.questionresponse.split("|")
            listOfQuestionResponse.append(output)

        QuestionResponse = {}
        for i in range(0,lenOfList):
            lQR=listOfQuestionResponse[i]
            QuestionResponse["k"+str(i)] = lQR

        cursor=connection.cursor()
        # cursor.execute('select* from tb_UserRole')
        # ___This for get question and responces__
        cursor.execute("select QuestionText,Response from CampaignQuestionResponse cqr inner join tb_CampaignQuestion cquestion on cqr.CampaignQuestionID = cquestion.CampaignQuestionID AND cquestion.CampaignVideoID ='{value}' inner join tb_Question question on cquestion.QuestionID = question.QuestionID;".format(value=CVID))
        # cursor.execute("select QuestionText,Response from CampaignQuestionResponse cqr inner join tb_CampaignQuestion cquestion on cqr.CampaignQuestionID = cquestion.CampaignQuestionID AND cqr.UserID = 1 inner join tb_Question question on cquestion.QuestionID = question.QuestionID;")
        result=cursor.fetchall()
        print(result)
        return render(request,'tc_DigitalMarketing/approverview.html',{'qT':questionsText,'qR':QuestionResponse,'R':result})
    



def unique_numbers(numbers):
    # this will take only unique numbers from the tuple
    return tuple(set(numbers))