# calculator/utils.py
def determine_maximum_load(material, width, length, height):
    properties_of_material = {
        'steel': {'yield_stress': 250, 'safety_factor': 2},
        'wood': {'yield_stress': 40, 'safety_factor': 3},
        # Add more materials and their properties as needed.
    }

    if material not in properties_of_material:
        return "Unsupported Material"

    if length <= 0 or width <= 0 or height <= 0:
        return "Dimensions not identified"

    max_load = (properties_of_material[material]['yield_stress'] * width * height) / \
               properties_of_material[material]['safety_factor']
    return max_load
