from django.forms import ValidationError

class MaxSizeFileValidator:

    def __init__(self, max_file_size=5):
        self.max_file_size = max_file_size

    def __call__(self, value):
        size = value.size
        numero = 1048576
        max_size = self.max_file_size * numero

        if size > max_size:
            raise ValidationError(f"El tamaño máximo del archivo es {self.max_file_size}MB")
        
        return value