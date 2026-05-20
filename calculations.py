from decimal import Decimal, getcontext

# Set precision
getcontext().prec = 60

def solve_jfet_design():
    # Design constants
    VDD = Decimal('15')
    VDS = Decimal('6')
    ID_target = Decimal('0.004') # 4 mA
    VG = Decimal('0.15')
    R2 = Decimal('10000') # 10 kOhm
    
    # Anchor case
    IDSS_anchor = Decimal('0.005') # 5 mA
    VP_anchor = Decimal('-6')
    
    # Square root of (ID / IDSS)
    ratio = ID_target / IDSS_anchor
    # ID = IDSS(1 - VGS/VP)^2  => sqrt(ID/IDSS) = 1 - VGS/VP  => VGS/VP = 1 - sqrt(ID/IDSS)
    VGS = VP_anchor * (Decimal('1') - ratio.sqrt())
    
    # VS = VG - VGS
    VS = VG - VGS
    
    # RS = VS / ID
    RS = VS / ID_target
    
    # RD = (VDD - VDS - VS) / ID
    RD = (VDD - VDS - VS) / ID_target
    
    # VG = VDD * R2 / (R1 + R2) => R1 + R2 = VDD * R2 / VG => R1 = (VDD * R2 / VG) - R2
    R1 = (VDD * R2 / VG) - R2
    
    print("--- Design Calculation (Anchor Case: IDSS=5mA, VP=-6V) ---")
    print(f"VGS: {VGS}")
    print(f"VS:  {VS}")
    print(f"RS:  {RS}")
    print(f"RD:  {RD}")
    print(f"R1:  {R1}")
    print()

    # Three Q-points for design values (checking parameters)
    test_params = [
        (Decimal('0.001'), Decimal('-0.5')),
        (Decimal('0.003'), Decimal('-3.25')),
        (Decimal('0.005'), Decimal('-6'))
    ]
    
    print("--- Q-points for Design Resistance Values ---")
    print(f"Using RS={RS}, RD={RD}, VG={VG}")
    for idss, vp in test_params:
        id_q, vds_q = solve_circuit(VG, RS, RD, VDD, idss, vp)
        print(f"Params: IDSS={idss*1000}mA, VP={vp}V => ID={id_q*1000}mA, VDS={vds_q}V")
    print()

    # Commercial case
    R1_comm = Decimal('1000000') # 1.0 MOhm
    R2_comm = Decimal('10000')   # 10 kOhm
    RS_comm = Decimal('200')     # 200 Ohm
    RD_comm = Decimal('2050')    # 2.05 kOhm
    
    VG_comm = VDD * R2_comm / (R1_comm + R2_comm)
    
    print("--- Commercial Case Calculation ---")
    print(f"VG: {VG_comm}")
    for idss, vp in test_params:
        id_q, vds_q = solve_circuit(VG_comm, RS_comm, RD_comm, VDD, idss, vp)
        print(f"Params: IDSS={idss*1000}mA, VP={vp}V => ID={id_q*1000}mA, VDS={vds_q}V")

def solve_circuit(VG, RS, RD, VDD, IDSS, VP):
    # k = IDSS / VP^2
    # ID = k * (VGS - VP)^2
    # VGS = VG - ID * RS
    # ID = k * (VG - ID * RS - VP)^2
    # Let X = VG - VP
    # ID = k * (X - ID * RS)^2 = k * (X^2 - 2*X*ID*RS + ID^2 * RS^2)
    # k*RS^2 * ID^2 - (1 + 2*k*RS*X) * ID + k*X^2 = 0
    k = IDSS / (VP**2)
    X = VG - VP
    a = k * (RS**2)
    b = -(Decimal('1') + 2 * k * RS * X)
    c = k * (X**2)
    
    # Discriminant
    discriminant = b**2 - 4*a*c
    sqrt_disc = discriminant.sqrt()
    
    # Roots
    id1 = (-b + sqrt_disc) / (2 * a)
    id2 = (-b - sqrt_disc) / (2 * a)
    
    # The valid root must have VGS > VP, i.e., ID * RS < VG - VP  => ID < (VG - VP) / RS
    limit = (VG - VP) / RS
    
    if id1 < limit:
        id_q = id1
    else:
        id_q = id2

    vds_q = VDD - id_q * (RD + RS)
    return id_q, vds_q

if __name__ == "__main__":
    solve_jfet_design()
