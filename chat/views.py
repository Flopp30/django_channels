from django.views.generic import TemplateView


class ChatSelectionView(TemplateView):
    template_name = '.chat/chat_selection.html'


class RoomView(TemplateView):
    template_name = '.chat/room.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data() | {"room_name": self.kwargs.get("room_name")}
