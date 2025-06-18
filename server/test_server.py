from escpos.printer import Network

def main():
    p = Network("localhost", port=9100)
    p.text("Hello from a real POS system!\n")
    p.cut()

if __name__ == "__main__":
    main()
