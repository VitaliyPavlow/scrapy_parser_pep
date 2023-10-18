import csv
from datetime import datetime
from pathlib import Path

from scrapy import Item


BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider) -> None:
        self.stat_count = {}
        pass

    def process_item(self, item, spider) -> Item:
        self.stat_count[item["status"]] = (
            self.stat_count.get(item["status"], 0) + 1
        )
        return item

    def close_spider(self, spider) -> None:
        result = [
            ("Статус", "Количество"),
        ]
        result.extend(self.stat_count.items())
        result.append(("Total", (sum(self.stat_count.values()))))
        results_dir = BASE_DIR / "results"
        results_dir.mkdir(exist_ok=True)
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"status_summary_{formatted_time}.csv"
        file_path = results_dir / file_name
        with open(file_path, "w", encoding="utf-8") as f:
            writer = csv.writer(f, dialect="unix")
            writer.writerows(result)
