def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except (ValueError, IndexError, KeyError) as error:
            base_value_error = "not enough values to unpack"
            if base_value_error in str(error):
                return "Please provide both name and phone number."
            
            if error.__class__ == IndexError:
                return 'Please, enter required arguments for the command'
            
            if error.__class__ == KeyError:
                return 'Contact not found.'
            
            return str(error)

    return inner