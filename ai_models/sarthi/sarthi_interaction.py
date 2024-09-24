# sarthi_interaction.py

from ai_models.yug.model import YugModel
from ai_models.aadi.model import AadiModel
from ai_models.arth.model import ArthModel
from ai_models.ved.model import VedModel

class SarthiAI:
    def __init__(self):
        self.yug = YugModel()
        self.aadi = AadiModel()
        self.arth = ArthModel()
        self.ved = VedModel()

    def process_request(self, request):
        """Process user request and interact with other AIs"""
        task_type = request.get('task_type')
        
        if task_type == 'generate_3d':
            return self.yug.generate_3d(request['input_data'])
        elif task_type == 'generate_music':
            return self.aadi.generate_music(request['input_data'])
        elif task_type == 'generate_video':
            return self.arth.generate_video(request['input_data'])
        elif task_type == 'emotion_recognition':
            return self.ved.recognize_emotion(request['image_data'])
        else:
            return {"error": "Unknown task type"}

    def interact(self, user_input):
        """Main user interaction logic for Sarthi AI"""
        print(f"Sarthi AI received request: {user_input}")
        response = self.process_request(user_input)
        print(f"Sarthi AI processed response: {response}")
        return response
