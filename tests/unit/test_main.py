import pytest

from actions_test_python.main import main


class TestMain():
    @pytest.fixture(params = ["Hello world!\n"])
    def output_text(self, request):
        yield request.param

    def count_lines(self, text):
        return len(text.split('\n'))

    def test_main(self, capsys, output_text):
        main()
        captured = capsys.readouterr()

        assert self.count_lines(captured.out) == 2
        assert str(captured.out) == output_text