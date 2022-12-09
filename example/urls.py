from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('blog/', views.blogs),
    path('blog/list/', views.blog_list),
    path('blog/detail/<int:pk>', views.blog_detail),
    path('blog-api/list/', views.BlogList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)