class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# NOTE: was copied from a project of mine

class ConsoleReporter(object):

    def start_test(self, test_name):
        print(f"{BColors.HEADER}## Test Start: {test_name} ##{BColors.ENDC}", flush=True)

    def end_test(self, test_name):
        print(f"{BColors.HEADER}## Test End: {test_name} ##{BColors.ENDC}", flush=True)

    def info(self, message):
        print(f"{BColors.OKGREEN}[INFO]   {message}{BColors.ENDC}", flush=True)

    def warning(self, message):
        print(f"{BColors.WARNING}[INFO]   {message}{BColors.ENDC}", flush=True)

    def debug(self, message):
        print(f"{BColors.OKBLUE}[DEBUG]  {message}{BColors.ENDC}", flush=True)

    def error(self, message):
        print(f"{BColors.FAIL}[ERROR]  {message}{BColors.ENDC}", flush=True)

    def image(self, image_name, description=None):
        print(f"{BColors.OKGREEN}[INFO] File: '{image_name}' with description '{description}'{BColors.ENDC}", flush=True)

    def file(self, file_name, description=None):
        print(f"{BColors.OKGREEN}[INFO] File: '{file_name}' with description '{description}'{BColors.ENDC}", flush=True)
