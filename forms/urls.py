from rest_framework.routers import DefaultRouter
from forms.views import CategoryView, FormView, PassedView, UserView, AnswerView


router = DefaultRouter()

router.register('category', CategoryView, basename='category')
router.register('form', FormView, basename='form')
router.register('passed-form', PassedView, basename='passed-form')
router.register('user', UserView, basename='user')
router.register('answer', AnswerView, basename='answer')