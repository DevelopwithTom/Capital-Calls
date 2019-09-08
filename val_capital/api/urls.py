from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'funds', views.FundViewSet, basename='funds')  
router.register(r'deposits', views.DepositViewSet, basename='deposits')  
router.register(r'calls', views.CallViewSet, basename='calls')  
router.register(r'commitments', views.CommitmentViewSet, basename='commitments')  

urlpatterns = router.urls