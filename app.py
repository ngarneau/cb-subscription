# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api
import datetime

app = Flask(__name__)
api = Api(app)

famous_date = datetime.datetime(1970, 1, 1)

class HelloWorld(Resource):
    def post(self):
        data = request.get_json()
        q = data["q"]
        paragraphs = data["paragraphs"]
        matched_paragraphs = []
        for key, value in paragraphs.iteritems():
            if q in value:
                matched_paragraphs.append(key)
        return self.build_response(matched_paragraphs)

    def build_response(self, matched_paragraphs):
        return {
            'teamName': 'Jumpers',
            'matchedParagraphs': matched_paragraphs,
            'teamMembers': self.build_members()
        }

    def build_members(self):
        return [
            self.build_nic(),
            self.build_jo(),
            self.build_ul(),
        ]

    def build_nic(self):
        return {
            'firstName': 'Nicolas',
            'lastName': 'Garneau',
            'email': 'nicolas.garneau.1@ulaval.ca',
            'phoneNumber': '418-569-3097',
            'educationalEstablishment': 'Université Laval',
            'studyProgram': 'Baccalauréat en Informatique',
            'dateProgramEnd': (datetime.datetime(2016, 5, 1,)-famous_date).total_seconds(),
            'inCharge': True
        }

    def build_jo(self):
        return {
            'firstName': 'Nicolas',
            'lastName': 'Garneau',
            'email': 'nicolas.garneau.1@ulaval.ca',
            'phoneNumber': '418-569-3097',
            'educationalEstablishment': 'Universite Laval',
            'studyProgram': 'Informatique',
            'dateProgramEnd': (datetime.datetime(2016, 5, 1,)-famous_date).total_seconds(),
            'inCharge': False
        }

    def build_ul(self):
        return {
            'firstName': 'Nicolas',
            'lastName': 'Garneau',
            'email': 'nicolas.garneau.1@ulaval.ca',
            'phoneNumber': '418-569-3097',
            'educationalEstablishment': 'Universite Laval',
            'studyProgram': 'Informatique',
            'dateProgramEnd': (datetime.datetime(2016, 5, 1,)-famous_date).total_seconds(),
            'inCharge': False
        }

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)