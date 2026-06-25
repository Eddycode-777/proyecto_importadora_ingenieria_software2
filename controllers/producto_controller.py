from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.producto_model import db, Producto

producto_bp = Blueprint('productos', __name__)

# Listar
@producto_bp.route('/')
def index():
    productos = Producto.query.order_by(Producto.id).all()
    return render_template('index.html', productos=productos)

# Crear - GET muestra formulario, POST guarda
@producto_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nuevo = Producto(
            nombre      = request.form['nombre'].strip(),
            descripcion = request.form['descripcion'].strip(),
            precio      = request.form['precio'],
            stock       = request.form['stock'],
            categoria   = request.form['categoria'].strip()
        )
        db.session.add(nuevo)
        db.session.commit()
        flash('Producto creado correctamente.', 'ok')
        return redirect(url_for('productos.index'))
    return render_template('crear.html')

# Editar - GET carga datos, POST actualiza
@producto_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    producto = Producto.query.get_or_404(id)
    if request.method == 'POST':
        producto.nombre      = request.form['nombre'].strip()
        producto.descripcion = request.form['descripcion'].strip()
        producto.precio      = request.form['precio']
        producto.stock       = request.form['stock']
        producto.categoria   = request.form['categoria'].strip()
        db.session.commit()
        flash('Producto actualizado.', 'ok')
        return redirect(url_for('productos.index'))
    return render_template('editar.html', producto=producto)

# Eliminar
@producto_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    flash('Producto eliminado.', 'ok')
    return redirect(url_for('productos.index'))
