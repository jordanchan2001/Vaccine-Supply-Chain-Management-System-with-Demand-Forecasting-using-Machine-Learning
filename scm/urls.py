from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.login, name="login"),
	path('register',views.register,name="register"),
	path('dashboard',views.dashboard,name="dashboard"),
	path('users',views.users,name="users"),
	path('vaccines',views.vaccines,name="vaccines"),
	path('shipments',views.shipments,name="shipments"),
	path('analysts',views.analysts,name="analysts"),
	path('logout',views.logout,name="logout"),
	path('edit_user/<int:id>', views.edit,name="edit_user"),
	path('update_user/<int:id>', views.update,name="update_user"),
	path('delete_user/<int:id>', views.delete,name="delete_user"),
	path('activate_user/<int:id>', views.activate,name="activate_user"),
	path('show_vaccine_form',views.show_vaccine_form,name="show_vaccine_form"),
	path('add_vaccine',views.add_vaccine,name="add_vaccine"),
	path('edit_vaccine/<str:name>',views.edit_vaccine,name="edit_vaccine"),
	path('update_vaccine/<str:name>', views.update_vaccine,name="update_vaccine"),
	path('delete_vaccine/<str:name>', views.delete_vaccine,name="delete_vaccine"),

	#Manufacturer Urls
	path('dashboard_manufacturer',views.dashboard_manufacturer,name="dashboard_manufacturer"),
	path('show_profile_setting',views.show_profile_setting,name="show_profile_setting"),
	path('update_profile',views.update_profile,name="update_profile"),
	path('delete_cart_item/<str:id>',views.delete_cart_item,name="delete_cart_item"),
	path('create_shipment',views.create_shipment,name="create_shipment"),
	path('transfer_shipment',views.transfer_shipment,name="transfer_shipment"),
	path('requests_received',views.requests_received,name="requests_received"),
	path('reject_request/<str:id>',views.reject_request,name="reject_request"),
	path('accept_request/<str:id>',views.accept_request,name="accept_request"),
	path('requests_sent',views.requests_sent,name="requests_sent"),
	path('show_shipment',views.show_shipment,name="show_shipment"),

	#Hospital Urls
	path('dashboard_hospital',views.dashboard_hospital,name="dashboard_hospital"),
	path('hospital_accept_request/<str:id>',views.hospital_accept_request,name="hospital_accept_request"),

	#Public Urls
	path('public_page',views.public_page,name="public_page"),


]