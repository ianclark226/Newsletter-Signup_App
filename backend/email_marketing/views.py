from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests

activecampaign_url = settings.ACTIVE_CAMPAIGN_URL
activecampaign_key = settings.ACTIVE_CAMPAIGN_KEY

class EBookSignupView(APIView):
    def post(self, request, format=None):
        try:
            data = self.request.data
            first_name = data['first_name']
            email = data['email']
            agree = data['agree']

            try:
                agree = bool(agree)
            except:
                return Response(
                    {'error': 'Must agree to privacy policy and terms of survice'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if not agree:
                return Response(
                    {'error': "Must agree to privacy policy and terms of survice"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            # CREATE/UPDATING CONTACT
            url = activecampaign_url + '/api/3/contacts/sync'

            data = {
                "contact": {
                    "email": email,
                    "firstName": first_name,
                }
            }
            headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Api-Token': activecampaign_key
            }

            response = request.post(url, json=data, headers=headers)

            if response.status_code != 201 and response.status_code !=200:
                return Response(
                    {'error': 'Something went wrong when creating contact'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            contact = response.json()

            try:
                contact_id = contact['contact']['id']
            except:
                return Response(
                    {'error': "Something went wrong when creating contact_id"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            # ADDING OF THE TAG TO CONTACT
            url = activecampaign_url + '/api/3/contactTags'
            data = {
                "contactTag": {
                    "contact": contact_id,
                    "tag": "1"
        }
            }

            response = request.post(url, json=data, headers=headers)

            if response.status_code != 201 and response.status_code != 200:
                return Response(
                    {'error': "Something went wrong when creating contact"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            # ADD CONTACT TO OUR MAIN LIST AND EBOOK LIST
            url = activecampaign_url + '/api/3/contactLists'
            data = {
                "contactList": {
                    "list": '1',
                    "contact": contact_id,
                    "status": '1'
        }
            }

            response = request.post(url, json=data, headers=headers)

            if response.status_code != 201 and response.status_code != 200:
                return Response(
                    {'error': "Something went wrong when adding contact to main list"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            data = {
                "contactList": {
                    "list": '2',
                    "contact": contact_id,
                    "status": '1'
        }
            }

            response = request.post(url, json=data, headers=headers)

            if response.status_code != 201 and response.status_code != 200:
                return Response(
                    {'error': "Something went wrong when adding contact to eBook list"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            else:
                return Response(
                    {'success': "Must agree to privacy policy and terms of survice"},
                    status=status.HTTP_400_BAD_REQUEST
            )
        except:
            return Response(
                {'error': 'Something whent wrong on our end'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


        

        
