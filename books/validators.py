from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize= value.size
    
    if filesize > 50000:
        raise ValidationError("The maximum file size that can be uploaded is 50MB")
    else:
        return value
