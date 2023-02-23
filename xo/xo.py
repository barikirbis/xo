cell_w = 100
cell_margin = 10
field_w = cell_w * 3 + cell_margin * 4 

def cfg_canvas(width: int, height: int, canvas: Element) -> Context2d:
    """
    настройка канваса
    """
    ctx = canvas.getContext("2d")

    canvas.style.width = f"{width}px"
    canvas.style.height = f"{height}px"

    canvas.width = width
    canvas.height = height

    ctx.clearRect(0, 0, width, height)

    print("cfg_canvas")
    return ctx

def draw_cell(x, y, w, h, ctx: Context2d):
    """
    рисуем одну клетку поля
    """
    ctx.fillRect(x, y, w, h)
    print("draw_cell")

def main():
    cfg_canvas(field_w, field_w, document.getElementById("canva"))
    draw_cell(cell_margin, cell_margin, cell_w, cell_w, ctx)
    
