import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# 1. 모델과 프로세서 로드
print("모델을 불러오는 중입니다...")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
print("모델 로드 완료!")