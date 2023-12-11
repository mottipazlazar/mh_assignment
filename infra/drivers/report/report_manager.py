from infra.drivers.report.console_reporter import ConsoleReporter
from infra.drivers.report.report_portal_reporter import ReportPortalReporter

# NOTE: was copied from a project of mine


def invoke_if_exists(reporter, method_name, message):
    if hasattr(reporter, method_name):
        method = getattr(reporter, method_name, None)
        if callable(method):
            method(message)


class ReportManager(object):
    class __ReportManager:
        def __init__(self):
            self.reporters = [ConsoleReporter(), ReportPortalReporter()]

        def add_reporter(self, reporter):
            self.reporters.append(reporter)

        def info(self, message):
            for reporter in self.reporters:
                invoke_if_exists(reporter, "info", message)

        def debug(self, message):
            for reporter in self.reporters:
                invoke_if_exists(reporter, "debug", message)

        def warning(self, message):
            for reporter in self.reporters:
                invoke_if_exists(reporter, "warning", message)

        def error(self, message):
            for reporter in self.reporters:
                invoke_if_exists(reporter, "error", message)

        def image(self, image_name, description=None):
            for reporter in self.reporters:
                if hasattr(reporter, "image"):
                    method = getattr(reporter, "image", None)
                    if callable(method):
                        method(image_name, description)

        def file(self, file_name, description=None):
            for reporter in self.reporters:
                if hasattr(reporter, "file"):
                    method = getattr(reporter, "file", None)
                    if callable(method):
                        method(file_name, description)

        def start_test(self, test_name):
            for reporter in self.reporters:
                invoke_if_exists(reporter, "start_test", test_name)

        def end_test(self, test_name):
            for reporter in self.reporters:
                invoke_if_exists(reporter, "end_test", test_name)

    instance = None

    def __new__(cls):  # __new__ always a classmethod
        if not ReportManager.instance:
            ReportManager.instance = ReportManager.__ReportManager()
        return ReportManager.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)


