from django.core.exceptions import ValidationError

def validate_image_size(image):
    # 5 MB in bytes
    max_size = 5 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError("Image size exceeds the maximum limit (5 MB).")


