# from django.shortcuts import render
#
# # Create your views here.
# from django.contrib.auth import get_user_model
# from django.views.generic import TemplateView
# from rest_auth.views import LoginView
# from rest_framework import status, viewsets
# from rest_framework.permissions import BasePermission
# from rest_framework.response import Response
# from rest_framework.viewsets import ModelViewSet
# from django.conf import settings
#
#
# from .serializers import (
#     IMAccountConfirmSerializer,
#     IMResetPasswordSerializer,
#     send_verification_registration_email,
#     set_ver_code_and_send_forgot_password_email,
# )
#
# User = get_user_model()
#
#
# class RestAuthViewSet(viewsets.ModelViewSet):
#     permission_classes = []
#     queryset = User.objects.filter()
#     http_method_names = ["post"]
#
#
# class AfterRegisterPermission(BasePermission):
#     def has_permission(self, request, view):
#         if request.GET.get("isReset") == "1":
#             email = request.get_full_path().split("/")[-2]
#             user = User.objects.filter(email__iexact=email.strip().lower())
#             return user[0].is_email_verified
#         return True
#
#
# class IMAccountConfirmViewSet(RestAuthViewSet):
#     queryset = User.objects.all()
#     permission_classes = [AfterRegisterPermission]
#
#     def get_queryset(self):
#         user = User.objects.filter(email__iexact=self.kwargs["email"].strip().lower())
#         user = user[0]
#
#         if self.request.GET.get("isReset") == "1":
#             if not user or not user.is_email_verified:
#                 return Response(
#                     {"message": "User with specified email address does not exists"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )
#             else:
#                 set_ver_code_and_send_forgot_password_email(user)
#         else:
#             send_verification_registration_email(user)
#         return []
#
#     http_method_names = ["post", "get"]
#     serializer_class = IMAccountConfirmSerializer
#
#
# class IMResetPasswordViewSet(RestAuthViewSet):
#     serializer_class = IMResetPasswordSerializer
#
#
# class LoginView(LoginView):
#     authentication_classes = []
#
#     def get_response(self):
#         serializer_class = self.get_response_serializer()
#         serializer = serializer_class(
#             instance=self.token, context={"request": self.request}
#         )
#         serialier_data = serializer.data
#
#         serialier_data["user_id"] = self.user.pk
#         serialier_data["first_name"] = self.user.first_name
#         serialier_data["last_name"] = self.user.last_name
#         serialier_data["email"] = self.user.email
#         serialier_data["phone_number"] = self.user.phone_number
#         serialier_data["verification_code"] = self.user.verification_code
#         serialier_data["forgot_pin_code"] = self.user.forgot_pin_code
#         serialier_data["image"] = self.user.photo.url if self.user.photo else None
#
#         return Response(
#             data={
#                 "message": "Succesfully logged in",
#                 "details": serialier_data,
#                 "success": True,
#             },
#             status=status.HTTP_200_OK,
#         )
#
# #
# # class ProfileSettingsViewSet(ModelViewSet):
# #     queryset = User.objects.all()
# #     serializer_class = IMUserSerializer
# #     # permission_classes = [IsAuthenticatedOrReadOnly]
# #     permission_classes = [AllowAny]
# #
# #     def send_verification_edit_email(self, user, email):
# #         EPC = settings.EDIT_CONFIGURATION
# #         if (
# #             "verification-email" in EPC
# #             and "set_pin" in EPC["verification-email"]
# #         ):
# #             pin_length = EPC["verification-email"]["set_pin"]["length"]
# #             if (
# #                 datetime.datetime.now()
# #                 - user.verification_code_time.replace(tzinfo=None)
# #             ).seconds > 300:
# #                 user.verification_code = "".join(
# #                     random.choice("123456789") for _ in range(pin_length)
# #                 )
# #         subject = EPC["verification-email"]["subject"]
# #         message = EPC["verification-email"]["message"].format(user=user)
# #         send_mail(
# #             subject,
# #             message,
# #             settings.EMAIL_HOST_USER_EMAIL,
# #             [email],
# #             fail_silently=True,
# #         )
# #         user.verification_code_time = datetime.datetime.now()
# #         user.save()
# #
# #     def send_verification_edit_sms(self, user, phone_number):
# #         EPC = settings.EDIT_CONFIGURATION
# #         if (
# #             "verification-email" in EPC
# #             and "set_pin" in EPC["verification-email"]
# #         ):
# #             pin_length = EPC["verification-email"]["set_pin"]["length"]
# #             if (
# #                 datetime.datetime.now()
# #                 - user.verification_code_time.replace(tzinfo=None)
# #             ).seconds > 300:
# #                 user.verification_code = "".join(
# #                     random.choice("123456789") for _ in range(pin_length)
# #                 )
# #         sns = boto3.client(
# #             "sns",
# #             aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
# #             aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
# #             region_name=os.environ.get("AWS_S3_REGION_NAME"),
# #         )
# #         sns.publish(
# #             PhoneNumber=phone_number,
# #             Message=f"Hello {user.first_name} {user.last_name}.\nPlease enter the verification code below into the EscaipPlan app to change phone number:\n{user.verification_code}\nThank you,\nThe EscaipPlan Team",
# #         )
# #         user.verification_code_time = datetime.datetime.now()
# #         user.save()
# #
# #     def verify_email_phone_number(
# #         self, user_obj, new_email, new_phone_number, verification_pin
# #     ):
# #         if not new_email and user_obj.email:
# #             user_obj.email = ""
# #         if not new_phone_number and user_obj.phone_number:
# #             user_obj.phone_number = ""
# #
# #         if new_email and verification_pin == user_obj.verification_code:
# #             if (
# #                 User.objects.filter(
# #                     email__iexact=new_email.strip().lower()
# #                 ).exists()
# #                 and user_obj.email.strip().lower() != new_email.strip().lower()
# #             ):
# #                 raise Exception(
# #                     "A user has already been registered with this email"
# #                 )
# #             if EmailAddress.objects.filter(user=user_obj).exists():
# #                 EmailAddress.objects.filter(user=user_obj).update(
# #                     email=new_email
# #                 )
# #             user_obj.email = new_email
# #             user_obj.username = new_email
# #             user_obj.is_email_verified = True
# #
# #         if new_phone_number and verification_pin == user_obj.verification_code:
# #             if (
# #                 User.objects.filter(phone_number=new_phone_number).exists()
# #                 and user_obj.phone_number != new_phone_number
# #             ):
# #                 raise Exception(
# #                     "A user has already been registered with this phone number"
# #                 )
# #             user_obj.phone_number = new_phone_number
# #             user_obj.is_mobile_verified = True
# #
# #         return user_obj
# #
# #     def list(self, request, *args, **kwargs):
# #         try:
# #             queryset = self.get_queryset()
# #             user_id = request.query_params.get("user_id", None)
# #             email = request.query_params.get("email", None)
# #             phone_number = request.query_params.get(
# #                 "phone_number", None
# #             ).strip()
# #             if phone_number:
# #                 phone_number = "+" + phone_number
# #
# #             if user_id:
# #                 user = queryset.filter(id=user_id).first()
# #             else:
# #                 raise Exception("Please provide valid user id")
# #
# #             if (
# #                 email
# #                 and user.email.strip().lower() != email.strip().lower()
# #                 and User.objects.filter(
# #                     email__iexact=email.strip().lower()
# #                 ).exists()
# #             ):
# #                 raise Exception(
# #                     "A user has already been registered with this email"
# #                 )
# #             if (
# #                 phone_number
# #                 and user.phone_number != phone_number
# #                 and User.objects.filter(phone_number=phone_number).exists()
# #             ):
# #                 raise Exception(
# #                     "A user has already been registered with this phone number"
# #                 )
# #
# #             if email:
# #                 self.send_verification_edit_email(user, email)
# #             if phone_number:
# #                 self.send_verification_edit_sms(user, phone_number)
# #
# #             return Response(
# #                 data={
# #                     "message": "Successfully sent otp to email or phone_number",
# #                     "success": True,
# #                 },
# #                 status=status.HTTP_200_OK,
# #             )
# #         except Exception as exp_main:
# #             return Response(
# #                 {"message": str(exp_main)}, status=status.HTTP_400_BAD_REQUEST
# #             )
# #
# #     def partial_update(self, request, *args, **kwargs):
# #         try:
# #             with transaction.atomic():
# #                 data = request.data
# #                 user_obj = self.get_object()
# #                 if user_obj:
# #                     image_details = data.get("image", {})
# #                     if image_details:
# #                         user_obj.upload_image(user_obj, image_details)
# #
# #                     user_obj.chat_messages = data.get("chat_messages", False)
# #                     user_obj.people_added = data.get("people_added", False)
# #                     user_obj.new_events = data.get("new_events", False)
# #                     user_obj.trip_cancel = data.get("trip_cancel", False)
# #                     user_obj.trip_remainder = data.get("trip_remainder", False)
# #
# #                     new_first_name = data.get("first_name", None)
# #                     new_last_name = data.get("last_name", None)
# #                     new_phone_number = data.get("phone_number", None)
# #                     new_email = data.get("email", None)
# #                     verification_pin = data.get("pin", None)
# #
# #                     if new_first_name:
# #                         user_obj.first_name = new_first_name
# #                     if new_last_name:
# #                         user_obj.last_name = new_last_name
# #
# #                     if verification_pin:
# #                         if verification_pin != user_obj.verification_code:
# #                             raise Exception(
# #                                 "Invalid OTP code. Please check the code and try again"
# #                             )
# #                         user_obj = self.verify_email_phone_number(
# #                             user_obj,
# #                             new_email,
# #                             new_phone_number,
# #                             verification_pin,
# #                         )
# #
# #                     user_obj.save()
# #
# #                     serializer = self.get_serializer(user_obj).data
# #                     pn = serializer["phone_number"]
# #                     serializer["phone_number"] = (
# #                         pn[:-10] + " " + pn[-10:] if pn else None
# #                     )
# #                     serializer["image"] = (
# #                         user_obj.photo.url if user_obj.photo else None
# #                     )
# #
# #                 return Response(
# #                     data={
# #                         "message": "Successfully updated user profile",
# #                         "details": serializer,
# #                         "success": True,
# #                     },
# #                     status=status.HTTP_200_OK,
# #                 )
# #         except Exception as exp:
# #             return Response(
# #                 {"message": str(exp)}, status=status.HTTP_400_BAD_REQUEST
# #             )
# #
#
#
# class StaticView(TemplateView):
#     def get(self, request, page, *args, **kwargs):
#         self.template_name = f"pages/{page}.html"
#         response = super(StaticView, self).get(request, *args, **kwargs)
#         return response.render()
