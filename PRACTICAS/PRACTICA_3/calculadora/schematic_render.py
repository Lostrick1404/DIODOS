import schemdraw
import schemdraw.elements as elm
from matplotlib.figure import Figure

def draw_bjt_schematic(fig: Figure):
    """
    Dibuja el esquema del circuito BJT directamente en una figura de Matplotlib.
    Compatible con schemdraw 0.15+ (usando backend de Matplotlib).
    """
    # Limpiar figura y preparar eje
    fig.clear()
    ax = fig.add_subplot(111)
    
    # Crear dibujo de schemdraw especificando el backend
    # El backend 'matplotlib' es necesario para integrarse con FigureCanvasTkAgg
    d = schemdraw.Drawing(backend='matplotlib')
    d.config(unit=2.5, fontsize=12)
    
    # --- COMPONENTES ---
    # Transistor NPN
    Q = d.add(elm.BjtNpn().anchor('base'))
    d.add(elm.Label().at(Q.center).label('Q1', loc='right', ofst=(0.6, 0)))
    
    # Nodo de base
    d.add(elm.Line().left().at(Q.base).length(1.0))
    B_node = d.add(elm.Dot())
    
    # Niveles de voltaje
    vcc_level = 3.5
    gnd_level = -3.5
    
    # Divisor de Voltaje y Polarización
    R1 = d.add(elm.Resistor().up().at(B_node.center).toy(vcc_level).label('$R_1$'))
    R2 = d.add(elm.Resistor().down().at(B_node.center).toy(gnd_level).label('$R_2$'))
    RC = d.add(elm.Resistor().up().at(Q.collector).toy(vcc_level).label('$R_C$'))
    RE = d.add(elm.Resistor().down().at(Q.emitter).toy(gnd_level).label('$R_E$'))
    
    # --- CONEXIONES ---
    d.add(elm.Line().at(R1.end).to(RC.end))
    d.add(elm.Vdd().at(RC.end).label('$V_{CC}$'))
    d.add(elm.Line().at(R2.end).to(RE.end))
    d.add(elm.Ground().at(RE.end))
    
    # Marcado de voltajes
    d.add(elm.Label().at(Q.base).label('$V_B$', loc='left', ofst=(-0.3, 0.3)))
    d.add(elm.Label().at(Q.collector).label('$V_C$', loc='left', ofst=(-0.3, 0.3)))
    d.add(elm.Label().at(Q.emitter).label('$V_E$', loc='left', ofst=(-0.3, -0.3)))

    # Realizar el dibujo en el AXIS de Matplotlib
    # show=False evita que schemdraw intente llamar a plt.show()
    d.draw(canvas=ax, show=False)
    
    # Estética final: Pastel Claro
    ax.set_facecolor("#ffffff") 
    fig.patch.set_facecolor("#f8f9fa") # Fondo exterior pastel claro
    
    # Asegurar que el fondo del eje sea visible
    ax.set_axis_off()
    ax.patch.set_visible(True) 
    
    # CRÍTICO: Mantener relación de aspecto igual para evitar que se estire
    ax.set_aspect('equal')
    
    # Ajustar márgenes suavemente
    fig.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
