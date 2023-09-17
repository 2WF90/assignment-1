#----------------------------------------------------------------
# DEFINITION DECORATOR callonce
#----------------------------------------------------------------

# Source: https://stackoverflow.com/questions/25929564/how-to-make-a-few-lines-of-function-execute-only-once-in-python-preferably-usin
# Function decorator, makes sure a function is only called once

class callonce(object):
    def __init__(self, f):
        self.f = f
        self.called = False

    def __call__(self, *args, **kwargs):
        if not self.called:
            self.called = True
            return self.f(*args, **kwargs)