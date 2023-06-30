from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from .models import CustomUser


def admin_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="accounts:login"
):
    """
    Decorator for views that checks that the logged in user is an admin,
    redirects to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.role == CustomUser.Role.ADMIN,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def editor_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="accounts:login"
):
    """
    Decorator for views that checks that the logged in user is a editor,
    redirects to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.role == CustomUser.Role.Editor,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
