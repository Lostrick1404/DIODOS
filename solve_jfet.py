from decimal import Decimal, getcontext
getcontext().prec = 70
def solve():
    R1 = Decimal("1000000")
    R2 = Decimal("10000")
    RS = Decimal("180")
    RD = Decimal("2200")
    VDD = Decimal("15")
    VG = VDD * (R2 / (R1 + R2))
    print(f"VG: {VG:.60f}")
    parameter_sets = [
        (Decimal("0.001"), Decimal("-0.5")),
        (Decimal("0.003"), Decimal("-3.25")),
        (Decimal("0.005"), Decimal("-6"))
    ]
    for idss, vp in parameter_sets:
        K = 1 - (VG / vp)
        L = RS / vp
        a = idss * (L ** 2)
        b = 2 * K * L * idss - 1
        c = idss * (K ** 2)
        discriminant = b**2 - 4*a*c
        sqrt_disc = discriminant.sqrt()
        id1 = (-b + sqrt_disc) / (2 * a)
        id2 = (-b - sqrt_disc) / (2 * a)
        results = []
        for id_val in [id1, id2]:
            vgsq = VG - id_val * RS
            if id_val >= 0 and vgsq >= vp:
                vdsq = VDD - id_val * (RD + RS)
                results.append((id_val, vgsq, vdsq))
        if results:
            idq, vgsq, vdsq = min(results, key=lambda x: x[0])
            print(f"SET IDSS={idss} VP={vp}")
            print(f"IDQ={idq:.60f}")
            print(f"VGSQ={vgsq:.60f}")
            print(f"VDSQ={vdsq:.60f}")
solve()
solve()
