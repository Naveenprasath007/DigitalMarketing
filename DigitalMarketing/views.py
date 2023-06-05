from django.shortcuts import render,redirect,HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import Video_form,Question,userRole
from .models import Video,TbVideo,Campaignvideo,TbCampaignquestion,TbQuestion,Campaignquestionresponse,TbUserrole,cVideoId,TbStatus,TbUser,TbApprove
import pandas as pd


import speech_recognition as sr 
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

import uuid
from django.contrib import messages

from django.db import connection

import os
from datetime import datetime

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
            Vendor=request.POST.get('Vendor')
            Lob=request.POST.get('LOB')
            Creative=request.POST.get('Creative')
            Platform=request.POST.get('Platform')
            print(Creative)
            print(Platform)
            Qlist=[q0,q1,q2,q3,q4,q5,q6]
            Qlist=list(filter(None,Qlist))
            print(Qlist)


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

                    # Generate a new UUID
                    new_id = uuid.uuid4()
                    str(new_id)
                    print(str(new_id))

                    video_id = cVideoId(VideoID=new_id)
                    video_id.save()

                    T=Title1
                    video_details2 = TbVideo(videoid=new_id,videoname=T,videopath=url1,
                                            previousvideoid=0,videotranscription=text,vendor=Vendor,lob=Lob,creative=Creative,platform=Platform)
                    video_details2.save()

                    video_details3 = Campaignvideo(campaignvideoid=new_id,
                                                videoid=TbVideo.objects.get(videoname = T)
                                                ,campaignid=1,previousvideoid=0)
                    video_details3.save()

                    if Platform == 'Facebook':    
                        video_details4 = TbCampaignquestion(campaignquestionid=str(new_id)+str(1),
                                                    campaignvideoid=Campaignvideo.objects.get(campaignvideoid=new_id)
                                                    ,userroleid=TbUserrole.objects.get(userroleid='U1'),
                                                    questionid=TbQuestion.objects.get(questionid='1'))
                        video_details4.save()

                        # video_details4 = TbCampaignquestion(campaignquestionid=str(new_id)+str(2),
                        #                             campaignvideoid=Campaignvideo.objects.get(campaignvideoid=new_id)
                        #                             ,userroleid=TbUserrole.objects.get(userroleid='U1'),
                        #                             questionid=TbQuestion.objects.get(questionid='2'))
                        # video_details4.save()

                        # video_details4 = TbCampaignquestion(campaignquestionid=str(new_id)+str(3),
                        #                             campaignvideoid=Campaignvideo.objects.get(campaignvideoid=new_id)
                        #                             ,userroleid=TbUserrole.objects.get(userroleid='U1'),
                        #                             questionid=TbQuestion.objects.get(questionid='3'))
                        # video_details4.save()

                        # video_details4 = TbCampaignquestion(campaignquestionid=str(new_id)+str(4),
                        #                             campaignvideoid=Campaignvideo.objects.get(campaignvideoid=new_id)
                        #                             ,userroleid=TbUserrole.objects.get(userroleid='U1'),
                        #                             questionid=TbQuestion.objects.get(questionid='4'))
                        # video_details4.save()
                    
                    if Platform == 'Youtube':    

                        video_details4 = TbCampaignquestion(campaignquestionid=str(new_id)+str(3),
                                                    campaignvideoid=Campaignvideo.objects.get(campaignvideoid=new_id)
                                                    ,userroleid=TbUserrole.objects.get(userroleid='U1'),
                                                    questionid=TbQuestion.objects.get(questionid='1'))
                        video_details4.save()

                        # video_details4 = TbCampaignquestion(campaignquestionid=str(new_id)+str(4),
                        #                             campaignvideoid=Campaignvideo.objects.get(campaignvideoid=new_id)
                        #                             ,userroleid=TbUserrole.objects.get(userroleid='U1'),
                        #                             questionid=TbQuestion.objects.get(questionid='6'))
                        # video_details4.save()
                    
                    if Platform == 'GDN':    

                        video_details4 = TbCampaignquestion(campaignquestionid=str(new_id)+str(3),
                                                    campaignvideoid=Campaignvideo.objects.get(campaignvideoid=new_id)
                                                    ,userroleid=TbUserrole.objects.get(userroleid='U1'),
                                                    questionid=TbQuestion.objects.get(questionid='1'))
                        video_details4.save()

                    if Platform == 'TikTok':    

                        video_details4 = TbCampaignquestion(campaignquestionid=str(new_id)+str(3),
                                                    campaignvideoid=Campaignvideo.objects.get(campaignvideoid=new_id)
                                                    ,userroleid=TbUserrole.objects.get(userroleid='U1'),
                                                    questionid=TbQuestion.objects.get(questionid='1'))
                        video_details4.save()


                        

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

                    return render(request,'tc_DigitalMarketing/createrupload.html',{"form":videoform,
                                                                                    "video":url,"text":text,
                                                                                    'qT':questionsText,
                                                                                    'qR':QuestionResponse,
                                                                                    "data":data,'dataQ':dataQ})
            all_video=Video.objects.all()



            cursor=connection.cursor()
            cursor.execute("SELECT TOP 1 VideoID FROM DigitalMarketing_cvideoid ORDER BY id DESC;")
            result=cursor.fetchall()
            print(result)
            CVID=result[0][0]
            

            cursor1=connection.cursor()
            cursor1.execute("select VideoPath,VideoTranscription,VideoName,Platform from CampaignVideo cv inner join tb_Video v on v.VideoID=cv.VideoID AND cv.CampaignVideoID='{val}'".format(val=CVID))
            VideoDeatails=cursor1.fetchall()
            vP='/'+VideoDeatails[0][0]
            vN=VideoDeatails[0][2]
            pN=VideoDeatails[0][3]

            userName=connection.cursor()
            userName.execute("select UserName from tb_User where UserID='{val}'".format(val=id))
            userName=userName.fetchall()
            UN=userName[0][0]
            print(UN)

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
            from datetime import datetime

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

            # status = TbStatus(userid=TbUser.objects.get(userid=id),VideoID=CVID,status='Pending',VideoName=vN,ApproverName='---')
            status = TbStatus(userid=TbUser.objects.get(userid=id),videoid=CVID,status='Pending',videoname=vN,approver='---',uploadername=UN,platform=pN)
            status.save()
  
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
            messages.success(request, 'submitted succesfully')
            return redirect('/dm/createrupload/'+id)
        else:
  
            videoform=Video_form()
            a=id
            return render(request,'tc_DigitalMarketing/createrupload.html',{"form":videoform,'k':a})



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

def unique_numbers(numbers):
    # this will take only unique numbers from the tuple
    return tuple(set(numbers))

    
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
                    val=a.get('userid')
                    
                    return redirect('/dm/approver/'+str(val))
            messages.error(request, 'Invalid! userName or password')
            return redirect('/dm/UserIndexpage')    
        else:
            return render(request, 'tc_DigitalMarketing/UserindexPage.html')


    
def approver(request,id):
    if request.method == "POST":
        return render(request,'tc_DigitalMarketing/createrupload.html')
    else:
        # cursor1=connection.cursor()
        # cursor1.execute("select CampaignVideoID from tb_User u inner join CampaignQuestionResponse cqr on u.UserID = cqr.UserID inner join tb_CampaignQuestion cq on cq.CampaignQuestionID=cqr.CampaignQuestionID;")
        # result1=cursor1.fetchall()
        
        
        # uniresult=unique_numbers(result1)
        # print(uniresult)

        # listOfVid=[]
        # for i in uniresult:
        #     OUTPUT=i[0]
        #     listOfVid.append(OUTPUT)
        # print(listOfVid)

        # listOfuserName=[]

        # for i in listOfVid:
        #     cursor=connection.cursor()
        #     # cursor.execute("select UserName,CampaignVideoID from tb_User u inner join CampaignQuestionResponse cqr on u.UserID = cqr.UserID inner join tb_CampaignQuestion cq on cq.CampaignQuestionID=cqr.CampaignQuestionID AND cq.CampaignVideoID='{val}';".format(val=i))
            
        #     #old one
        #     # cursor.execute("select date,UserName,videoName,VideoID from DigitalMarketing_status status inner join tb_User u on u.UserID=status.UserID  Where VideoID='{val}';".format(val=i))
        #     cursor.execute("select CreatedDate,UserName,videoName,VideoID from tb_Status status inner join tb_User u on u.UserID=status.UserID  Where VideoID='{val}';".format(val=i))
        #     result=cursor.fetchall()
        #     result=unique_numbers(result)
        #     listOfuserName.append(result)
        # print(listOfuserName)
    

        # return render(request,'tc_DigitalMarketing/approver.html',{"r":listOfuserName,'id':id,})
        d=1
        userName=connection.cursor()
        userName.execute("select UserName from tb_User where UserID='{val}';".format(val=d))
        userName=userName.fetchall()
        UN=userName[0][0]
        print(UN)
    
        status=TbStatus.objects.all()
        return render(request,'tc_DigitalMarketing/approver.html',{'status':status,'id':id})



def approverview(request,id,uid):
    if request.method == "POST":
            q0 = request.POST.get('q0')
            q1 = request.POST.get('q1')
            q2 = request.POST.get('q2')
            q3 = request.POST.get('q3')
            q4 = request.POST.get('q4')
            q5 = request.POST.get('q5')
            q6 = request.POST.get('q6')
            tb= request.POST.get('Textbox')
            Qlist=[q0,q1,q2,q3,q4,q5,q6]
            Qlist=list(filter(None,Qlist))
            btn=request.POST.get('btn')
            if btn =='Approve':  
                cursor1=connection.cursor()
                cursor1.execute("select VideoPath,VideoTranscription,VideoName,Platform from CampaignVideo cv inner join tb_Video v on v.VideoID=cv.VideoID AND cv.CampaignVideoID='{val}'".format(val=id))
                VideoDeatails=cursor1.fetchall()
                vP='/'+VideoDeatails[0][0]
                vN=VideoDeatails[0][2]
                pN=VideoDeatails[0][3]

                getApproverName=connection.cursor()
                getApproverName.execute("select UserName from tb_User  WHERE UserID='{value}';".format(value=uid) )
                getApproverName=getApproverName.fetchall() 
                print(getApproverName[0][0])
    
                getuid=connection.cursor()
                getuid.execute("select UserName from tb_User u inner join CampaignQuestionResponse cqr on cqr.userID=u.userID inner join tb_CampaignQuestion cq on cq.CampaignQuestionID=cqr.CampaignQuestionID AND cq.CampaignVideoID ='{value}';".format(value=id))  
                getuid=getuid.fetchall() 
                getuserid=connection.cursor()
                getuserid.execute("select UserID from tb_User WHERE UserName='{value}';".format(value=getuid[0][0]))  
                getuserid=getuserid.fetchall()  
                print(getuserid[0][0])

                userName=connection.cursor()
                userName.execute("select UserName from tb_User where UserID='{val}'".format(val=getuserid[0][0]))
                userName=userName.fetchall()
                UN=userName[0][0]
                
                approve = TbApprove(userid=TbUser.objects.get(userid=getuserid[0][0]),videoid=id,videotitle=vN,videopath=vP,uploadername=UN)
                approve.save()
                deletestatus=connection.cursor()
                deletestatus.execute("DELETE FROM tb_Status WHERE videoID='{value}';".format(value=id))

                video = TbStatus(userid=TbUser.objects.get(userid=getuserid[0][0]),videoid=id,status='Approved',reason='Video is Correct',videoname=vN,approver=getApproverName[0][0],uploadername=UN,platform=pN)   
                # video = Status(userid=TbUser.objects.get(userid=getuserid[0][0]),VideoID=id,status='Approved',reason='Video is Correct',VideoName=vN,ApproverName=getApproverName[0][0])
                video.save() 
                deleteQuestionsres=connection.cursor()
                deleteQuestionsres.execute("DELETE CampaignQuestionResponse FROM CampaignQuestionResponse inner join tb_CampaignQuestion on CampaignQuestionResponse.CampaignQuestionID = tb_CampaignQuestion.CampaignQuestionID WHERE tb_CampaignQuestion.CampaignVideoID='{value}';".format(value=id))
                messages.success(request, 'Approved succesfully')
                return redirect('/dm/approver/'+str(uid))
            if btn =='Reject':
                deletestatus=connection.cursor()
                deletestatus.execute("DELETE FROM tb_Status WHERE videoID='{value}';".format(value=id))
                
                # ___This for get question and responces__
                cursor=connection.cursor()
                cursor.execute("select QuestionText,Response from CampaignQuestionResponse cqr inner join tb_CampaignQuestion cquestion on cqr.CampaignQuestionID = cquestion.CampaignQuestionID AND cquestion.CampaignVideoID ='{value}' inner join tb_Question question on cquestion.QuestionID = question.QuestionID;".format(value=id))
                result=cursor.fetchall()
                print(result)
                l=[]
                res = {}
                for key in result:
                    for value in Qlist:
                        res[key[0]] = value
                        Qlist.remove(value)
                        break       
                l.append(res)
                l.append(tb)

                cursor1=connection.cursor()
                cursor1.execute("select VideoPath,VideoTranscription,VideoName,Platform from CampaignVideo cv inner join tb_Video v on v.VideoID=cv.VideoID AND cv.CampaignVideoID='{val}'".format(val=id))
                VideoDeatails=cursor1.fetchall()
                vP='/'+VideoDeatails[0][0]
                vN=VideoDeatails[0][2]
                pN=VideoDeatails[0][3]

                getuid=connection.cursor()
                getuid.execute("select UserName from tb_User u inner join CampaignQuestionResponse cqr on cqr.userID=u.userID inner join tb_CampaignQuestion cq on cq.CampaignQuestionID=cqr.CampaignQuestionID AND cq.CampaignVideoID ='{value}';".format(value=id))  
                getuid=getuid.fetchall() 
                getuserid=connection.cursor()
                getuserid.execute("select UserID from tb_User WHERE UserName='{value}';".format(value=getuid[0][0]))  
                getuserid=getuserid.fetchall() 

                getApproverName=connection.cursor()
                getApproverName.execute("select UserName from tb_User  WHERE UserID='{value}';".format(value=uid) )
                getApproverName=getApproverName.fetchall() 
                print(getApproverName)


                userName=connection.cursor()
                userName.execute("select UserName from tb_User where UserID='{val}'".format(val=getuserid[0][0]))
                userName=userName.fetchall()
                UN=userName[0][0]

                video = TbStatus(userid=TbUser.objects.get(userid=getuserid[0][0]),videoid=id,status='Rejected',reason=l,videoname=vN,approver=getApproverName[0][0],uploadername=UN,platform=pN)   
                # video = Status(userid=TbUser.objects.get(userid=getuserid[0][0]),VideoID=id,status='Rejected',reason=l,VideoName=vN,ApproverName=getApproverName[0][0])
                video.save() 

                # ____new Delete lines added here__
                deleteQuestionsres=connection.cursor()
                deleteQuestionsres.execute("DELETE CampaignQuestionResponse FROM CampaignQuestionResponse inner join tb_CampaignQuestion on CampaignQuestionResponse.CampaignQuestionID = tb_CampaignQuestion.CampaignQuestionID WHERE tb_CampaignQuestion.CampaignVideoID='{value}';".format(value=id))
                # deleteQuestions.execute("DELETE FROM CampaignQuestionResponse CQR inner join tb_CampaignQuestion CQ on CQ.CampaignQuestionID = CQR.CampaignQuestionID WHERE CQ.CampaignVideoID='{value}';".format(value=id))
                
                
                # This for deleting videoID
                # deleteQuestions=connection.cursor()
                # deleteQuestions.execute("DELETE tb_CampaignQuestion WHERE CampaignVideoID='{value}';".format(value=id))

                # deleteCampVideo=connection.cursor()
                # deleteCampVideo.execute("DELETE tb_CampaignVideo WHERE CampaignVideoID='{value}';".format(value=id))
                messages.error(request, 'rejected succesfully')
                return redirect('/dm/approver/'+str(uid))
        # return render(request,'tc_DigitalMarketing/approverview.html',{})
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

        # ___This for get question and responces__
        cursor=connection.cursor()
        cursor.execute("select QuestionText,Response from CampaignQuestionResponse cqr inner join tb_CampaignQuestion cquestion on cqr.CampaignQuestionID = cquestion.CampaignQuestionID AND cquestion.CampaignVideoID ='{value}' inner join tb_Question question on cquestion.QuestionID = question.QuestionID;".format(value=CVID))
        result=cursor.fetchall()
        print(result)

        cursor1=connection.cursor()
        cursor1.execute("select VideoPath,VideoTranscription,VideoName from CampaignVideo cv inner join tb_Video v on v.VideoID=cv.VideoID AND cv.CampaignVideoID='{val}'".format(val=CVID))
        VideoDeatails=cursor1.fetchall()
        vP='/'+VideoDeatails[0][0]
        vT=VideoDeatails[0][1]
        vN=VideoDeatails[0][2]
        return render(request,'tc_DigitalMarketing/approverview.html',{'qT':questionsText,'qR':QuestionResponse,'R':result,'video':vP,'Transcribe':vT,'vname':vN,'id':uid})
    

def status(request,id):
    if request.method == "POST":
        return render(request,'tc_DigitalMarketing/createrupload.html')
    else:
        status=TbStatus.objects.filter(userid=id)
        return render(request,'tc_DigitalMarketing/status.html',{'status':status,'id':id})
    
def statusview(request,id,id1):
    if request.method == "POST":
        return render(request,'tc_DigitalMarketing/createrupload.html')
    else:
        # status=Status.objects.filter(userid=id)
        print(id1)
        status=connection.cursor()
        status.execute("select reason FROM tb_Status WHERE userid='{value}' AND VideoID='{value1}';".format(value=id,value1=id1))
        response=status.fetchall()

        cursor1=connection.cursor()
        cursor1.execute("select VideoPath,VideoName from CampaignVideo cv inner join tb_Video v on v.VideoID=cv.VideoID AND cv.CampaignVideoID='{val}'".format(val=id1))
        VideoDeatails=cursor1.fetchall()
        vP='/'+VideoDeatails[0][0]
        vName=VideoDeatails[0][1]

        import ast
        res = ast.literal_eval(response[0][0])
        return render(request,'tc_DigitalMarketing/statusview.html',{'approverres':res[0],'reason':res[1],'id':id,'video':vP,'vname':vName,'vid':id1,})
    

def Download(request):
    if request.method == "POST":
        return render(request,'tc_DigitalMarketing/Download.html',{'approvedvid':approvedvid,})
    else:
        approvedvid=TbApprove.objects.all()
        return render(request,'tc_DigitalMarketing/Download.html',{'approvedvid':approvedvid,})
    
def Downloadvideo(request,id):
        cursor1=connection.cursor()
        cursor1.execute("select VideoPath,VideoTranscription,VideoName from CampaignVideo cv inner join tb_Video v on v.VideoID=cv.VideoID AND cv.CampaignVideoID='{val}'".format(val=id))
        VideoDeatails=cursor1.fetchall()
        vP='/'+VideoDeatails[0][0]
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = BASE_DIR+vP
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

def Deletevideo(request,id,id1):
        cursor1=connection.cursor()
        cursor1.execute("select VideoName from CampaignVideo cv inner join tb_Video v on v.VideoID=cv.VideoID AND cv.CampaignVideoID='{val}'".format(val=id))
        VideoDeatails=cursor1.fetchall()
        vName=VideoDeatails[0][0]

        getpath=connection.cursor()
        getpath.execute("SELECT VideoPath FROM tb_Video WHERE videoID='{value}';".format(value=id))
        getpath=getpath.fetchall()
        v_path=getpath[0][0]
        print(v_path)

        deletestatus=connection.cursor()
        deletestatus.execute("DELETE FROM DigitalMarketing_status WHERE videoID='{value}';".format(value=id))

        deleteQuestionsres=connection.cursor()
        deleteQuestionsres.execute("DELETE CampaignQuestionResponse FROM CampaignQuestionResponse inner join tb_CampaignQuestion on CampaignQuestionResponse.CampaignQuestionID = tb_CampaignQuestion.CampaignQuestionID WHERE tb_CampaignQuestion.CampaignVideoID='{value}';".format(value=id))
        # deleteQuestions.execute("DELETE FROM CampaignQuestionResponse CQR inner join tb_CampaignQuestion CQ on CQ.CampaignQuestionID = CQR.CampaignQuestionID WHERE CQ.CampaignVideoID='{value}';".format(value=id))
        
        
        # This for deleting videoID
        deleteQuestions=connection.cursor()
        deleteQuestions.execute("DELETE tb_CampaignQuestion WHERE CampaignVideoID='{value}';".format(value=id))

        deleteCampVideo=connection.cursor()
        deleteCampVideo.execute("DELETE CampaignVideo WHERE VideoID='{value}';".format(value=id))
       
        video=connection.cursor()
        video.execute("DELETE tb_Video WHERE VideoID='{value}';".format(value=id))

        video=connection.cursor()
        video.execute("DELETE DigitalMarketing_video WHERE Title='{value}';".format(value=vName))

        os.remove(v_path)
        messages.error(request, 'Video Details Deleted succesfully')
        return redirect('/dm/createrupload/'+str(id1))



