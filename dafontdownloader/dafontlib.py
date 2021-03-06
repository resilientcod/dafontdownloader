import os
import re
import shutil
import tempfile
import zipfile
import requests
import platform


class CompactFont:
    def __init__(self, bin_content):
        self.bin_content = bin_content
        self._tmp_dir = tempfile.mkdtemp()
        self._tmp_compact_file = os.sep.join([self._tmp_dir, 'font_file.zip'])
        self._tmp_dir_fonts = os.sep.join([self._tmp_dir, 'dirfont'])

    def _download_compact_file(self):
        with open(self._tmp_compact_file, "wb") as f:
            f.write(self.bin_content)

    def _extract_compact_file(self):
        try:
            compact_file = zipfile.ZipFile(self._tmp_compact_file)
            compact_file.extractall(self._tmp_dir_fonts)
            compact_file.close()
        except zipfile.BadZipFile:
            print('Incompatible archive.')

    def install_font_file(self):
        current_system = platform.system()

        self._download_compact_file()
        self._extract_compact_file()

        REGEX_TYPE_FONT = r"^.*?\.(otf|ttf|OTF|TTF)$"

        if current_system == 'Linux':
            DEFAULT_FONT_DIR = os.path.expanduser('~/.fonts')

            if not os.path.exists(DEFAULT_FONT_DIR):
                os.makedirs(DEFAULT_FONT_DIR)

            for file in os.listdir(self._tmp_dir_fonts):
                if re.search(REGEX_TYPE_FONT, file):
                    shutil.copy2(os.path.join(
                        self._tmp_dir_fonts, file), DEFAULT_FONT_DIR)
        elif current_system == 'Windows':
            for file in os.listdir(self._tmp_dir_fonts):
                if re.search(REGEX_TYPE_FONT, file):
                    os.system(os.sep.join([self._tmp_dir_fonts, f'"{file}"']))
        else:
            print('Unsuported system')

        shutil.rmtree(self._tmp_dir)


class Dafont:
    def __init__(self):
        self.BASE_URL = 'https://dl.dafont.com/dl/?f='

    def search_font(self, name):
        parsed_name = name.replace(' ', '_').lower()
        request = requests.get(self.BASE_URL + parsed_name)

        if not request.content:
            raise ValueError

        return CompactFont(request.content)
