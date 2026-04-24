import matplotlib.pyplot as plt
import numpy as np

def generate_load_line_final():
    # Parámetros del circuito
    Vcc = 12
    Rc_plus_Re = 1200 
    beta = 100
    Va = 100 
    
    # Valores de Ib (6 curvas)
    ib_values = [10, 20, 30, 40, 50, 60] 
    
    # Eje X (Vce)
    vce_range = np.linspace(0, Vcc + 2, 200)
    
    plt.figure(figsize=(10, 7))
    
    # Graficar curvas del transistor (Gris suave)
    for ib in ib_values:
        ic_base = (beta * ib / 1000) 
        ic_curve = ic_base * (1 + vce_range / Va)
        plt.plot(vce_range, ic_curve, color='#cccccc', linewidth=0.8, alpha=0.6)
        plt.text(Vcc + 0.3, ic_curve[-1], r'$I_{B%d} = %d\mu A$' % (ib//10, ib), fontsize=9)

    # Graficar recta de carga DC (AZUL solicitado)
    vce_recta = np.linspace(0, Vcc, 100)
    ic_recta = (Vcc - vce_recta) / Rc_plus_Re * 1000 
    plt.plot(vce_recta, ic_recta, color='#0000ff', linewidth=2.5, label='Recta de Carga DC')
    
    # Señalar puntos extremos con fórmulas
    ic_sat = Vcc / Rc_plus_Re * 1000
    plt.plot(0, ic_sat, 'bo', markersize=8)
    plt.annotate(r'Saturación: $\frac{V_{CC}}{R_C + R_E}$', 
                 xy=(0, ic_sat), xytext=(0.5, ic_sat + 0.5),
                 arrowprops=dict(arrowstyle='->', color='blue'))
    
    plt.plot(Vcc, 0, 'bo', markersize=8)
    plt.annotate(r'Corte: $V_{CC}$', 
                 xy=(Vcc, 0), xytext=(Vcc - 2, 1.0),
                 arrowprops=dict(arrowstyle='->', color='blue'))
    
    # Estética
    plt.title('Recta de Carga DC y Curvas Características (BJT)')
    plt.xlabel('$V_{CE}$ [Voltios]')
    plt.ylabel('$I_C$ [miliAmperios]')
    plt.grid(True, linestyle=':', alpha=0.5)
    plt.axhline(0, color='black', lw=1.2)
    plt.axvline(0, color='black', lw=1.2)
    plt.ylim(0, ic_sat + 2)
    plt.xlim(0, Vcc + 3)
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('topics/02-transistor-bjt/assets/bjt-recta-carga-divisor.png')
    plt.close()

if __name__ == "__main__":
    generate_load_line_final()
    print("Gráfico final (Azul + Fórmulas) generado.")
