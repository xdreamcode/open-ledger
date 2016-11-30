from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from django_cas_ng.views import login as cas_login, logout as cas_logout, callback as cas_callback

from imageledger.views import search_views, api_views, list_views

urlpatterns = [
    url(r'^$', search_views.index, name='index'),
    url(r'^provider-apis$', search_views.provider_apis, name='provider-apis'),
    url(r'^provider/(?P<provider>\w+)$', search_views.by_provider, name='by-provider'),
    url(r'^image/detail$', search_views.by_image, name="by-image"),
    url(r'^image/detail/(?P<identifier>.*)$', search_views.detail, name="detail"),

    # CAS
    url(r'^accounts/login$', cas_login, name='cas_ng_login'),
    url(r'^accounts/logout$', cas_logout, name='cas_ng_logout'),
    url(r'^accounts/callback$', cas_callback, name='cas_ng_proxy_callback'),

    # Lists (public)
    url(r'list/(?P<slug>[^/]+)$', list_views.OLListDetail.as_view(), name='list-detail'),

    # Lists (user admin)
    url(r'list/add/$', list_views.OLListCreate.as_view(), name='my-list-add'),
    url(r'list/mine/(?P<slug>[^/]+)$', list_views.OLListUpdate.as_view(), name='my-list-update'),
    url(r'list/mine(?P<slug>[^/]+)/delete$', list_views.OLListDelete.as_view(), name='my-list-delete'),
    url(r'lists/mine', list_views.OLOwnedListList.as_view(), name="my-lists"),

]

apipatterns = [
    # List API
    url(r'^api/v1/lists$', api_views.ListList.as_view()),
    url(r'^api/v1/autocomplete/lists$', api_views.ListAutocomplete.as_view()),
    url(r'^api/v1/lists/(?P<slug>[^/]+)$', api_views.ListDetail.as_view()),

    # Favorite API
    url(r'^api/v1/images/favorite/(?P<identifier>[^/]+)$', api_views.FavoriteDetail.as_view()),
]

apipatterns = format_suffix_patterns(apipatterns)

urlpatterns += apipatterns
