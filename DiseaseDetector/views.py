from django.shortcuts import render

def main(request):
    return render(request, 'DiseaseDetector/index.html', )
