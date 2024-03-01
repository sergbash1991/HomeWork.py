class ValidatorType:
    VALID_TYPES = [int, float]

    def _is_valid(self, data):
        if type(data) not in Validator.VALID_TYPES:
            raise ValueError('Data does not have an appropriate type')
        return True

    def __call__(self, data, *args, **kwargs):
        return self._is_valid(data)


    class IntegerValidator(Validator):
        def __init__(self, min_value, max_value):
            self.min_value = min_value
            self.max_value = max_value

        def _is_valid(self, data):
            if super()._is_valid(data):
                if self.min_value <= data <= self.max_value:
                    return True
                else:
                    raise ValueError('Unsupported range')

    class FloatValidator(Validator):
        def __init__(self, min_value, max_value):
            self.min_value = min_value
            self.max_value = max_value

        def _is_valid(self, data):
            if super()._is_valid(data):
                if self.min_value <= data <= self.max_value:
                    return True
                else:
                    raise ValueError('Unsupported range')

integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)