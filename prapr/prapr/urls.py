from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blog import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('signup/',views.user_signup, name="signup"),
    path('login/',views.user_login, name="login"),
    path('logout/',views.user_logout, name="logout"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('addblog/',views.add_blog, name="addblog"),
    path('updateblog/<int:id>/',views.update_blog, name="updateblog"),
    path('delete/<int:id>/',views.delete_blog, name="deleteblog"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),

]+ static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
