def kroonid_eurodeks(kroonid):
    vahetuskurss = 0.086
    eurod = kroonid * vahetuskurss
    return eurod
def main():
    try:
        kroonid = float(input("Sisestage summa Rootsi kroonides: "))
        eurod = kroonid_eurodeks(kroonid)
        eurod_umberdatud = round(eurod, 2)
        print(f"{kroonid} Rootsi krooni on {eurod_umberdatud} eurot.")
    except ValueError:
        print("Vigane sisend. Palun sisestage number.")

if __name__ == "__main__":
    main()