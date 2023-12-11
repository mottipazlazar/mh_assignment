from abc import ABC
from infra.drivers.report.report_manager import ReportManager


class Component(ABC):

    def __init__(self) -> None:
        """

        :rtype: object
        """
        self.report = ReportManager()
