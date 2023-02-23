from pyodide.ffi import to_js, create_proxy
from js import (
    document,
    CanvasRenderingContext2D as Context2d,
)

cell_w = 100
cell_margin = 10
field_w = cell_w * 3 + cell_margin * 4 

def cfg_canvas(width: int, height: int, canvas) -> Context2d:
    """
    настройка канваса
    """
    ctx = canvas.getContext("2d")

    canvas.style.width = f"{width}px"
    canvas.style.height = f"{height}px"

    canvas.width = width
    canvas.height = height

    ctx.clearRect(0, 0, width, height)

    return ctx

def draw_cell(x, y, w, h, ctx: Context2d):
    """
    рисуем одну клетку поля
    """
    ctx.fillRect(x, y, w, h)

def draw_field(cell_w, cell_margin, ctx: Context2d):
    """
    рисуем игровое поле 3х3
    """
    for i in range(3):
        for j in range(3):
            x = cell_margin * (i+1) + cell_w * i
            y = cell_margin * (j+1) + cell_w * j
            draw_cell(x, y, cell_w, cell_w, ctx)

def main():
    ctx = cfg_canvas(field_w, field_w, document.getElementById("canva"))
    #draw_cell(cell_margin, cell_margin, cell_w, cell_w, ctx)
    draw_field(cell_w, cell_margin, ctx)
