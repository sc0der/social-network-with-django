from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf	import	settings
from django.conf.urls.static	import	static
from django.urls import path
from subject.views import by_subject
from questions.views import (
    search, edit_savol,
    add_savol, post_delete, 
    PostDetail, PostList, like_post
    )
from account.views import user_login, register, dashboard, edit, user_detail, user_list
from	django.contrib.auth	import	views	as	auth_views

urlpatterns = [
    path('', PostList, name="index"),
    path('register',	register,	name='register'),
    path('edit/',	edit,	name='edit_profile'),
    path('dashboard',	dashboard,	name='dashboard'),
	path('logout/',	auth_views.LogoutView.as_view(),	name='logout'),
    path('login/',	user_login,	name='login'),
    path('users/',	user_list,	name='user_list'),
	path('users/<username>/', user_detail,	name='user_detail'),
    path('search/', search, name="search"),
    path('add_savol/', add_savol, name="add_savol"),
    path('like_post/', like_post, name="like_post"),
    path('<int:pk>/', by_subject, name='by_subject'),
    path('edit_savol/<int:pk>/', edit_savol, name="edit_savol"),
    path('post_delete/<int:pk>/', post_delete, name="post_delete"),
    path('post_detail/<post>/', PostDetail, name="savolho_detail"),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'), 
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin/', admin.site.urls),
]
urlpatterns	+=	static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)