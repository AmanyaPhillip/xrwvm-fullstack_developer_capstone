from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for about view
    # E265: block comment should start with '# '
    # W291: trailing whitespace
    path(route='about', view=views.about, name='about'), # E231: missing whitespace after ','

    # # path for contact us view
    # E265: block comment should start with '# '
    path(route='contact', view=views.contact, name='contact'),

    # path for login
    path(route='login', view=views.login_user, name='login'), # E501: Line too long.
                                                               # E251: unexpected spaces around keyword / parameter equals (in path)

    # path for logout
    path(route='logout', view=views.logout_request, name='logout'), # E501: Line too long.

    # path for registration
    path(route='register', view=views.registration_request, name='register'), # E501: Line too long.

    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view
    path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_details'), # E501: Line too long.

    # path for add a review view
    path(route='add_review', view=views.add_review, name='add_review'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
