import schemdraw
import schemdraw.elements as elm
from pathlib import Path
import matplotlib.pyplot as plt

def generate_bjt_schematic():
    # Definir ruta de salida a SVG
    output_path = Path("PRACTICAS/PRACTICA_3/esquema_bjt_polarizacion.svg")
    
    # Asegurar que el directorio existe
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Configuración CRÍTICA: Exportar texto como trazados vectoriales (paths)
    # Esto soluciona que los símbolos desaparezcan en motores SVG limitados (como tksvg)
    plt.rcParams['svg.fonttype'] = 'path'

    d = schemdraw.Drawing(show=False)
    # Configuración estética con fondo blanco explícito
    d.config(unit=2.5, fontsize=12, bgcolor='white')
    
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

    # Guardar como SVG
    d.save(str(output_path))
    
    # Post-procesamiento: Asegurar fondo blanco sólido en el XML
    with open(output_path, 'r', encoding='utf-8') as f:
        svg_content = f.read()
    
    # Reemplazar el primer patch fill:none por fill:white
    svg_content = svg_content.replace('style="fill: none"', 'style="fill: #ffffff"', 1)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)

if __name__ == "__main__":
    try:
        generate_bjt_schematic()
        print("Esquema BJT generado exitosamente (SVG + Text-to-Path + Fondo Blanco)")
    except Exception as e:
        print(f"Error al generar el esquema: {e}")
