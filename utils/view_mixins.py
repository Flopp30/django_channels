import json


class OpenModalMixin:
    modal_name: str

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response['HX-Trigger'] = json.dumps({"openModal": self.modal_name})
        return response
