from escpos.printer import Network


class Print():
    def __init__(self, id, items, date, time) -> None:
        self.id: str = id
        self.items: dict = items # item: number of item
        self.date: str = date
        self.time: str = time

    def print_tickets(self, printer_ip, port=9100):
        separator = "-" * 24  # length of separator line

        for item, count in self.items.items():
            for _ in range(count):
                printer = Network(printer_ip, port=port, profile="TM-m30III")

                # Print header with ID
                printer.set(align='left', font='a', width=1, height=1)
                printer.text(f"# {self.id}\n")
                
                # Separator line
                printer.text(f"{separator}\n")

                # Print quantity and item name
                printer.text(f"1 x {item}\n")

                # Separator line
                printer.text(f"{separator}\n")

                # Print date and time
                printer.text(f"{self.date}   {self.time}\n")

                printer.cut()
                printer.close()

    @staticmethod
    def from_str(string: str) -> "Print":
        id = ""
        items = {}
        date = ""
        time = ""
        for line in string:
            if line == "":
                continue
            if line[0] == "#":
                id = line[1:]
                continue
            if line[0] == "-":
                continue
            if line[0] in "1234567890":
                if line[2] == "/" or line[3] == "/":
                    split = line.split()
                    date = split[0]
                    time = split[1]
                    continue
                split = line.split()
                assert len(split) >= 3
                assert split[1] == "x"
                num = split[0]
                item = " ".join(split[2:])
                items[item] = num
            
        assert id != ""
        assert date != ""
        assert time != ""
        assert items != {}
        return Print(id, items, date, time)

