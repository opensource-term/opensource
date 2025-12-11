import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# 1. 모델과 프로세서 로드
print("모델을 불러오는 중입니다...")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
print("모델 로드 완료!")

# 2. 이미지 캡션 생성 함수 정의
def generate_caption(image):
    try:
        # 이미지가 없으면 리턴
        if image is None:
            return "이미지를 업로드해주세요."
        
        # 모델 입력 전처리
        inputs = processor(images=image, return_tensors="pt")

        # 캡션 생성 (max_new_tokens로 문장 길이 조절 가능)
        out = model.generate(**inputs, max_new_tokens=50)

        # 토큰을 텍스트로 디코딩
        caption = processor.decode(out[0], skip_special_tokens=True)
        
        return caption
    except Exception as e:
        return f"에러 발생: {str(e)}"