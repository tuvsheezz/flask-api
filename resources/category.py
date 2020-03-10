from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.category import CategoryModel
from db import db

class Categories(Resource):
    # @jwt_required()
    def get(self):
        conn = db.connect()
        return conn.execute("select 5")
        return {'categories': list(map(lambda x: x.json(), CategoryModel.query.all()))}


class ShowCategory(Resource):
    # @jwt_required()
    def get(self, id):
        category = CategoryModel.find_by_id(id)
        if category:
            return category.json()
        return {'message': 'Category not found'}, 404


class CreateCategory(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help="This field cannot be left blank!")

    # @jwt_required()
    def post(self):
        data = CreateCategory.parser.parse_args()
        if CategoryModel.find_by_name(data['name']):
            return {'message': "An category with name '{}' already exists.".format(data['name'])}, 400

        category = CategoryModel(**data)

        try:
            category.save_to_db()
        except:
            return {"message": "An error occurred inserting the category."}, 500

        return category.json(), 201


class EditCategory(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help="This field cannot be left blank!")

    # @jwt_required()
    def put(self, id):
        data = EditCategory.parser.parse_args()
        ex_category = CategoryModel.find_by_name(data['name'])

        if ex_category and ex_category.id != id:
            return {'message': "An category with name '{}' already exists.".format(data['name'])}, 400

        category = CategoryModel.find_by_id(id)

        if category:
            category.name = data['name']
        else:
            category = CategoryModel(**data)

        category.save_to_db()
        return category.json()


class DeleteCategory(Resource):
    # @jwt_required()
    def delete(self, id):
        category = CategoryModel.find_by_id(id)
        if category:
            category.delete_from_db()
            return {'message': 'Category deleted.'}
        return {'message': 'Category not found.'}, 404
