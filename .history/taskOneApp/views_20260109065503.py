from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .utils import convert_file
import os


def home(request):
    output_url = None
    error = None

    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        from_ext = request.POST.get('from_ext', '').replace('.', '').lower()
        to_ext = request.POST.get('to_ext', '').replace('.', '').lower()

        fs = FileSystemStorage()

        # Save input file
        input_filename = fs.save(uploaded_file.name, uploaded_file)
        input_path = fs.path(input_filename)

        base_name = os.path.splitext(input_filename)[0]
        output_filename = f"{base_name}.{to_ext}"
        output_path = fs.path(output_filename)

        print(f"Input path: {input_path}")
        print(f"Output path: {output_path}")

        try:
            convert_file(input_path, from_ext, to_ext, output_path)

            output_url = fs.url(output_filename)

            # ✅ delete input file after success
            if os.path.exists(input_path):
                os.remove(input_path)

        except Exception as e:
            error = str(e)

            if os.path.exists(input_path):
                os.remove(input_path)

    return render(request, 'index.html', {
        'output': output_url,
        'error': error
    })
