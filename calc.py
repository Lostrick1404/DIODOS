from decimal import Decimal, getcontext
getcontext().prec = 60
def solve_jfet_design():
    VDD, VDS, ID_target, VG, R2 = Decimal("15"), Decimal("6"), Decimal("0.004"), Decimal("0.15"), Decimal("10000")
    IDSS_a, VP_a = Decimal("0.005"), Decimal("-6")
    VGS = VP_a * (Decimal("1") - (ID_target / IDSS_a).sqrt())
    VS = VG - VGS
    RS, RD = VS / ID_target, (VDD - VDS - VS) / ID_target
    R1 = (VDD * R2 / VG) - R2
    print(f"--- Design ---\nVGS: {VGS}\nVS: {VS}\nRS: {RS}\nRD: {RD}\nR1: {R1}\n")
    test_params = [(Decimal("0.001"), Decimal("-0.5")), (Decimal("0.003"), Decimal("-3.25")), (Decimal("0.005"), Decimal("-6"))]
    for idss, vp in test_params:
        id_q, vds_q = solve_circuit(VG, RS, RD, VDD, idss, vp)
        print(f"P: IDSS={idss*1000}, VP={vp} => ID={id_q*1000}, VDS={vds_q}")
    R1_c, R2_c, RS_c, RD_c = Decimal("1000000"), Decimal("10000"), Decimal("200"), Decimal("2050")
    VG_c = VDD * R2_c / (R1_c + R2_c)
    print(f"\n--- Commercial (VG={VG_c}) ---")
    for idss, vp in test_params:
        id_q, vds_q = solve_circuit(VG_c, RS_c, RD_c, VDD, idss, vp)
        print(f"P: IDSS={idss*1000}, VP={vp} => ID={id_q*1000}, VDS={vds_q}")
def solve_circuit(VG, RS, RD, VDD, IDSS, VP):
    k, X = IDSS / (VP**2), VG - VP
    a, b, c = k * (RS**2), -(Decimal("1") + 2 * k * RS * X), k * (X**2)
    sd = (b**2 - 4*a*c).sqrt()
    id1, id2 = (-b + sd) / (2 * a), (-b - sd) / (2 * a)
    id_q = id1 if id1 < (VG - VP) / RS else id2
    return id_q, VDD - id_q * (RD + RS)
if __name__ == "__main__": solve_jfet_design()
