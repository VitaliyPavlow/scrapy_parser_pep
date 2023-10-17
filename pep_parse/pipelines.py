import csv
from datetime import datetime
from pathlib import Path

from scrapy import Item

from pep_parse.spiders.pep import stat_count


BASE_DIR: Path = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider) -> None:
        pass

    def process_item(self, item, spider) -> Item:
        return item

    def close_spider(self, spider) -> None:
        result = [
            ("Статус", "Количество"),
        ]
        result.extend(stat_count.items())
        result.append(("Total", (sum(stat_count.values()))))
        results_dir = BASE_DIR / "results"
        results_dir.mkdir(exist_ok=True)
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"status_summary_{formatted_time}.csv"
        file_path = results_dir / file_name
        with open(file_path, "w", encoding="utf-8") as f:
            writer = csv.writer(f, dialect="unix")
            writer.writerows(result)
