import os
from utilities.read_properties import ReadConfig

class VerifyDownload:
    downloads_filepath = ReadConfig.get_downloads_filepath()

    def verify_invoice_download(self):
        return True if 'invoice.txt' in os.listdir(self.downloads_filepath) else False