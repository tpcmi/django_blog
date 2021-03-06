from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.post_list,name="post_list"), # ^（表示开头）并紧随 $（表示结尾），所以只有空字符串会被匹配到
    re_path(r'^post/(?P<pk>[0-9]+)/$',views.post_detail,name="post_detail"),
    path('post/new/',views.post_new,name="post_new"),
    re_path(r'post/(?P<pk>[0-9]+)/edit/$',views.post_edit,name="post_edit")
]