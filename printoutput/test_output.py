from output import Print


if __name__ == "__main__":
    p = Print("#002", { "steak": 2, "bier": 3}, "15/06/2025", "14:05:19")

    p.print_tickets("localhost")
