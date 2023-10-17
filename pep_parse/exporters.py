from scrapy.exporters import CsvItemExporter


class CustomCsvItemExporter(CsvItemExporter):
    def __init__(
        self, file, include_headers_line=False, join_multivalued=",", **kwargs
    ):
        super().__init__(
            file,
            include_headers_line=include_headers_line,
            join_multivalued=join_multivalued,
            **kwargs
        )

    def start_exporting(self):
        self.csv_writer.writerow(["Номер", "Название", "Статус"])
