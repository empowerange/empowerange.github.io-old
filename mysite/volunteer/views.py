from django.shortcuts import render
from volunteer.forms import UserForm
 
 

def register(request):

    registered = False

    if request.method =="POST" :
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            ngo = user_form.cleaned_data['ngo'] #getting the list of the ngos. 

            user = user_form.save()
             
            user.save()

            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'volunteer/volunteer.html',
                             {'user_form':user_form,
                              'registered':registered})


 



     
          


        
