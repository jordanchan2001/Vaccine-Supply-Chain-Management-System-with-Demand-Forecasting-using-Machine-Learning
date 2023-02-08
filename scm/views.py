from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.db.models import Count
from .models import Profile,Vaccine,Cart,CartItems,Shipment,SupplyChain
import os
import datetime
import csv
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# from django.http import HttpResponse

def data(name,time,pfizer_count,sinovac_count,az_count,sender):
    hospital = Profile.objects.get(name = name)
    hospital_cart = Cart.objects.create(user=hospital.user)
    shipment_time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M")
    hospital_cart_items = CartItems.objects.create(cart = hospital_cart,vaccine_name='Pfizer',vaccine_quantity = pfizer_count)
    hospital_cart_items2 = CartItems.objects.create(cart = hospital_cart,vaccine_name='Sinovac',vaccine_quantity = sinovac_count)
    hospital_cart_items3 = CartItems.objects.create(cart = hospital_cart,vaccine_name='AstraZeneca',vaccine_quantity = az_count)
    hospital_supply_chain = SupplyChain.objects.create(ownership=hospital,time_created = shipment_time, 
                                                        origin =sender,cart = hospital_cart,issue=True)
    hospital_shipment = Shipment.objects.create(sender = sender,receiver = hospital.name,
                                                time_shipment = shipment_time,supply_chain = hospital_supply_chain, status ='Accepted' )
    hospital_cart.save()
    hospital_cart_items.save()
    hospital_cart_items2.save()
    hospital_cart_items3.save()
    hospital_supply_chain.save()
    hospital_shipment.save()

def user_data(username,email,password,name,role,profileimg,location):

    new_user = User.objects.create_user(username=username,email=email,password=password)
    new_profile = Profile.objects.create(user=new_user,id_user=new_user.id,name=name
                    ,role=role,profileimg = profileimg,
                    location=location)
    new_user.save()
    new_profile.save()

def vaccine_data(name,disease,dosage):
    new_vaccine = Vaccine.objects.create(name=name,disease=disease,dosage=dosage)
    new_vaccine.save()

def insert_data():

    # User.objects.all().exclude(username='admin').delete()
    # Profile.objects.all().delete()
    # Vaccine.objects.all().delete()
    # Shipment.objects.all().delete()
    # SupplyChain.objects.all().delete()
    # Cart.objects.all().delete()
    # CartItems.objects.all().delete()

    #User Data
    user_data('bioangle','bio_angle07@gmail.com','bioangle','Bio Angle Vacs Sdn Bhd','Manufacturer','profile_images/bioangle_logo.png','Universiti Putra Malaysia (UPM), UNIT D-G-1 & UNIT D-G-3, BLOCK D, UPM-MTDC TECHNOLOGY CENTRE III, 43400 Serdang, Selangor')
    user_data('vaccinex123','vaccine_x@hotmail.com','vaccinex123','Vaccine X Malaysia Sdn Bhd','Manufacturer','profile_images/vaccinex_logo.png','Wisma Averis Tower 2, 8, Jalan Kerinchi, Bangsar South, 59200 Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur')
    user_data('desapark123','parkcity@gmail.com','desapark123','ParkCity Medical Centre','Hospital','profile_images/parkcity_logo.jpg','Perdana, 2, Jalan Intisari, Desa Parkcity, 52200 Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur')
    user_data('mvp123','mvp123@gmail.com','mvp123','MVP- Pharmaceuticals Sdn Bhd','Manufacturer','profile_images/mvp_logo.png','Lot 11182, Jalan Pulau Meranti, 47100 Puchong, Selangor')
    user_data('sunway123','sunway_medical@gmail.com','sunway123','Sunway Medical Centre','Hospital','profile_images/sunway_logo.jpg','5, Jalan Lagoon Selatan, Bandar Sunway, 47500 Petaling Jaya, Selangor')
    
    #Vaccine Data
    vaccine_data('AstraZeneca','COVID-19',2)
    vaccine_data('Sinovac','COVID-19',3)
    vaccine_data('Pfizer','COVID-19',3)
    
    #2021-02
    data('ParkCity Medical Centre','2021-02-01 08:15',115,56,15,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2021-02-01 08:15',1205,250,125,'Bio Angle Vacs Sdn Bhd')

    #2021-03
    data('ParkCity Medical Centre','2021-03-01 08:15',2865,1402,375,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2021-03-01 08:15',2812,1201,344,'Vaccine X Malaysia Sdn Bhd')

    #2021-04
    data('ParkCity Medical Centre','2021-04-01 08:15',2534,1246,332,'MVP- Pharmaceuticals Sdn Bhd')
    data('Sunway Medical Centre','2021-04-01 08:15',2121,1020,501,'Bio Angle Vacs Sdn Bhd')

    #2021-05
    data('ParkCity Medical Centre','2021-05-01 08:15',6375,3135,836,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2021-05-01 08:15',5890,3212,910,'MVP- Pharmaceuticals Sdn Bhd')

    #2021-06
    data('ParkCity Medical Centre','2021-06-01 08:15',24495,12046,3212,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2021-06-01 08:15',28190,8900,3191,'MVP- Pharmaceuticals Sdn Bhd')

    #2021-07
    data('ParkCity Medical Centre','2021-07-01 08:15',50323,24749,6599,'MVP- Pharmaceuticals Sdn Bhd')
    data('Sunway Medical Centre','2021-07-01 08:15',47212,22000,3121,'Vaccine X Malaysia Sdn Bhd')

    #2021-08
    data('ParkCity Medical Centre','2021-08-01 08:15',36720,18059,4815,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2021-08-01 08:15',31212,21212,8211,'MVP- Pharmaceuticals Sdn Bhd')

    #2021-09
    data('ParkCity Medical Centre','2021-09-01 08:15',23364,11490,3064,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2021-09-01 08:15',31212,21212,8211,'Vaccine X Malaysia Sdn Bhd')

    #2021-10
    data('ParkCity Medical Centre','2021-10-01 08:15',9094,4472,1192,'MVP- Pharmaceuticals Sdn Bhd')
    data('Sunway Medical Centre','2021-10-01 08:15',15012,4121,1010,'Vaccine X Malaysia Sdn Bhd')

    #2021-11
    data('ParkCity Medical Centre','2021-11-01 08:15',1066,524,139,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2021-11-01 08:15',4912,1121,281,'Bio Angle Vacs Sdn Bhd')

    #2021-12
    data('ParkCity Medical Centre','2021-12-01 08:15',628,309,82,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2021-12-01 08:15',2011,450,120,'Bio Angle Vacs Sdn Bhd')

    #2022-01
    data('ParkCity Medical Centre','2022-01-01 08:15',324,159,42,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2022-01-01 08:15',1001,230,90,'Bio Angle Vacs Sdn Bhd')

    #2022-02
    data('ParkCity Medical Centre','2022-02-01 08:15',5754,2829,754,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2022-02-01 08:15',6500,2911,1211,'Bio Angle Vacs Sdn Bhd')

    #2022-03
    data('ParkCity Medical Centre','2022-03-01 08:15',3062,1506,401,'Vaccine X Malaysia Sdn Bhd')
    data('Sunway Medical Centre','2022-03-01 08:15',3211,2011,610,'Bio Angle Vacs Sdn Bhd')

    #2022-04
    data('ParkCity Medical Centre','2022-04-01 08:15',1642,807,215,'Vaccine X Malaysia Sdn Bhd')
    data('Sunway Medical Centre','2022-04-01 08:15',2001,821,340,'Bio Angle Vacs Sdn Bhd')

    #2022-05
    data('ParkCity Medical Centre','2022-05-01 08:15',1352,665,177,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2022-05-01 08:15',1675,712,340,'Bio Angle Vacs Sdn Bhd')

    #2022-06
    data('ParkCity Medical Centre','2022-06-01 08:15',1190,193,125,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2022-06-01 08:15',875,72,34,'Bio Angle Vacs Sdn Bhd')

    #2022-07
    data('ParkCity Medical Centre','2022-07-01 08:15',880,120,120,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2022-06-01 08:15',710,120,66,'Bio Angle Vacs Sdn Bhd')

    #2022-08
    data('ParkCity Medical Centre','2022-08-01 08:15',721,120,90,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2022-08-01 08:15',680,109,28,'Bio Angle Vacs Sdn Bhd')

    #2022-09
    data('ParkCity Medical Centre','2022-09-01 08:15',621,110,17,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2022-09-01 08:15',560,102,21,'Bio Angle Vacs Sdn Bhd')

    #2022-10
    data('ParkCity Medical Centre','2022-10-01 08:15',500,40,8,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2022-10-01 08:15',402,99,19,'Bio Angle Vacs Sdn Bhd')

    #2022-11
    data('ParkCity Medical Centre','2022-11-01 08:15',450,350,40,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2022-11-01 08:15',321,88,44,'Bio Angle Vacs Sdn Bhd')

    #2022-12
    data('ParkCity Medical Centre','2022-12-01 08:15',600,200,101,'Bio Angle Vacs Sdn Bhd')
    data('Sunway Medical Centre','2022-12-01 08:15',302,65,32,'Bio Angle Vacs Sdn Bhd')

def login(request):
    
    #insert_data()  #dummy data
    
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user =  auth.authenticate(username=username,password=password)

        if not username and not password:
            messages.info(request,"Please insert the credentials!",extra_tags='error')
            return redirect('login')
        elif not username:
            messages.info(request,"Please insert the username!",extra_tags='error')
            return redirect('login')
        elif not password:
            messages.info(request,"Please insert the password!",extra_tags='error')
            return redirect('login')
        
        if user is not None:
            profile = Profile.objects.get(user = user)
            if profile.status =='Active':
                auth.login(request,user)
                if profile.role =='Manufacturer':
                    messages.info(request,"Login Successfully!",extra_tags='success')
                    return redirect('dashboard_manufacturer')
                elif profile.role =='Hospital':
                    messages.info(request,"Login Successfully!",extra_tags='success')
                    return redirect('dashboard_hospital')
                else:
                    messages.info(request,"Login Successfully!",extra_tags='success')
                    return redirect('dashboard')
            elif profile.status =='Inactive':   
                messages.info(request,"Account Not Activated!",extra_tags='error')
                return redirect('login')
        else:
            messages.info(request,"Credentials Invalid!",extra_tags='error')
            return redirect('login')
    else:

        return render(request,'scm/login.html')

def register(request):
    context={}
    if request.method =='POST':
        username= request.POST['username']
        name = request.POST['name']
        email= request.POST['email']
        user_type= request.POST['user_type']
        location= request.POST['location']
        password= request.POST['password']
        if not username :
            messages.info(request,'Username field is empty!',extra_tags='error')
            return redirect('register')
        elif not name:
            messages.info(request,'Name field is empty!',extra_tags='error')
            return redirect('register')
        elif not email:
            messages.info(request,'Email field is empty!',extra_tags='error')
            return redirect('register')
        elif not location:
            messages.info(request,'Location field is empty!',extra_tags='error')
            return redirect('register')
        elif not password:
            messages.info(request,'Password field is empty!',extra_tags='error')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Taken!',extra_tags='error')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request,"Username Taken!",extra_tags='error')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            user_model = User.objects.get(username=username)
            new_profile = Profile.objects.create(user=user_model,id_user=user_model.id,name=name,role=user_type,location=location)
            new_profile.save()
            messages.info(request,'Account Successfully Registered!',extra_tags='success')
            return redirect('login')
    else:    
        return render(request,'scm/register.html',context)

def logout(request):
    auth.logout(request)
    messages.info(request,"Logout Successfully",extra_tags='success')
    return redirect('login')
    
def dashboard(request):
    profiles_count = Profile.objects.all().count()-1
    vaccines_count = Vaccine.objects.all().count()
    shipments_count = SupplyChain.objects.all().count() 
    profiles = Profile.objects.all().order_by('-id_user')[:5]
    shipments = SupplyChain.objects.all().order_by('-id')[:5]
    carts_items_list =[]
    for shipment in shipments :
        cart_items= CartItems.objects.filter(cart=shipment.cart)
        for item in cart_items:
            carts_items_list.append(item)
    context={'profiles_count':profiles_count,'vaccines_count':vaccines_count,
            'shipments_count':shipments_count,'profiles':profiles,
            'shipments':shipments,'carts_items_list':carts_items_list}
    return render(request, 'scm/admin_dashboard.html',context)

def users(request):
    profiles = Profile.objects.all().order_by('id_user').exclude(role ='Admin')
    context={'profiles':profiles}
    return render(request, 'scm/admin_users.html',context)

def edit(request, id):  
    user = Profile.objects.get(id_user=id)
    context={'selectedprofile':user}
    return render(request,'scm/admin_edit_users.html', context)

def update(request,id):
    profile = Profile.objects.get(id_user = id)
    if request.method =='POST':
        username= request.POST['username']
        email= request.POST['email']
        role= request.POST['user_type']    
        location= request.POST['location']
        if User.objects.filter(email=request.POST['email']).exists() and profile.user.email != request.POST['email'] :
            messages.info(request,'Email Taken!',extra_tags='error')
            return render(request,'scm/admin_edit_users.html', {'selectedprofile':profile})
        elif User.objects.filter(username=request.POST['username']).exists() and profile.user.username != request.POST['username'] :
            messages.info(request,"Username Taken!",extra_tags='error')
            return render(request,'scm/admin_edit_users.html', {'selectedprofile':profile})
        elif not username : 
            messages.info(request,"Username is empty!",extra_tags='error')
            return render(request,'scm/admin_edit_users.html', {'selectedprofile':profile})
        elif not email : 
            messages.info(request,"Email is empty!",extra_tags='error')
            return render(request,'scm/admin_edit_users.html', {'selectedprofile':profile}) 
        elif not location : 
            messages.info(request,"Location is empty!",extra_tags='error')
            return render(request,'scm/admin_edit_users.html', {'selectedprofile':profile})  
        else:
            profile.user.username= username
            profile.user.email= email
            profile.role= role
            profile.location= location
            try :
                password = request.POST['password']
                if password:
                    profile.user.set_password(password)
                    profile.user.save()
                    auth.logout(request)
                    user =  auth.authenticate(username=profile.user.username,password=password)
                    auth.login(request,user)
            except KeyError:
                pass
            profile.user.save()
            profile.save()
            messages.info(request,"Profile successfully updated! ",extra_tags='success')
            return redirect('users')

def delete(request,id):
    profile = Profile.objects.get(id_user=id)
    profile.user.delete()
    profile.delete()
    messages.info(request,"Profile successfully deleted!",extra_tags='success')
    return redirect ('users')

def activate(request,id):
    profile = Profile.objects.get(id_user=id)
    if profile.status == 'Inactive':
        profile.status = 'Active'
        profile.save()
        messages.info(request,"Profile successfully activated!",extra_tags='success')
    else:
        messages.info(request,"Profile is already activated!!",extra_tags='error')
    return redirect ('users')

def vaccines(request):  
    vaccines = Vaccine.objects.all()
    context={'vaccines':vaccines}   
    return render(request, 'scm/admin_vaccines.html',context)

def show_vaccine_form(request):
    return render(request, 'scm/admin_add_vaccine.html')

def add_vaccine(request):
    context={}
    if request.method =='POST':
        vaccine_name= request.POST['name']
        disease = request.POST['disease']
        dosage = request.POST['dosage']
        if not vaccine_name:
            messages.info(request,'Vaccine Name is empty!',extra_tags='error')
            return redirect('show_vaccine_form')
        elif not disease:
            messages.info(request,'Disease Name is empty!',extra_tags='error')
            return redirect('show_vaccine_form')
        elif not dosage:
            messages.info(request,'Dosage is empty!',extra_tags='error')
            return redirect('show_vaccine_form')
        elif Vaccine.objects.filter(name=vaccine_name).exists():
            messages.info(request,'The vaccine name is registered!',extra_tags='error')
            return redirect('show_vaccine_form')
        else:
            try:
                dosage = int(request.POST['dosage'])
                if not (1 <= dosage <=10):
                    messages.info(request,'Please insert dosage number between 1-10',extra_tags='error')
                    return redirect('show_vaccine_form')
            except ValueError:
                messages.info(request,'Please enter integer for dosage!',extra_tags='error')
                return redirect('show_vaccine_form')
            new_vaccine = Vaccine.objects.create(name=vaccine_name,disease=disease,dosage=dosage)
            new_vaccine.save()
            messages.info(request,'Vaccine Successfully Registered!',extra_tags='success')
            return redirect('vaccines')
    else:    
        return redirect('vaccines')
        
def edit_vaccine(request, name):  
    vaccine = Vaccine.objects.get(name=name)
    context={'selectedvaccine':vaccine}
    return render(request,'scm/admin_edit_vaccine.html', context)

def update_vaccine(request,name):
    vaccine = Vaccine.objects.get(name=name)
    if request.method =='POST':
        vac_name = request.POST['name']
        disease = request.POST['disease']
        dosage = request.POST['dosage']

        if not vac_name:
            messages.info(request,'Vaccine Name is empty!',extra_tags='error')
            return redirect('show_vaccine_form')
        elif not disease:
            messages.info(request,'Disease Name is empty!',extra_tags='error')
            return redirect('show_vaccine_form')
        elif not dosage:
            messages.info(request,'Dosage is empty!',extra_tags='error')
            return redirect('show_vaccine_form')
        elif Vaccine.objects.filter(name=request.POST['name']).exists() and vaccine.name != request.POST['name'] :
            messages.info(request,'Vaccine name is registered!!',extra_tags='error')
            return render(request,'scm/admin_edit_vaccine.html', {'selectedvaccine':vaccine})
        
        else:
            try:
                dosage = int(request.POST['dosage'])
                if not (1 <= dosage <=10):
                    messages.info(request,'Please insert dosage number between 1-10',extra_tags='error')
                    return render(request,'scm/admin_edit_vaccine.html', {'selectedvaccine':vaccine})
            except ValueError:
                messages.info(request,'Please enter integer for dosage!',extra_tags='error')
                return render(request,'scm/admin_edit_vaccine.html', {'selectedvaccine':vaccine})
            vaccine.name= vac_name
            vaccine.disease = disease
            vaccine.dosage = dosage
            vaccine.save()
            messages.info(request,"Vaccine successfully updated! ",extra_tags='success')
            vaccines = Vaccine.objects.all()
            return render(request, 'scm/admin_vaccines.html',{'vaccines':vaccines})

def delete_vaccine(request,name):
    vaccine = Vaccine.objects.get(name=name)
    vaccine.delete()
    messages.info(request,"Vaccine successfully deleted!",extra_tags='success')
    return redirect ('vaccines')

def shipments(request):
    shipments = SupplyChain.objects.all()
    carts_items_list =[]
    ownerships_list=[]
    for shipment in shipments :
        cart_items= CartItems.objects.filter(cart=shipment.cart)
        for item in cart_items:
            carts_items_list.append(item)
    for shipment in shipments :
        ships = Shipment.objects.filter(supply_chain = shipment)
        for ship in ships:
            ownerships_list.append(ship)
        
    profiles = Profile.objects.all()

    context={'profiles':profiles,'shipments':shipments,'carts_items_list':carts_items_list,'ownerships_list':ownerships_list}   
    return render(request, 'scm/admin_shipments.html',context)

def analysts(request):
    # # shipments = SupplyChain.objects.filter(issue=True).values('ownership').order_by('ownership').annotate(count=Count('ownership'))
    # shipments = SupplyChain.objects.filter(issue=True)
    # data =[]
    # for shipment in shipments : 
    #     cart_items = CartItems.objects.filter(cart = shipment.cart)
    #     total_quantity = 0 
    #     for cart_item in cart_items:
    #         total_quantity += cart_item.vaccine_quantity    
    #     data.append((shipment.ownership.name,total_quantity))
    
    # counts = {}
    # for t in data:
    #     element, count = t
    #     if element not in counts:
    #         counts[element] = count
    #     else:
    #         counts[element] += count
    
    # result = [(k, v) for k, v in counts.items()]

    # print(result)
    # csv_header = ['Hospital','Production']
    # with open('data.csv', 'w') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(csv_header)
    #     for res in result :
    #         writer.writerow(res)
    # rows.append([hospital_name, month, vaccine_quantity])

    
    # months = []
    # years = []
    # for shipment in shipments:
    #     months.append(shipment.time_created.strftime("%m"))
    #     years.append(shipment.time_created.strftime("%Y"))
    # months = list(dict.fromkeys(months))
    # years = list(dict.fromkeys(years))

    shipments = SupplyChain.objects.filter(issue=True)
    data=[]
    for shipment in shipments:
        cart_items = CartItems.objects.filter(cart = shipment.cart)
        month = shipment.time_created.strftime("%Y")+ "-" + shipment.time_created.strftime("%m")
        total_quantity = 0
        for cart_item in cart_items:
            total_quantity += cart_item.vaccine_quantity
        data.append((shipment.ownership.name,month,total_quantity))

    visits_by_center_and_month = {}
    for t in data:
        center, month, visits = t
        if center not in visits_by_center_and_month:
            visits_by_center_and_month[center] = {}
        if month in visits_by_center_and_month[center]:
            visits_by_center_and_month[center][month] += visits
        else:
            visits_by_center_and_month[center][month] = visits

    new_data = []
    for center, visits_by_month in visits_by_center_and_month.items():
        if len(visits_by_month) >= 12:
            for month, visits in visits_by_month.items():
                new_data.append((center, month, visits))
     
    csv_header = ['Hospital','Month','Vaccination']
    with open('data.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(csv_header)
        for dat in new_data :
            writer.writerow(dat)
    df = pd.read_csv('data.csv')
    df.drop('Hospital',axis=1)


    #Machine Learning Demand Forecasting Model
    df = pd.read_csv('data.csv',index_col='Month',parse_dates=True)
    hospital_names = df['Hospital'].unique()

    # Create a dictionary to store the DataFrames,models for each hospital
    hospital_dfs = {}
    hospital_models = {}
    hospital_forecast_data ={}

    # Iterate over the hospital names
    for hospital in hospital_names:
        # Create a DataFrame for the current hospital
        hospital_df = df[df['Hospital'] == hospital]
        
        # Add the DataFrame to the dictionary
        hospital_dfs[hospital] = hospital_df

    # Print the DataFrames for each hospital
    for hospital, hospital_df in hospital_dfs.items():
        # print(f'DataFrame for {hospital}:')
        # print(hospital_df)
        # print()

        hospital_df = hospital_df.drop(['Hospital'],axis=1)
        hospital_df['Vaccination_LastMonth']=hospital_df['Vaccination'].shift(+1)
        hospital_df['Vaccination_2Monthsback']=hospital_df['Vaccination'].shift(+2)
        hospital_df['Vaccination_3Monthsback']=hospital_df['Vaccination'].shift(+3)
        hospital_df = hospital_df.dropna()

        print(f'DataFrame for {hospital}:')
        print(hospital_df)

        
        model=RandomForestRegressor(n_estimators=100,max_features=3, random_state=1)
        x = hospital_df.drop(['Vaccination'],axis=1)
        y= hospital_df.Vaccination.values
        model.fit(x,y)
        hospital_models[hospital] = model
        pred=model.predict(x)
        
        
        plt.rcParams["figure.figsize"] = (12,8)
        plt.plot(pred,label='Predictions')
        plt.plot(hospital_df.Vaccination.values,label='Actual Vaccination')
        plt.legend(loc="upper left")
        plt.xlabel('Months')
        plt.title('Demand Forecasting of ' + hospital)
        plot_filename = f'static/images/{hospital}.png'
        if os.path.exists(plot_filename):
            os.remove(plot_filename)

        plt.savefig(plot_filename)
        plt.clf()


        forecast_data = pd.DataFrame({'Vaccination_LastMonth':hospital_df['Vaccination'].iloc[-1],
                        'Vaccination_2Monthsback':hospital_df['Vaccination'].iloc[-2],
                        'Vaccination_3Monthsback':hospital_df['Vaccination'].iloc[-3]},
                  index=['2023-01-01'])
        forecast_data.index.freq = 'MS'
        forecast = model.predict(forecast_data)
        hospital_forecast_data[hospital] = forecast[0]
        
        
    print (hospital_forecast_data)
    hospitals = Profile.objects.filter(role = 'Hospital')
    loginUser = Profile.objects.get(user = request.user)
    context = {'hospitals':hospitals,'forecast_data':hospital_forecast_data,'loginUser':loginUser}
    if loginUser.role == 'Admin':
        return render(request, 'scm/admin_analysts.html',context)
    elif loginUser.role =='Hospital':
        return render(request, 'scm/hospital_analysts.html',context)

#Manufacturer Screens
def dashboard_manufacturer(request):
    profile = Profile.objects.get(user=request.user)
    shipments_onhand_count = SupplyChain.objects.filter(ownership = profile).count()
    requests_inprogress_count = Shipment.objects.filter(sender = profile.name,status='In Progress').exclude(status = 'N/A').count()
    requests_received_count = Shipment.objects.filter(receiver = profile.name,status='In Progress').count()
    shipments = Shipment.objects.filter(sender = profile.name).exclude(status = 'N/A').order_by('-supply_chain')[:5]
    carts_items_list2 =[]
    carts_items_list =[]
    for shipment in shipments:
        cart_items= CartItems.objects.filter(cart=shipment.supply_chain.cart)
        for item in cart_items:
            carts_items_list.append(item)

    ships = SupplyChain.objects.filter(ownership = profile).order_by('-id')[:5]
    carts_items_list2 =[]
    for ship in ships :
        cart_items= CartItems.objects.filter(cart=ship.cart)
        for item in cart_items:
            carts_items_list2.append(item)

    context={'shipments_onhand_count':shipments_onhand_count, 'requests_inprogress_count':requests_inprogress_count,
            'requests_received_count':requests_received_count,'loginUser':profile,
            'shipments':shipments,'carts_items_list':carts_items_list,
            'ships':ships,'carts_items_list2':carts_items_list2}
    return render(request, 'scm/manufacturer_dashboard.html',context)

def show_profile_setting(request):
    profile = Profile.objects.get(user = request.user)
    context = {'loginUser' : profile}
    
    if profile.role == 'Manufacturer':
        return render(request, 'scm/manufacturer_profile_setting.html',context)
    elif profile.role == 'Hospital':
        return render(request, 'scm/hospital_profile_setting.html',context)

def update_profile(request):
    profile = Profile.objects.get(user = request.user)
    if request.method =='POST':
        email= request.POST['email']    
        location= request.POST['location']
        username = request.POST['hidden_username']
        if not email :
            messages.info(request,'Email is empty!',extra_tags='error')
            return redirect('show_profile_setting')
        elif not location:
            messages.info(request,'Location is empty!',extra_tags='error')
            return redirect('show_profile_setting')
        elif User.objects.filter(email=request.POST['email']).exists() and profile.user.email != request.POST['email'] :
            messages.info(request,'Email Taken!',extra_tags='error')
            return redirect('show_profile_setting')
        else:
            profile.user.email= request.POST['email']    
            profile.location= request.POST['location']
            username = request.POST['hidden_username']
            try :
                password = request.POST['password']
                if password:
                    profile.user.set_password(password)
                    profile.user.save()
                    auth.logout(request)
                    user =  auth.authenticate(username=username,password=password)
                    auth.login(request,user)
            except KeyError:
                pass
            try :
                profileImg_save = request.FILES['profileImg']
                if profileImg_save:
                    profile.profileimg= profileImg_save
            except KeyError:
                pass
            
            profile.user.save()
            profile.save()
            messages.info(request,"Profile successfully updated! ",extra_tags='success')
            return redirect('show_profile_setting')
   
def create_shipment(request):
    profile = Profile.objects.get(user=request.user)
    vaccines = Vaccine.objects.all()
    cart, created = Cart.objects.get_or_create(user = request.user, completed = False)
    cart_items_list = CartItems.objects.filter(cart = cart)
    if request.method =='POST':
        action = request.POST['action']
        if  action == 'Add':
            vaccine_name= request.POST['vaccine_name']
            try:
                vaccine_quantity= request.POST['quantity']
                if not vaccine_quantity:
                    messages.info(request,"Please insert all the details! ",extra_tags='error')
                else:
                    CartItems.objects.create(cart = cart, vaccine_name = vaccine_name,vaccine_quantity= vaccine_quantity)
                    cart_items_list = CartItems.objects.filter(cart = cart)
                    messages.info(request,"Vaccine successfully added into cart! ",extra_tags='success')
            except ValueError:
                messages.info(request,"Please insert integer for quantity! ",extra_tags='error')
        elif action == 'Clear Cart':
            if CartItems.objects.filter(cart=cart).exists():
                CartItems.objects.filter(cart = cart).delete()
                cart_items_list = None
                messages.info(request,"Cart is succesfully cleared! ",extra_tags='success')
            else:
                messages.info(request,"Cart is already empty! ",extra_tags='error')
        elif action == 'Confirm':
            if CartItems.objects.filter(cart=cart).exists():
                profile = Profile.objects.get(user=request.user)
                supply_chain = SupplyChain.objects.create(ownership =profile,origin = profile.name, cart = cart)
                Shipment.objects.create(sender = profile.name,supply_chain=supply_chain)
                processed_cart = Cart.objects.get(user = request.user, completed = False)
                processed_cart.completed=True
                processed_cart.save()
                cart_items_list = None
                messages.info(request,"Shipment is succesfully created! ",extra_tags='success')
            else:
                messages.info(request,"Cart is empty! ",extra_tags='error')

    context={'cartitems': cart_items_list,'vaccines':vaccines,'loginUser':profile}
    return render(request, 'scm/manufacturer_create_shipment.html',context)

def delete_cart_item(request,id):
    cart_items = CartItems.objects.get(id=id)
    cart_items.delete()
    messages.info(request,"Cart Item successfully deleted!",extra_tags='success')
    return redirect ('create_shipment')

def transfer_shipment(request):
    profile = Profile.objects.get(user=request.user)
    shipments = SupplyChain.objects.filter(ownership = profile,status_transferring = False)
    receivers = Profile.objects.all().exclude(role = 'Admin').exclude(name=profile.name)
    if request.method =='POST':
        try:
            shipment_id = request.POST['shipmentID']
            receiver_name = request.POST['receiver_name']
        except:
            messages.info(request,"Please select all the details! ",extra_tags='error')
        else:
            selected_supplychain = SupplyChain.objects.get(id = shipment_id)
            selected_supplychain.status_transferring = True
            selected_shipment = Shipment.objects.get(sender=profile.name,supply_chain = selected_supplychain)
            selected_shipment.receiver = receiver_name
            selected_shipment.time_shipment=datetime.datetime.now()
            selected_shipment.status='In Progress'
            selected_supplychain.save()
            selected_shipment.save()
            messages.info(request,"The request is succesfully sent! ",extra_tags='success')
    context={'shipments':shipments,'receivers':receivers,'loginUser':profile}
    return render(request, 'scm/manufacturer_transfer_shipment.html',context)

def requests_received(request):
    profile = Profile.objects.get(user=request.user)
    shipments = Shipment.objects.filter(receiver = profile.name,status='In Progress')
    allUsers = Profile.objects.all()
    carts_items_list =[]
    for shipment in shipments:
        cart_items= CartItems.objects.filter(cart=shipment.supply_chain.cart)
        print (cart_items)
        for item in cart_items:
            carts_items_list.append(item)
    
    context={'shipments':shipments,'carts_items_list':carts_items_list,'allUsers':allUsers,'loginUser':profile}
    if profile.role == 'Manufacturer':
        return render(request, 'scm/manufacturer_requests_received.html',context)
    elif profile.role == 'Hospital':
        return render(request, 'scm/hospital_requests_received.html',context)

def reject_request(request,id):
    selected_shipment = Shipment.objects.get(id = id)
    selected_supplychain = selected_shipment.supply_chain
    selected_shipment.status = 'Rejected'
    selected_supplychain.status_transferring = False
    selected_shipment.save()
    selected_supplychain.save()
    messages.info(request,"The request is successfully rejected!",extra_tags='success')
    return redirect ('requests_received')

def accept_request(request,id):
    profile = Profile.objects.get(user=request.user)
    selected_shipment = Shipment.objects.get(id = id)
    selected_supplychain = selected_shipment.supply_chain
    selected_shipment.status = 'Accepted'
    selected_supplychain.status_transferring = False
    selected_supplychain.ownership= profile
    Shipment.objects.create(sender = profile.name,supply_chain=selected_supplychain,previous_hash = selected_shipment.hash)
    selected_shipment.save()
    selected_supplychain.save()
    messages.info(request,"The request is successfully accepted!",extra_tags='success')
    return redirect ('requests_received')

def hospital_accept_request(request,id):
    profile = Profile.objects.get(user=request.user)
    selected_shipment = Shipment.objects.get(id = id)
    selected_supplychain = selected_shipment.supply_chain
    selected_shipment.status = 'Accepted'
    selected_supplychain.status_transferring = False
    selected_supplychain.ownership= profile
    selected_supplychain.issue = True
    selected_shipment.save()
    selected_supplychain.save()
    messages.info(request,"The request is successfully accepted!",extra_tags='success')
    return redirect ('requests_received')

def requests_sent(request):
    profile = Profile.objects.get(user=request.user)
    shipments = Shipment.objects.filter(sender = profile.name).exclude(status = 'N/A')
    carts_items_list =[]
    for shipment in shipments:
        cart_items= CartItems.objects.filter(cart=shipment.supply_chain.cart)
        print (cart_items)
        for item in cart_items:
            carts_items_list.append(item)
    context={'shipments':shipments,'carts_items_list':carts_items_list,'loginUser':profile}
    return render(request, 'scm/manufacturer_requests_sent.html',context)

def show_shipment(request):
    profile = Profile.objects.get(user=request.user)
    shipments = SupplyChain.objects.filter(ownership = profile)
    
    carts_items_list =[]
    ownerships_list =[]
    for shipment in shipments :
        cart_items= CartItems.objects.filter(cart=shipment.cart)
        for item in cart_items:
            carts_items_list.append(item)


    for shipment in shipments :
        ships = Shipment.objects.filter(supply_chain = shipment)
        for ship in ships:
            ownerships_list.append(ship)
        
    profiles = Profile.objects.all()
    context={'shipments':shipments,'carts_items_list':carts_items_list,
            'ownerships_list':ownerships_list,'profiles':profiles,'loginUser':profile}
    if profile.role == 'Manufacturer':
        return render(request, 'scm/manufacturer_shipment.html',context)
    elif profile.role == 'Hospital':
        return render(request, 'scm/hospital_shipment.html',context)
    
#Hospital Screens
def dashboard_hospital(request):
    profile = Profile.objects.get(user=request.user)
    shipments_onhand_count = SupplyChain.objects.filter(ownership = profile).count()
    requests_received_count = Shipment.objects.filter(receiver = profile.name,status='In Progress').count()
    shipments = SupplyChain.objects.filter(ownership = profile).order_by('-id')[:5]
    carts_items_list =[]
    for shipment in shipments :
        cart_items= CartItems.objects.filter(cart=shipment.cart)
        for item in cart_items:
            carts_items_list.append(item)
    context={'shipments_onhand_count':shipments_onhand_count,
            'requests_received_count':requests_received_count,'loginUser':profile,
            'shipments':shipments,'carts_items_list':carts_items_list,}
    return render(request, 'scm/hospital_dashboard.html',context)

#Public Access Screen
def public_page(request):
    hospitals = Profile.objects.filter(role='Hospital')
    
    if request.method == 'POST':
        try:
            selectedhospital = request.POST['hospital_name']
            selectedID = request.POST['badge_id']
        except:
            messages.info(request,"Please insert all details!",extra_tags='error')
            context={'hospitals':hospitals}
            return render(request, 'scm/public_page.html',context)

        if selectedID.isdigit():
            try:
                hosp = Profile.objects.get(name=selectedhospital)
                shipment = SupplyChain.objects.get(id = selectedID, ownership = hosp )
                cart_items= CartItems.objects.filter(cart=shipment.cart)

                carts_items_list =[]
                ownerships_list=[]
                for item in cart_items :
                    carts_items_list.append(item)

                ships = Shipment.objects.filter(supply_chain = shipment)
                for ship in ships:
                    ownerships_list.append(ship)
                
                profiles = Profile.objects.all()

                context={'hospitals':hospitals,'carts_items_list':carts_items_list,'shipment':shipment,
                    'ownerships_list':ownerships_list,'profiles':profiles}
            except:
                messages.info(request,"Badge Number not exist!",extra_tags='error')
                context={'hospitals':hospitals}
                return render(request, 'scm/public_page.html',context)
        else : 
            messages.info(request,"Invalid Input! Please insert integer for badge number !",extra_tags='error')
            context={'hospitals':hospitals}
            return render(request, 'scm/public_page.html',context)

        
    else :
        context={'hospitals':hospitals}

    return render(request, 'scm/public_page.html',context)


    
