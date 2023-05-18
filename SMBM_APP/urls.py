from django.urls import path
from.import views,views01,views02,API


urlpatterns = [
   path('',views.home,name='home'),
   path('cusRegisteration/',views.customer_resgister,name='cust_regs'),
   path('staffRegisteration/',views.staff_resgister,name='staff_regs'),
   path('login/',views.login_page,name='login'),
   path('home2/',views.after_login,name='home2'),
   path('profile/',views.profile,name='profile'),
   path('home3/',views.staff_home,name='home3'),
   path('manageCusAcc/',views.manage_cus_account,name='manageCusAcc'),
   path('createCusAcc/',views.create_cus_acc,name='createCusAcc'),
   path('staff_manage_acc/',views.staff_manage_acc,name='staff_manage_acc'),
   path('staff_create_acc/',views.staff_create_acc,name='staff_create_acc'),
   path('searchAcc/',views.search_acc,name='searchAccount'),
   path('logout/',views.logout_page,name='logout'),

   path('booking/',views01.book_now,name='booking'),
   path('makebooking/',views01.make_booking,name='makebooking'),
   path('bookingdetail/',views01.booking_detail,name='detail'),
   path('bookingticket/',views01.booking_ticket,name='ticket'),
   path('cusgbooking/',views01.customer_booking,name='cusgbooking'),
   path('cusgbooking2',views01.customer_booking2,name='cusgbooking2'),
   path('managebooking/',views01.managebooking,name='managebooking'),
   path('views_slot',views01.view_slot,name='view_slot'),
   path('create_slot',views01.create_slot,name='create_slot'),
   path('clear_allslot',views01.clear_allslot,name='clear'),
   path('delete_slot/<int:id>',views01.delete_slot,name='delete_slot'),
   path('update_slot/<int:id>',views01.update_slot,name='update_slot'),
   path('avalible_slot/<int:id>',views01.avalible,name='avalible_slot'),
    path('unavalible_slot/<int:id>',views01.unavalible,name='unavalible_slot'),
   

   path('redeemrewards/',views02.redeem_rewards,name='myrewards'),
   path('redeemHistory/',views02.redeem_history,name='myhistory'),
   path('chat/',views02.chat,name='chat'),
   path('feedback',views02.feedback,name='feedback'),
   path('retrieveFeedback/',views02.retri_feedback,name='retri_feedback'),
   path('deletefeedback/<int:id>',views02.feedback_delete,name='deletefeedback'),
   path('chatInfo/',views02.chat_info,name='chat_info'),
   path('chatDelete/<int:id>',views02.chat_delete,name='chat_delete'),

   path('api/', API.SlotList.as_view()),
   path('api2/<str:q>/', API.ChatList.as_view()),
   path('api3/', API.MessageList.as_view()),
   path('api4/<int:q>/', API.SingleuserList.as_view()),

]
