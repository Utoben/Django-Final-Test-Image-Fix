from django.urls import path
from . import views
from .views import RegisterUser, LoginUser
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path ('', views.home_view, name='home'),
    path('about', views.to_about, name='about'),
    path('delete_task/<int:task_id>/', views.delete_task_view, name='delete_task'),
    path('create_post/', views.post_create, name='create_post'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('category/<int:cat_id>/', views.category_posts, name='category_posts'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)