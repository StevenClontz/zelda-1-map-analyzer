from analyzer.extrator import DataExtractor

with open("zelda1.nes", "rb") as f:
    d = DataExtractor(f)
    print(d.level_info)
