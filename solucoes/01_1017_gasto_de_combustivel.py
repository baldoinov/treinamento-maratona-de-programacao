def main():
    A = int(input())
    B = int(input())

    dist = A * B
    consumo = dist / 12

    print(f"{consumo:.3f}")

if __name__ == "__main__":
    main()