from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
# from new_app.models import info,Document
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import matplotlib.pyplot as plt
import pickle
import keras
from keras.preprocessing import image
import numpy as np
from keras.applications.vgg19 import decode_predictions
from keras.applications import MobileNet

# from .models import ModelWithFileField
# Create your views here


model=pickle.load(open('pick.pkl','rb'))


def intro(request):
    return render(request,'intro.html')
def home(request):    

    # if request.user.is_anonymous:
    #     return redirect('/login')
    # else:
 
       return render(request,'home.html')


def predict(request):
    if request.method == 'POST' and request.FILES['image']:
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        # img=Document(document=myfile)
        # img.save()
        uploaded_file_url = fs.url(filename)
        # print(uploaded_file_url)
        
        import keras.backend.tensorflow_backend as tb
        tb._SYMBOLIC_SCOPE.value = True
        
        img='.'+uploaded_file_url
        # test_image=[]
        img=image.load_img(img,target_size=(224,224,3))
        img=image.img_to_array(img)
        img=img/255
        img=img.reshape(1,224,224,3)
        # test_image.append(img)
        # img=np.array(img)
        # img=preprocess_input(img)
        # plt.imshow(img.reshape(224,224,3))
        
        pred=model.predict(img)
        predictions=decode_predictions(pred,top=3)
        predictions=np.array(predictions)[0][0:][0:,1:]
        ans=1
        # print(predictions)
        # return render(request, 'home.html', {
        #     'uploaded_file_url': uploaded_file_url
        # })
        context={'predictions':predictions,'image':uploaded_file_url,'ans':ans}
    return render(request,'home.html',context)


# def signin(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=authenticate(username=username,password=password)
#         if user is not None:
#             INFO=info(username=username,password=password)
#             # INFO.save()
#             login(request,user)
#             return redirect('/home')
#         else:
#             return render(request,'login.html')

#     else:
#         return render(request,'login.html')
    
# def signout(request):
#     logout(request)
#     return redirect('/')

  