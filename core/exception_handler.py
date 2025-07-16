from rest_framework.views import exception_handler
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    if isinstance(exc, IntegrityError):
        return Response(
            {"email": ["A user with this email already exists."]},
            status=status.HTTP_400_BAD_REQUEST
        )

    return exception_handler(exc, context)