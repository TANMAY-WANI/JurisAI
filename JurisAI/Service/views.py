from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from Service.forms import DocumentForm
import PyPDF2
# Create your views here.

from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API"))
model = genai.GenerativeModel('gemini-pro')

def get_summary_from_llm(text_input):
    res= model.generate_content(text_input+"\n Summarize the given text in not more than 500 words. give only the summary and not anything else, like the introduction line or concluding line.")
    return res

def chat(request):
    return render(request,'chat.html')

def get_summary(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            document = request.FILES['document']
            # Extract text from the PDF
            pdf_reader = PyPDF2.PdfReader(document)
            text = ''
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

            response = get_summary_from_llm(text)


        
    return JsonResponse({'summary':response.text})
