from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from Service.forms import DocumentForm
import PyPDF2
# Create your views here.

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
        
        
    return JsonResponse({'summary':"Hello world, this is tanmay wani. You are currenly viewing my summary as a response"})
