



def main():
    n = 10
    # print the table
    for i in range(1, n+1):
        for j in range(1, n+1):
             print(f"{i*j:4}", end=" " )
        print()
    pass

if __name__ == "__main__":
    main()