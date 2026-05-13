#!/usr/bin/env python3
"""
ui_tkinter.py — Interfaz gráfica para la calculadora de BJT (Práctica 3)
==============================================================================
Interfaz gráfica interactiva usando Tkinter y matplotlib.

::SCRIPT_METADATA::
script_id    : practica3-ui-tkinter
module       : BJT
generates    : interfaz gráfica interactiva
last_updated : 2026-05-12
"""

import matplotlib
matplotlib.use("TkAgg")

import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import sys
from pathlib import Path

# Agregar directorio actual al path para imports relativos
sys.path.insert(0, str(Path(__file__).parent))

try:
    from core import InputParams, CalcResults, calcular_polarizacion, validate_params
    import plotting
    import schematic_render
except ImportError:
    # Si se ejecuta como módulo
    from .core import InputParams, CalcResults, calcular_polarizacion, validate_params
    from . import plotting
    from . import schematic_render

class App(tk.Tk):
    """Ventana principal de la calculadora BJT."""

    # Paleta Pastel Claro (Soft & Professional)
    BG_MAIN = "#f8f9fa"      # Blanco grisáceo muy suave
    BG_PANEL = "#ffffff"     # Blanco puro para paneles
    BG_TAB = "#edf2f4"       # Gris azulado muy tenue para pestañas
    BG_ENTRY = "#ffffff"     # Fondo entrada blanco
    FG_TITLE = "#2d3436"     # Gris oscuro para títulos
    FG_LABEL = "#636e72"     # Gris medio para etiquetas
    FG_VALUE = "#6c5ce7"     # Lavanda Pastel (Valor principal)
    FG_WARN = "#ff7675"      # Rosa Pastel (Alertas)
    ACCENT = "#a29bfe"       # Lavanda suave
    ACCENT_MINT = "#55efc4"  # Menta suave

    def __init__(self):
        super().__init__()
        self.title("Calculadora de Polarización BJT — Práctica 3 | ITT")
        self.configure(bg=self.BG_MAIN)
        self.geometry("1100x750")
        self.minsize(900, 600)

        # Variables de entrada
        default = InputParams()
        self._params = {
            "Vcc": tk.StringVar(value=str(default.Vcc)),
            "R1": tk.StringVar(value=str(default.R1)),
            "R2": tk.StringVar(value=str(default.R2)),
            "Rc": tk.StringVar(value=str(default.Rc)),
            "Re": tk.StringVar(value=str(default.Re)),
            "beta": tk.StringVar(value=str(default.beta)),
            "Vbe": tk.StringVar(value=str(default.Vbe)),
        }

        self._results: CalcResults = None
        self._input_p: InputParams = None

        self._build_styles()
        self._build_gui()
        self._calcular()

    def _build_styles(self):
        s = ttk.Style(self)
        s.theme_use("clam")
        s.configure("TNotebook", background=self.BG_MAIN, borderwidth=0)
        s.configure("TNotebook.Tab", background=self.BG_TAB, foreground=self.FG_LABEL, padding=[12, 4], borderwidth=0)
        s.map("TNotebook.Tab", 
              background=[("selected", self.BG_PANEL)], 
              foreground=[("selected", self.FG_VALUE)])
        
        s.configure("TFrame", background=self.BG_PANEL)
        s.configure("TLabel", background=self.BG_PANEL, foreground=self.FG_LABEL)
        s.configure("TEntry", fieldbackground=self.BG_ENTRY, foreground=self.FG_TITLE, insertbackground=self.FG_TITLE)
        
        s.configure("Calc.TButton", background=self.ACCENT, foreground="#ffffff", font=("Consolas", 10, "bold"), borderwidth=0)
        s.map("Calc.TButton", background=[("active", self.ACCENT_MINT)])
        
        s.configure("Vertical.TScrollbar", background=self.BG_TAB, arrowcolor=self.FG_LABEL)

    def _get_latex_image(self, tex, width=0.8, height=0.3):
        """Renderiza una cadena LaTeX a PhotoImage usando Matplotlib con fondo claro."""
        key = (tex, width, height)
        if not hasattr(self, "_latex_cache"):
            self._latex_cache = {}
        if key not in self._latex_cache:
            import io, base64
            from matplotlib.backends.backend_agg import FigureCanvasAgg
            fig = Figure(figsize=(width, height), facecolor=self.BG_PANEL)
            FigureCanvasAgg(fig)
            fig.text(0, 0.5, f"${tex}$", fontsize=11, color=self.FG_LABEL, ha='left', va='center')
            buf = io.BytesIO()
            fig.savefig(buf, format='png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0.02)
            buf.seek(0)
            self._latex_cache[key] = tk.PhotoImage(data=base64.b64encode(buf.read()))
        return self._latex_cache[key]

    def _build_gui(self):
        main = tk.Frame(self, bg=self.BG_MAIN)
        main.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Header
        hdr = tk.Frame(main, bg=self.BG_MAIN)
        hdr.pack(fill=tk.X, pady=(0, 15))
        tk.Label(hdr, text="PRÁCTICA 3 — POLARIZACIÓN DE TRANSISTOR BJT (EMISOR COMÚN)", 
                 bg=self.BG_MAIN, fg=self.FG_TITLE, font=("Consolas", 12, "bold")).pack(side=tk.LEFT)
        
        paned = tk.PanedWindow(main, orient=tk.HORIZONTAL, bg=self.BG_MAIN, sashwidth=2, bd=0)
        paned.pack(fill=tk.BOTH, expand=True)

        # Panel Izquierdo (Inputs)
        left = tk.Frame(paned, bg=self.BG_PANEL, width=280)
        paned.add(left)
        self._build_input_panel(left)

        # Panel Derecho (Gráfica y Resumen)
        right = tk.Frame(paned, bg=self.BG_MAIN)
        paned.add(right)
        
        nb = ttk.Notebook(right)
        nb.pack(fill=tk.BOTH, expand=True)
        
        self._tab_plot = tk.Frame(nb, bg=self.BG_TAB)
        self._tab_resumen = tk.Frame(nb, bg=self.BG_TAB)
        self._tab_esquema = tk.Frame(nb, bg=self.BG_TAB)
        
        nb.add(self._tab_plot, text=" Recta de Carga ")
        nb.add(self._tab_resumen, text=" Resumen de Cálculos ")
        nb.add(self._tab_esquema, text=" Esquema del Circuito ")
        
        self._build_tab_plot(self._tab_plot)
        self._build_tab_resumen(self._tab_resumen)
        self._build_tab_esquema(self._tab_esquema)

    def _build_input_panel(self, parent):
        tk.Label(parent, text="DATOS DE DISEÑO", bg=self.BG_PANEL, fg=self.FG_TITLE, 
                 font=("Consolas", 12, "bold")).pack(pady=(15, 10))
        
        def entry_latex(tex_label, var, unit):
            # Línea divisoria superior
            tk.Frame(parent, bg=self.BG_TAB, height=1).pack(fill=tk.X, padx=10)
            
            row = tk.Frame(parent, bg=self.BG_PANEL)
            row.pack(fill=tk.X, padx=10, pady=8)
            
            # Contenedor para el label con ancho fijo para alinear
            lbl_container = tk.Frame(row, bg=self.BG_PANEL, width=60, height=35)
            lbl_container.pack_propagate(False)
            lbl_container.pack(side=tk.LEFT)
            
            # Label con imagen LaTeX
            img = self._get_latex_image(tex_label, width=0.9, height=0.4)
            lbl = tk.Label(lbl_container, image=img, bg=self.BG_PANEL)
            lbl.image = img
            lbl.pack(expand=True)
            
            tk.Entry(row, textvariable=var, width=12, bg=self.BG_ENTRY, fg=self.FG_TITLE, 
                     insertbackground=self.FG_TITLE, borderwidth=1, relief=tk.SOLID,
                     font=("Consolas", 11)).pack(side=tk.LEFT, padx=10)
            
            tk.Label(row, text=unit, font=("Consolas", 11), fg=self.FG_LABEL).pack(side=tk.LEFT)

        entry_latex("V_{CC}", self._params["Vcc"], "V")
        entry_latex("R_1", self._params["R1"], "Ω")
        entry_latex("R_2", self._params["R2"], "Ω")
        entry_latex("R_C", self._params["Rc"], "Ω")
        entry_latex("R_E", self._params["Re"], "Ω")
        entry_latex("\\beta", self._params["beta"], "(hFE)")
        entry_latex("V_{BE}", self._params["Vbe"], "V")
        
        # Línea de cierre
        tk.Frame(parent, bg=self.BG_TAB, height=1).pack(fill=tk.X, padx=10)

        ttk.Button(parent, text="RECALCULAR ANÁLISIS", style="Calc.TButton", command=self._calcular).pack(fill=tk.X, padx=20, pady=25)

    def _build_tab_plot(self, parent):
        self._fig = Figure(figsize=(6, 5), facecolor=self.BG_MAIN)
        self._canvas = FigureCanvasTkAgg(self._fig, master=parent)
        self._canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        toolbar_frame = tk.Frame(parent, bg=self.BG_TAB)
        toolbar_frame.pack(fill=tk.X)
        NavigationToolbar2Tk(self._canvas, toolbar_frame)

    def _build_tab_resumen(self, parent):
        """Pestaña de resumen con tablas y renderizado LaTeX."""
        # Canvas con Scrollbar para contenido largo
        canvas = tk.Canvas(parent, bg=self.BG_MAIN, highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        self._scroll_frame = tk.Frame(canvas, bg=self.BG_MAIN)

        self._scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self._scroll_frame, anchor="nw", width=800)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True, padx=20)
        scrollbar.pack(side="right", fill="y")

        # Vincular rueda del ratón
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

    def _build_tab_esquema(self, parent):
        """Pestaña para mostrar el diagrama del circuito renderizado dinámicamente usando Matplotlib."""
        import schematic_render
        
        # Crear figura de Matplotlib para el esquema
        self._fig_esquema = Figure(figsize=(6, 8), facecolor=self.BG_MAIN)
        self._canvas_esquema = FigureCanvasTkAgg(self._fig_esquema, master=parent)
        self._canvas_esquema.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Agregar barra de herramientas (opcional, pero útil para zoom)
        toolbar_frame = tk.Frame(parent, bg=self.BG_TAB)
        toolbar_frame.pack(fill=tk.X)
        NavigationToolbar2Tk(self._canvas_esquema, toolbar_frame)
        
        # Renderizado inicial
        schematic_render.draw_bjt_schematic(self._fig_esquema)
        self._canvas_esquema.draw()

    def _calcular(self):
        try:
            p = InputParams(
                Vcc=float(self._params["Vcc"].get()),
                R1=float(self._params["R1"].get()),
                R2=float(self._params["R2"].get()),
                Rc=float(self._params["Rc"].get()),
                Re=float(self._params["Re"].get()),
                beta=float(self._params["beta"].get()),
                Vbe=float(self._params["Vbe"].get()),
            )
            
            valid, msg = validate_params(p)
            if not valid:
                messagebox.showerror("Error", msg)
                return
            
            self._input_p = p
            self._results = calcular_polarizacion(p)
            
            self._update_plot()
            self._update_resumen()
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

    def _update_plot(self):
        self._fig.clear()
        plotting.plot_load_line(self._fig, self._input_p, self._results)
        self._canvas.draw()

    def _update_resumen(self):
        r = self._results
        
        # Limpiar frame anterior
        for widget in self._scroll_frame.winfo_children():
            widget.destroy()

        def add_header(text):
            lbl = tk.Label(self._scroll_frame, text=text, bg=self.BG_MAIN, fg=self.FG_TITLE, 
                           font=("Consolas", 16, "bold"), pady=20)
            lbl.pack(anchor="w")

        def add_section_table(title, rows):
            # Contenedor de sección
            sec_frame = tk.Frame(self._scroll_frame, bg=self.BG_PANEL, padx=20, pady=15, 
                                 highlightbackground=self.BG_TAB, highlightthickness=1)
            sec_frame.pack(fill="x", pady=(0, 25), padx=5)
            
            tk.Label(sec_frame, text=title, bg=self.BG_PANEL, fg=self.FG_VALUE, 
                     font=("Consolas", 12, "bold")).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 15))
            
            # Encabezados de tabla
            headers = ["Símbolo", "Descripción", "Valor", "Unidad"]
            for col, h in enumerate(headers):
                tk.Label(sec_frame, text=h, bg=self.BG_PANEL, fg=self.FG_LABEL, 
                         font=("Consolas", 10, "bold", "italic")).grid(row=1, column=col, sticky="w", padx=15, pady=(0, 5))

            # Filas de datos
            for i, (tex, desc, val, unit, is_highlight) in enumerate(rows):
                row_idx = (i * 2) + 2
                
                # Línea de división horizontal entre filas
                sep = tk.Frame(sec_frame, bg="#f1f2f6", height=1)
                sep.grid(row=row_idx, column=0, columnspan=4, sticky="ew", pady=5)
                
                curr_row = row_idx + 1
                
                # Símbolo LaTeX
                img = self._get_latex_image(tex, width=0.8, height=0.4)
                l_sym = tk.Label(sec_frame, image=img, bg=self.BG_PANEL)
                l_sym.image = img
                l_sym.grid(row=curr_row, column=0, sticky="w", padx=15, pady=4)
                
                # Descripción
                tk.Label(sec_frame, text=desc, bg=self.BG_PANEL, fg=self.FG_LABEL,
                         font=("Consolas", 11)).grid(row=curr_row, column=1, sticky="w", padx=15)
                
                # Valor
                color = self.FG_VALUE if is_highlight else "#2d3436"
                tk.Label(sec_frame, text=val, bg=self.BG_PANEL, fg=color,
                         font=("Consolas", 12, "bold")).grid(row=curr_row, column=2, sticky="w", padx=15)
                
                # Unidad
                tk.Label(sec_frame, text=unit, bg=self.BG_PANEL, fg=self.FG_LABEL,
                         font=("Consolas", 11)).grid(row=curr_row, column=3, sticky="w", padx=15)

        add_header("ANÁLISIS DE POLARIZACIÓN BJT")

        # 1. Thévenin
        add_section_table("1. EQUIVALENTE THÉVENIN EN BASE", [
            ("V_{th}", "Voltaje de Thévenin", f"{r.Vth:.4f}", "V", False),
            ("R_{th}", "Resistencia de Thévenin", f"{r.Rth:.2f}", "Ω", False),
        ])

        # 2. Corrientes
        add_section_table("2. CORRIENTES DE OPERACIÓN", [
            ("I_{b}", "Corriente de Base", f"{r.Ib*1e6:.3f}", "μA", False),
            ("I_{c}", "Corriente de Colector", f"{r.Ic*1e3:.3f}", "mA", False),
            ("I_{e}", "Corriente de Emisor", f"{r.Ie*1e3:.3f}", "mA", False),
            ("\\alpha", "Factor Alfa", f"{r.alpha:.4f}", "-", False),
        ])

        # 3. Voltajes y Punto Q
        add_section_table("3. VOLTAJES DE NODOS Y PUNTO Q", [
            ("V_{b}", "Voltaje en Base", f"{r.Vb:.3f}", "V", False),
            ("V_{c}", "Voltaje en Colector", f"{r.Vc:.3f}", "V", False),
            ("V_{e}", "Voltaje en Emisor", f"{r.Ve:.3f}", "V", False),
            ("V_{ce}(Q)", "Punto de Operación Q", f"{r.Vce:.4f}", "V", True),
        ])

        # 4. Potencias
        add_section_table("4. ANÁLISIS DE POTENCIA (DISIPACIÓN)", [
            ("P_{R1}", "Potencia en R1", f"{r.Pr1*1e3:.2f}", "mW", False),
            ("P_{R2}", "Potencia en R2", f"{r.Pr2*1e3:.2f}", "mW", False),
            ("P_{Rc}", "Potencia en Rc", f"{r.Prc*1e3:.2f}", "mW", False),
            ("P_{Re}", "Potencia en Re", f"{r.Pre*1e3:.2f}", "mW", False),
            ("P_{Q}", "Potencia en Transistor", f"{r.Pq*1e3:.2f}", "mW", True),
        ])

        # 5. Recta de Carga
        add_section_table("5. LÍMITES DE LA RECTA DE CARGA", [
            ("I_{c(sat)}", "Corriente de Saturación", f"{r.Ic_sat*1e3:.2f}", "mA", False),
            ("V_{ce(off)}", "Voltaje de Corte", f"{r.Vce_off:.2f}", "V", False),
        ])

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
