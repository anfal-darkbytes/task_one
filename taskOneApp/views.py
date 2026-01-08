from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .utils import convert_file
import os


def home(request):
    output_url = None
    error = None


    if request.method == 'POST' and 'file' in request.FILES:
        uploaded_file = request.FILES['file']
        from_ext = request.POST.get('from_ext', '').strip('.')
        to_ext = request.POST.get('to_ext', '').strip('.')

        file_sys = FileSystemStorage()
        filename = file_sys.save(uploaded_file.name, uploaded_file)
        
        input_path = file_sys.path(filename)
        
        base_name = os.path.splitext(filename)[0]
        output_file_name = f"{base_name}.{to_ext}"

        output_path = file_sys.path(output_file_name)

        print(f"Input path: {input_path}")
        print(f"Output path: {output_path}")

        try:
            output_dir = os.path.dirname(output_path)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir) 
                print(f"Created directory: {output_dir}")

            convert_file(input_path, from_ext, to_ext, output_path)
            
            output_url = file_sys.url(output_file_name)
            
        except Exception as e:
            error = str(e)
            if os.path.exists(input_path):
                 os.remove(input_path)

    return render(request, 'index.html', {
        'output': output_url,
        'error': error
    })
