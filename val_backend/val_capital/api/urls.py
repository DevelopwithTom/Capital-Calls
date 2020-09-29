from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'funds', views.FundViewSet, basename='funds')  
router.register(r'commitments', views.CommitmentViewSet, basename='commitments')  
router.register(r'calls', views.CallViewSet, basename='calls')  
router.register(r'drawdowns', views.DrawdownViewSet, basename='drawdowns')  

urlpatterns = router.urls