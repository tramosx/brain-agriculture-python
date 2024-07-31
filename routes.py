from flask import Blueprint, request, jsonify
from models import db, Produtor
from utils import valida_cpf_cnpj, valida_areas
from config import Config

routes_blueprint = Blueprint('routes', __name__)


@routes_blueprint.route('/produtores', methods=['POST'])
def cadastrar_produtor():
    data = request.get_json()
    cpf_cnpj = data.get('cpf_cnpj')
    if not valida_cpf_cnpj(cpf_cnpj):
        return jsonify({'error': 'CPF/CNPJ inválido'}), 400

    area_total = data.get('area_total')
    area_agricultavel = data.get('area_agricultavel')
    area_vegetacao = data.get('area_vegetacao')
    if not valida_areas(area_total, area_agricultavel, area_vegetacao):
        return jsonify({'error': 'Áreas inválidas'}), 400

    produtor = Produtor(
        cpf_cnpj=cpf_cnpj,
        nome_produtor=data.get('nome_produtor'),
        nome_fazenda=data.get('nome_fazenda'),
        cidade=data.get('cidade'),
        estado=data.get('estado'),
        area_total=area_total,
        area_agricultavel=area_agricultavel,
        area_vegetacao=area_vegetacao,
        culturas=','.join(data.get('culturas', []))
    )
    db.session.add(produtor)
    db.session.commit()
    return jsonify({'message': 'Produtor cadastrado com sucesso'}), 201

@routes_blueprint.route('/produtores/<int:id>', methods=['PUT'])
def editar_produtor(id):
    data = request.get_json()
    produtor = Produtor.query.get_or_404(id)

    if 'cpf_cnpj' in data and not valida_cpf_cnpj(data['cpf_cnpj']):
        return jsonify({'error': 'CPF/CNPJ inválido'}), 400
    
    produtor.cpf_cnpj = data.get('cpf_cnpj', produtor.cpf_cnpj)
    produtor.nome_produtor = data.get('nome_produtor', produtor.nome_produtor)
    produtor.nome_fazenda = data.get('nome_fazenda', produtor.nome_fazenda)
    produtor.cidade = data.get('cidade', produtor.cidade)
    produtor.estado = data.get('estado', produtor.estado)

    area_total = data.get('area_total', produtor.area_total)
    area_agricultavel = data.get('area_agricultavel', produtor.area_agricultavel)
    area_vegetacao = data.get('area_vegetacao', produtor.area_vegetacao)
    if not valida_areas(area_total, area_agricultavel, area_vegetacao):
        return jsonify({'error': 'Áreas inválidas'}), 400

    produtor.area_total = area_total
    produtor.area_agricultavel = area_agricultavel
    produtor.area_vegetacao = area_vegetacao
    produtor.culturas = ','.join(data.get('culturas', produtor.culturas.split(',')))

    db.session.commit()
    return jsonify({'message': 'Produtor atualizado com sucesso'}), 200

@routes_blueprint.route('/produtores/<int:id>', methods=['DELETE'])
def excluir_produtor(id):
    produtor = Produtor.query.get_or_404(id)
    db.session.delete(produtor)
    db.session.commit()
    return jsonify({'message': 'Produtor excluído com sucesso'}), 200


@routes_blueprint.route('/produtores', methods=['GET'])
def listar_produtores():
    produtores = Produtor.query.all()  # Consulta todos os produtores
    return jsonify([produtor.to_dict() for produtor in produtores]), 200
