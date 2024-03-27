from abc import abstractmethod
from test_data.yaml_data import YamlData
from common.const import TestResult
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchFrameException,
    NoSuchElementException
)
from common.in_test_exeption import UICheckException


class BaseTest:
    test_result: TestResult

    def run_case(self, yaml_data: YamlData):
        try:
            self.test_result = TestResult.PASS
            self.test_act(yaml_data)
        except ElementClickInterceptedException as e:
            self.test_result = TestResult.FAIL
            print(e.msg)
        except NoSuchFrameException as e:
            self.test_result = TestResult.FAIL
            print(e.msg)
        except UICheckException:
            self.test_result = TestResult.FAIL
        except NoSuchElementException as e:
            self.test_result = TestResult.FAIL
            print(e.msg)
        except Exception as e:
            print(e)
            self.test_result = TestResult.ERROR
        finally:
            print(f'----   Test Result: {self.test_result.value}')

    @abstractmethod
    def test_act(self, yaml_data: YamlData):
        pass
