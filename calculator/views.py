

from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import determine_maximum_load

def calculate_load(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            material = request.POST.get('material', '').lower()
            width = request.POST.get('width', '')
            length = request.POST.get('length', '')
            height = request.POST.get('height', '')

            # Check if any of the fields are empty
            if not material or not width or not length or not height:
                messages.error(request, 'Please fill out all fields.')
                return redirect('calculator:calculate_load')

            try:
                width = float(width)
                length = float(length)
                height = float(height)
            except ValueError:
                messages.error(request, 'Invalid input. Please enter numeric values for width, length, and height.')
                return redirect('calculator:calculate_load')

            maximum_capacity = determine_maximum_load(material, width, length, height)

            if isinstance(maximum_capacity, (int, float)):
                result = f"The maximum load the {material} material can handle is {maximum_capacity}N."
            else:
                result = maximum_capacity

            context = {'result': result,'material': material,'width': width,'length': length, 'height': height}
            return render(request, 'calculate_load.html', context)
        else:
            messages.error(request, "You Must Be Logged In...")
            return redirect('core:login')

    return render(request, 'calculate_load.html')
